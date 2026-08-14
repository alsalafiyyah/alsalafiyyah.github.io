from pathlib import Path

# Target directory
SCHOLAR_DIR = Path("_pages/scholar")


def convert_html_to_md():
    if not SCHOLAR_DIR.exists():
        print(
            f"Directory '{SCHOLAR_DIR}' not found. Please run the script from your site root."
        )
        return

    renamed_count = 0
    skipped_count = 0

    print(f"Scanning for .html files inside '{SCHOLAR_DIR}'...\n")

    # Recursively traverse all subfolders inside _pages/scholar/
    for file_path in SCHOLAR_DIR.rglob("*"):
        if file_path.is_file():
            if file_path.suffix.lower() == ".html":
                new_path = file_path.with_suffix(".md")

                # Safeguard against overwriting an existing file
                if new_path.exists():
                    print(
                        f"[SKIP] Cannot rename '{file_path.name}' -> '{new_path.name}' (file already exists)"
                    )
                    skipped_count += 1
                    continue

                file_path.rename(new_path)
                renamed_count += 1
                print(
                    f"[RENAMED] {file_path.relative_to(SCHOLAR_DIR)} -> {new_path.name}"
                )

    print("\n--- Execution Summary ---")
    print(f"Total files renamed to .md: {renamed_count}")
    if skipped_count > 0:
        print(f"Total files skipped (conflicts): {skipped_count}")


if __name__ == "__main__":
    convert_html_to_md()