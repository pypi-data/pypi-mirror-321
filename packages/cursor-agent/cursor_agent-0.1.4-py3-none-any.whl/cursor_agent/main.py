#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
from pathlib import Path
import pkg_resources
import subprocess

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

    def init_cursor_agent(self, force=False):
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

        # Install dependencies
        requirements_path = os.path.join(self.target_dir, "requirements.txt")
        print("Installing dependencies...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error installing dependencies: {e}", file=sys.stderr)
            raise

def main():
    parser = argparse.ArgumentParser(
        description="""Initialize a project with Cursor agent capabilities.
        
Available commands after installation:
  cursor-agent     Initialize directory with agent capabilities
  cursor-llm       Interact with LLM providers (OpenAI, DeepSeek, Anthropic, Gemini, Local)
  cursor-scrape    Web scraping with JavaScript support
  cursor-search    Search engine integration
  cursor-update    Update to latest version
  cursor-verify    Verify setup and dependencies
  cursor-changelog Generate changelog from commits
        
Example usage:
  cursor-agent .                    # Initialize in current directory
  cursor-agent /path/to/project     # Initialize in specific directory
  cursor-llm --prompt "Hello"       # Query default LLM
  cursor-scrape URL1 URL2          # Scrape web pages
  cursor-search "keywords"         # Search the web
  cursor-update --force            # Force update to latest version
  cursor-verify                    # Check setup
  cursor-changelog --update        # Update CHANGELOG.md""")
    parser.add_argument("target_dir", nargs="?", default=".", 
                      help="Target directory to initialize (defaults to current directory)")
    parser.add_argument("--force", "-f", action="store_true",
                      help="Force overwrite existing files (creates backups)")
    
    args = parser.parse_args()
    
    try:
        initializer = CursorAgentInitializer(args.target_dir)
        initializer.init_cursor_agent(force=args.force)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 