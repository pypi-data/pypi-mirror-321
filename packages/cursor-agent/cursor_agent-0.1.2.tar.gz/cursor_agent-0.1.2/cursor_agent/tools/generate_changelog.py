#!/usr/bin/env python3
import os
import re
import sys
import subprocess
from datetime import datetime
from typing import List, Tuple

def get_latest_tag() -> str:
    """Get the latest git tag."""
    try:
        result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def get_commits_since_tag(tag: str = None) -> List[Tuple[str, str, str]]:
    """Get all commits since the specified tag."""
    if tag:
        try:
            # Try to get commits since tag
            cmd = ["git", "log", "--pretty=format:%h|%s|%an", f"{tag}..HEAD"]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError:
            # If tag doesn't exist, get all commits
            cmd = ["git", "log", "--pretty=format:%h|%s|%an"]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    else:
        # Get all commits if no tag specified
        cmd = ["git", "log", "--pretty=format:%h|%s|%an"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    
    commits = []
    for line in result.stdout.split("\n"):
        if line:
            hash, message, author = line.split("|")
            commits.append((hash, message, author))
    
    return commits

def categorize_commit(message: str) -> str:
    """Categorize commit based on conventional commit message."""
    categories = {
        "feat": "Features",
        "fix": "Bug Fixes",
        "docs": "Documentation",
        "style": "Style",
        "refactor": "Code Refactoring",
        "perf": "Performance",
        "test": "Tests",
        "build": "Build System",
        "ci": "CI/CD",
        "chore": "Chores",
    }
    
    pattern = r"^(\w+)(?:\(([^)]+)\))?: (.+)"
    match = re.match(pattern, message)
    
    if match:
        type_ = match.group(1)
        return categories.get(type_, "Other Changes")
    return "Other Changes"

def generate_changelog(version: str = None) -> str:
    """Generate changelog content."""
    if not version:
        version = get_latest_tag()
        if version:
            # Strip 'v' prefix if present and increment patch version
            version = version.lstrip("v").split(".")
            version[-1] = str(int(version[-1]) + 1)
            version = "v" + ".".join(version)
        else:
            version = "v0.1.0"
    
    date = datetime.now().strftime("%Y-%m-%d")
    changelog = [f"# {version} ({date})\n"]
    
    # Get and categorize commits
    commits = get_commits_since_tag(version)
    categorized = {}
    
    for hash, message, author in commits:
        category = categorize_commit(message)
        if category not in categorized:
            categorized[category] = []
        categorized[category].append((hash, message, author))
    
    # Generate formatted changelog
    for category in sorted(categorized.keys()):
        if categorized[category]:
            changelog.append(f"## {category}\n")
            for hash, message, author in categorized[category]:
                changelog.append(f"* {message} ({hash}) - {author}")
            changelog.append("")
    
    return "\n".join(changelog)

def update_changelog_file(content: str) -> None:
    """Update CHANGELOG.md file."""
    if os.path.exists("CHANGELOG.md"):
        with open("CHANGELOG.md", "r") as f:
            existing = f.read()
    else:
        existing = "# Changelog\n\n"
    
    # Insert new content after the header
    with open("CHANGELOG.md", "w") as f:
        parts = existing.split("\n", 2)
        f.write(parts[0] + "\n\n" + content + "\n")
        if len(parts) > 2:
            f.write(parts[2])

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate changelog from git commits")
    parser.add_argument("--version", "-v", help="Version number (default: increment latest)")
    parser.add_argument("--update", "-u", action="store_true", help="Update CHANGELOG.md")
    args = parser.parse_args()
    
    try:
        changelog = generate_changelog(args.version)
        if args.update:
            update_changelog_file(changelog)
        else:
            print(changelog)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 