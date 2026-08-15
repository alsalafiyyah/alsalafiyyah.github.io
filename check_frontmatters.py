import os
import re
from pathlib import Path

def has_two_frontmatters(file_path):
    """
    Checks if a markdown file contains at least two frontmatter blocks.
    A frontmatter block is defined as content starting and ending with '---'.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

    # Regex to find YAML frontmatter blocks at the beginning or separated by whitespace.
    # This matches blocks starting with '---' at the start of a line and ending with '---'.
    # We use multiline and dotall flags.
    pattern = r'^---\s*\n.*?\n---\s*$'
    matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)

    # Return True if we found 2 or more frontmatter blocks
    return len(matches) >= 2

def scan_posts_directory(directory_path):
    """
    Scans the given directory for .md or .markdown files with double frontmatters.
    """
    target_dir = Path(directory_path)
    
    if not target_dir.exists():
        print(f"Directory not found: {directory_path}")
        return

    print(f"Scanning '{target_dir.absolute()}' for posts with multiple frontmatters...\n")
    
    match_count = 0
    # Search for markdown files recursively
    for file_path in target_dir.rglob("*"):
        if file_path.suffix.lower() in ['.md', '.markdown']:
            if has_two_frontmatters(file_path):
                print(f"[MATCH] {file_path}")
                match_count += 1

    print(f"\nScan complete. Found {match_count} file(s) with multiple frontmatters.")

if __name__ == "__main__":
    # Change 'posts' to your actual directory path (e.g., '_posts' or './content')
    DIRECTORY_TO_SCAN = "_posts/alifta"
    
    scan_posts_directory(DIRECTORY_TO_SCAN)