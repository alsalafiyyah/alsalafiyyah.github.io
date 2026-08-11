from pathlib import Path

# Target directory
CATEGORIES_DIR = Path("_categories")


def rename_html_to_md():
    if not CATEGORIES_DIR.exists():
        print(f"Directory '{CATEGORIES_DIR}' does not exist.")
        return

    renamed_count = 0

    # Search recursively for all .html files (handles subfolders if present)
    for html_file in CATEGORIES_DIR.rglob("*.html"):
        # Create target path with .md extension
        md_file = html_file.with_suffix(".md")

        # Rename file
        html_file.rename(md_file)
        renamed_count += 1
        print(f"Renamed: {html_file.relative_to(CATEGORIES_DIR)} -> {md_file.name}")

    print("\n--- Execution Summary ---")
    print(f"Total files renamed to .md: {renamed_count}")


if __name__ == "__main__":
    rename_html_to_md()