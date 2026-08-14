import re
import shutil
from pathlib import Path

# Path configuration
TARGET_DIR = Path("_posts/alifta")
DEST_DIR = TARGET_DIR / "sects"

# Regex pattern matching target Shia/Ismaili-related terms
PATTERN = re.compile(
    r"\b(shia|shi'a|shi`a|shiah|shi'ah|shi`ah|shiites|shiis|ismailis|ismailiyyah|"
    r"shi'ites|isma'iliyyah|khomeiniyyah|khomeinism|khomeini|imamate|imamis|"
    r"imamiyah|imamiyyah|shi'i|shi'is|shi`i|shi`is|shi''ah|Al-Quburiyyah|Al-Quburiyyun|Al-Quburis|sufism|sufi|sufis|grave-worshippers|grave-worship|Al-Mu'tazilah|Al-Jahmiyyah)\b",
    re.IGNORECASE,
)


def move_matching_posts(directory: Path, destination: Path):
    if not directory.exists():
        print(f"Directory not found: {directory.resolve()}")
        return

    # Create destination directory if it doesn't exist
    destination.mkdir(parents=True, exist_ok=True)

    moved_count = 0

    # Collect file paths first before moving them
    all_files = list(directory.rglob("*.md"))

    for file_path in all_files:
        # Skip files already in the target destination folder
        if destination in file_path.parents:
            continue

        # Read file content safely
        content = None
        try:
            content = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                content = file_path.read_text(encoding="latin-1")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue

        # If pattern matches, move the file
        if content and PATTERN.search(content):
            target_path = destination / file_path.name

            # Prevent overwriting if a file with the exact same name exists in destination
            if target_path.exists() and target_path != file_path:
                # Append parent folder name to filename to ensure uniqueness
                unique_name = f"{file_path.stem}_{file_path.parent.name}{file_path.suffix}"
                target_path = destination / unique_name

            shutil.move(str(file_path), str(target_path))
            print(f"Moved: {file_path} -> {target_path}")
            moved_count += 1

    print(f"\nDone! Successfully moved {moved_count} file(s) to '{destination}'.")


if __name__ == "__main__":
    move_matching_posts(TARGET_DIR, DEST_DIR)