import os
import shutil
import frontmatter

# Define target folder paths
base_dir = os.path.join(os.getcwd(), '_posts', 'alifta')
target_dir = os.path.join(base_dir, 'ibn-baz')

matched_count = 0

# Scan all .md files directly inside _posts/alifta
for root, dirs, files in os.walk(base_dir):
    # Skip checking inside 'ibn-baz' if it already exists to avoid re-scanning moved files
    if os.path.abspath(root).startswith(os.path.abspath(target_dir)):
        continue

    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)

            try:
                # Read using utf-8-sig to handle any BOM characters cleanly
                with open(file_path, 'r', encoding='utf-8-sig') as f:
                    post = frontmatter.load(f)

                # Check if 'muftis' structure matches Shaykh Abdul-Aziz ibn Baz
                muftis = post.get('muftis', {})
                shaykh_list = []

                if isinstance(muftis, dict):
                    shaykh_list = muftis.get('shaykh', [])

                is_match = False
                if isinstance(shaykh_list, list):
                    for entry in shaykh_list:
                        if isinstance(entry, dict) and entry.get('name') == 'Shaykh Abdul-Aziz ibn Baz':
                            is_match = True
                            break

                # If found, move the file to the ibn-baz folder
                if is_match:
                    # Create the ibn-baz directory if it does not exist yet
                    if not os.path.exists(target_dir):
                        os.makedirs(target_dir)
                        print(f"Created folder: {target_dir}")

                    destination_path = os.path.join(target_dir, file)
                    
                    # Move the file
                    shutil.move(file_path, destination_path)
                    matched_count += 1
                    print(f"Moved: {file} -> ibn-baz/")

            except Exception as e:
                print(f"Error reading {file}: {e}")

print(f"\nDone! Moved {matched_count} files into '{target_dir}'.")