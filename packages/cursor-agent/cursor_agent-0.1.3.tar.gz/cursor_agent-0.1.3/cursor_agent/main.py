#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
from pathlib import Path
import pkg_resources

def get_package_file(filename):
    return pkg_resources.resource_filename('cursor_agent', filename)

class CursorAgentInitializer:
    def __init__(self, target_dir="."):
        self.target_dir = os.path.abspath(target_dir)

    def copy_file_if_not_exists(self, src, dst, force=False):
        if os.path.exists(dst) and not force:
            print(f"Skipping existing file: {dst}")
            return
        
        if force and os.path.exists(dst):
            backup = f"{dst}.bak"
            print(f"Creating backup: {backup}")
            shutil.copy2(dst, backup)
        
        print(f"Created {dst}")
        shutil.copy2(src, dst)

    def init_cursor_agent(self, force=False, skip_venv=False):
        # Create target directory if it doesn't exist
        os.makedirs(self.target_dir, exist_ok=True)
        print(f"Initializing Cursor agent in {self.target_dir}")

        # Copy configuration files
        files_to_copy = [
            ('.cursorrules', os.path.join(self.target_dir, '.cursorrules')),
            ('.env.example', os.path.join(self.target_dir, '.env.example')),
            ('requirements.txt', os.path.join(self.target_dir, 'requirements.txt')),
        ]

        for src_name, dst_path in files_to_copy:
            src_path = get_package_file(src_name)
            self.copy_file_if_not_exists(src_path, dst_path, force)

        if not skip_venv:
            self.setup_virtual_environment()

    def setup_virtual_environment(self):
        # Create virtual environment
        venv_dir = os.path.join(self.target_dir, "venv")
        if not os.path.exists(venv_dir):
            print("Creating virtual environment...")
            import venv
            venv.create(venv_dir, with_pip=True)

        # Install dependencies
        activate_script = "activate" if os.name != "nt" else "activate.bat"
        activate_path = os.path.join(venv_dir, "bin" if os.name != "nt" else "Scripts", activate_script)
        requirements_path = os.path.join(self.target_dir, "requirements.txt")
        
        print("Installing dependencies...")
        pip_path = os.path.join(venv_dir, "bin" if os.name != "nt" else "Scripts", "pip")
        import subprocess
        subprocess.run([pip_path, "install", "-r", requirements_path], check=True)

def main():
    parser = argparse.ArgumentParser(description="Initialize a project with Cursor agent capabilities")
    parser.add_argument("target_dir", nargs="?", default=".", 
                      help="Target directory to initialize (defaults to current directory)")
    parser.add_argument("--force", "-f", action="store_true",
                      help="Force overwrite existing files (creates backups)")
    parser.add_argument("--skip-venv", "-s", action="store_true",
                      help="Skip virtual environment creation and package installation")
    
    args = parser.parse_args()
    
    try:
        initializer = CursorAgentInitializer(args.target_dir)
        initializer.init_cursor_agent(force=args.force, skip_venv=args.skip_venv)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 