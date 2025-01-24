#!/usr/bin/env python3
import os
import sys
import json
import shutil
import tempfile
import subprocess
from pathlib import Path
from typing import List, Dict, Any

class SetupVerifier:
    def __init__(self):
        self.results: Dict[str, List[Dict[str, Any]]] = {
            "success": [],
            "failure": [],
            "skipped": []
        }
        self.temp_dir = tempfile.mkdtemp()
        self.project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(f"Project root: {self.project_root}")
        print(f"Using temporary directory: {self.temp_dir}")

    def cleanup(self):
        """Clean up temporary files."""
        try:
            shutil.rmtree(self.temp_dir)
        except Exception as e:
            print(f"Warning: Failed to clean up {self.temp_dir}: {e}")

    def copy_project_files(self):
        """Copy project files to temporary directory."""
        exclude = {".git", "venv", "__pycache__", "*.pyc", "*.pyo", "*.pyd", "*.so"}
        def ignore_patterns(path, names):
            return {n for n in names if any(p in n for p in exclude)}
        
        shutil.copytree(
            self.project_root,
            self.temp_dir,
            dirs_exist_ok=True,
            ignore=ignore_patterns
        )
        print(f"Copied project files to {self.temp_dir}")

    def log_result(self, category: str, test: str, details: str = None):
        """Log a test result."""
        self.results[category].append({
            "test": test,
            "details": details
        })
        status = "✅" if category == "success" else "❌" if category == "failure" else "⏭️"
        print(f"{status} {test}")
        if details:
            print(f"   {details}")

    def run_command(self, cmd: List[str], cwd: str = None) -> tuple[int, str, str]:
        """Run a command and return exit code, stdout, and stderr."""
        try:
            result = subprocess.run(
                cmd,
                cwd=cwd or self.temp_dir,
                capture_output=True,
                text=True,
                check=False,
                env=os.environ.copy()
            )
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            return 1, "", str(e)

    def verify_python_setup(self):
        """Verify Python package installation and CLI."""
        print("\n📦 Verifying Python Setup...")
        
        # Create virtual environment
        code, out, err = self.run_command([sys.executable, "-m", "venv", "venv"])
        if code != 0:
            self.log_result("failure", "Create virtual environment", err)
            return

        # Get the correct Python executable path
        if sys.platform == "win32":
            venv_python = os.path.join(self.temp_dir, "venv", "Scripts", "python.exe")
        else:
            venv_python = os.path.join(self.temp_dir, "venv", "bin", "python")

        # Upgrade pip
        code, out, err = self.run_command([venv_python, "-m", "pip", "install", "--upgrade", "pip"])
        if code != 0:
            self.log_result("failure", "Upgrade pip", err)
            return

        # Install package in editable mode
        code, out, err = self.run_command([venv_python, "-m", "pip", "install", "-e", "."])
        if code != 0:
            self.log_result("failure", "Install package", err)
            return
        
        self.log_result("success", "Python package installation")

        # Test CLI by running the script directly
        code, out, err = self.run_command([venv_python, "init_cursor_agent.py", "--help"])
        if code != 0:
            self.log_result("failure", "CLI help command", err)
        else:
            self.log_result("success", "CLI functionality")

    def verify_docker_setup(self):
        """Verify Docker build and run."""
        print("\n🐳 Verifying Docker Setup...")
        
        # Check if Docker is available
        code, out, err = self.run_command(["docker", "--version"])
        if code != 0:
            self.log_result("skipped", "Docker verification", "Docker not available")
            return

        # Build Docker image
        code, out, err = self.run_command(["docker", "build", "-t", "cursor-agent", "."])
        if code != 0:
            self.log_result("failure", "Docker build", err)
            return
        self.log_result("success", "Docker build")

        # Test Docker run
        code, out, err = self.run_command([
            "docker", "run", "--rm", "cursor-agent", "--help"
        ])
        if code != 0:
            self.log_result("failure", "Docker run", err)
        else:
            self.log_result("success", "Docker run")

        # Test Docker Compose
        code, out, err = self.run_command(["docker-compose", "--version"])
        if code == 0:
            code, out, err = self.run_command(["docker-compose", "config"])
            if code == 0:
                self.log_result("success", "Docker Compose configuration")
            else:
                self.log_result("failure", "Docker Compose configuration", err)
        else:
            self.log_result("skipped", "Docker Compose verification", "Docker Compose not available")

    def verify_git_setup(self):
        """Verify Git configuration and changelog generation."""
        print("\n📝 Verifying Git Setup...")
        
        # Initialize test git repository
        code, out, err = self.run_command(["git", "init"])
        if code != 0:
            self.log_result("failure", "Git initialization", err)
            return

        # Configure test user
        self.run_command(["git", "config", "user.name", "Test User"])
        self.run_command(["git", "config", "user.email", "test@example.com"])

        # Create test commits
        test_commits = [
            "feat: test feature",
            "fix: test bugfix",
            "docs: test documentation"
        ]
        
        for msg in test_commits:
            # Create a dummy file change
            with open(os.path.join(self.temp_dir, "test.txt"), "a") as f:
                f.write(f"{msg}\n")
            
            # Commit change
            self.run_command(["git", "add", "test.txt"])
            code, out, err = self.run_command(["git", "commit", "-m", msg])
            if code != 0:
                self.log_result("failure", f"Git commit: {msg}", err)
                return

        self.log_result("success", "Git commits")

        # Create initial tag
        code, out, err = self.run_command(["git", "tag", "v0.1.0"])
        if code != 0:
            self.log_result("failure", "Create git tag", err)
            return

        # Add one more commit for changelog
        with open(os.path.join(self.temp_dir, "test.txt"), "a") as f:
            f.write("feat: another feature\n")
        self.run_command(["git", "add", "test.txt"])
        self.run_command(["git", "commit", "-m", "feat: another feature"])

        # Test changelog generation
        code, out, err = self.run_command([sys.executable, "tools/generate_changelog.py"])
        if code != 0:
            self.log_result("failure", "Changelog generation", err)
        else:
            self.log_result("success", "Changelog generation")
            print("\nSample changelog:")
            print(out)

    def print_summary(self):
        """Print test results summary."""
        print("\n📊 Test Summary:")
        print(f"✅ Passed: {len(self.results['success'])}")
        print(f"❌ Failed: {len(self.results['failure'])}")
        print(f"⏭️ Skipped: {len(self.results['skipped'])}")
        
        if self.results['failure']:
            print("\n❌ Failed Tests:")
            for failure in self.results['failure']:
                print(f"- {failure['test']}")
                if failure['details']:
                    print(f"  Details: {failure['details']}")

    def run_all_tests(self):
        """Run all verification tests."""
        try:
            # Copy project files first
            self.copy_project_files()
            
            # Run verifications
            self.verify_python_setup()
            self.verify_docker_setup()
            self.verify_git_setup()
            self.print_summary()
        finally:
            self.cleanup()
        
        # Return non-zero exit code if any tests failed
        return len(self.results['failure']) == 0

def main():
    verifier = SetupVerifier()
    success = verifier.run_all_tests()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main() 