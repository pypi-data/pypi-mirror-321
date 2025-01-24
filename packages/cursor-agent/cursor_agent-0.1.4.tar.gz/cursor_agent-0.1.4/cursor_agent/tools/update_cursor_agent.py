#!/usr/bin/env python3
import os
import sys
import json
import subprocess
import pkg_resources
from urllib.request import urlopen
from packaging import version

def get_latest_version():
    """Get the latest version from PyPI."""
    try:
        url = "https://pypi.org/pypi/cursor-agent/json"
        with urlopen(url) as response:
            data = json.loads(response.read())
            return data["info"]["version"]
    except Exception as e:
        print(f"Error checking latest version: {e}", file=sys.stderr)
        return None

def get_current_version():
    """Get the currently installed version."""
    try:
        return pkg_resources.get_distribution("cursor-agent").version
    except pkg_resources.DistributionNotFound:
        return None

def update_cursor_agent(force=False):
    """Update cursor-agent to the latest version."""
    current_version = get_current_version()
    latest_version = get_latest_version()

    if not latest_version:
        print("Could not determine latest version. Please try again later.")
        return False

    if current_version:
        print(f"Current version: {current_version}")
        print(f"Latest version: {latest_version}")

        if not force and version.parse(current_version) >= version.parse(latest_version):
            print("You already have the latest version!")
            return True
    else:
        print("cursor-agent is not installed.")
        print(f"Latest version available: {latest_version}")

    try:
        # Install or upgrade the package
        subprocess.run([
            sys.executable, "-m", "pip", "install", "--upgrade",
            "cursor-agent"
        ], check=True)

        # Verify the installation
        new_version = get_current_version()
        if new_version == latest_version:
            print(f"\nSuccessfully updated to version {new_version}!")
            return True
        else:
            print("\nUpdate may have failed. Please try again.", file=sys.stderr)
            return False

    except subprocess.CalledProcessError as e:
        print(f"\nError during update: {e}", file=sys.stderr)
        return False

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Update cursor-agent to the latest version")
    parser.add_argument("--force", "-f", action="store_true", 
                       help="Force update even if current version is up to date")
    args = parser.parse_args()

    try:
        success = update_cursor_agent(force=args.force)
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\nUpdate cancelled by user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 