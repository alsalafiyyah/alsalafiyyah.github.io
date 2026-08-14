import re
from pathlib import Path

# Adjust path if your folder structure is '_posts/alifta/sects' or '_alifta/sects'
TARGET_DIR = Path("_posts/alifta/sects")

# Regex to check if category is already present in frontmatter
CATEGORY_PATTERN = re.compile(r"category:\s*\[\s*sects\s*\]", re.IGNORECASE)


def update_frontmatter(file_path: Path) -> bool:
    content = file_path.read_text(encoding="utf-8")

    # Match frontmatter block (starts and ends with ---)
    pattern = re.compile(r"^(---\r?\n)(.*?)(^---\r?\n)", re.DOTALL | re.MULTILINE)
    match = pattern.search(content)

    if not match:
        print(f"Skipped (No YAML frontmatter found): {file_path.name}")
        return False

    header, frontmatter, footer = match.group(1), match.group(2), match.group(3)

    # Check if 'category: [sects]' is already present
    if CATEGORY_PATTERN.search(frontmatter):
        print(f"Skipped (Category already exists): {file_path.name}")
        return False

    # Ensure frontmatter has a ending newline before adding the new line
    if not frontmatter.endswith("\n"):
        frontmatter += "\n"

    # Append category line
    updated_frontmatter = frontmatter + "category: [sects]\n"

    # Reconstruct the full file content
    new_content = header + updated_frontmatter + footer + content[match.end() :]

    file_path.write_text(new_content, encoding="utf-8")
    print(f"Updated: {file_path.name}")
    return True


def main():
    if not TARGET_DIR.exists():
        print(f"Directory not found: {TARGET_DIR.resolve()}")
        return

    updated_count = 0
    skipped_count = 0

    files = list(TARGET_DIR.glob("*.md")) + list(TARGET_DIR.rglob("*.md"))
    # Remove duplicates if rglob caught glob items
    files = sorted(list(set(files)))

    print(f"Found {len(files)} file(s) in '{TARGET_DIR}'\n")

    for file_path in files:
        if update_frontmatter(file_path):
            updated_count += 1
        else:
            skipped_count += 1

    print(
        f"\nDone! Processed {len(files)} files: {updated_count} updated, {skipped_count} skipped."
    )


if __name__ == "__main__":
    main()