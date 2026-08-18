import os
import yaml


def update_posts_frontmatter(root_directory):
  print(f"Scanning directory: {root_directory}\n" + "-" * 40)

  updated_count = 0
  skipped_count = 0
  total_files = 0

  for dirpath, _, filenames in os.walk(root_directory):
    for filename in filenames:
      if filename.endswith((".md", ".markdown")):
        total_files += 1
        file_path = os.path.join(dirpath, filename)

        try:
          with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

          if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
              frontmatter_raw = parts[1]
              body = parts[2]

              # Clean up custom delimiters like '///' for parsing
              cleaned_lines = [
                  line
                  for line in frontmatter_raw.splitlines()
                  if not line.strip().startswith("/")
              ]
              cleaned_frontmatter = "\n" + "\n".join(cleaned_lines)

              data = yaml.safe_load(cleaned_frontmatter)

              # Ensure data is a dictionary
              if not isinstance(data, dict):
                data = {}

              # Check if 'active' is already set to 'audios'
              if data.get("active") == "videos":
                print(f"[SKIPPED] Already has active: audios -> {file_path}")
                skipped_count += 1
              else:
                # Add or update the 'active' property
                data["active"] = "vidoes"

                # Rebuild the frontmatter text
                # Preserve your custom '///' style or standard YAML format
                new_frontmatter_lines = ["---"]
                
                # Check if original had the custom '///' styling
                has_custom_slashes = "///" in frontmatter_raw

                for key, value in data.items():
                  if has_custom_slashes:
                    new_frontmatter_lines.append(f"///\n///\n{key}: {value}\n///\n///\n///")
                  else:
                    new_frontmatter_lines.append(f"{key}: {value}")

                # If using standard YAML serialization instead of custom lines, use this cleaner approach:
                # Let's write it out cleanly using standard YAML block format:
                new_yaml = yaml.dump(data, sort_keys=False, default_flow_style=False).strip()
                
                # Reconstruct file content
                if has_custom_slashes:
                    # Re-insert your specific custom delimiters if preferred
                    formatted_data = "\n".join([f"///\n{k}: {v}\n///" for k, v in data.items()])
                    new_content = f"---\n{formatted_data}\n---{body}"
                else:
                    new_content = f"---\n{new_yaml}\n---{body}"

                # Write changes back to the file
                with open(file_path, "w", encoding="utf-8") as f:
                  f.write(new_content)

                print(f"[UPDATED] Added active: audios -> {file_path}")
                updated_count += 1

        except Exception as e:
          print(f"[ERROR] Could not process {file_path}: {e}")

  print("-" * 40)
  print(f"Process complete.")
  print(f"Total files checked: {total_files}")
  print(f"Files updated: {updated_count}")
  print(f"Files skipped (already had it): {skipped_count}")


if __name__ == "__main__":
  # Specify your target directory here
  target_dir = "_posts/salih-ibn-fawzan/videos"
  
  # Run the updater
  update_posts_frontmatter(target_dir)