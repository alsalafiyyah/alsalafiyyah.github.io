import os
import re
import frontmatter

target_dir = os.path.join(os.getcwd(), '_posts', 'alifta')

updated_count = 0

for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)

            # Read raw text to handle double frontmatter and BOM manually
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                content = f.read()

            # Parse frontmatter from the raw string
            post = frontmatter.loads(content)

            # --- CLEANUP KEYS ---
            if 'category' in post:
                del post['category']
            if 'categories' in post:
                del post['categories']
            if 'locale' in post:
                del post['locale']
            if 'note' in post:
                del post['note']

            # --- ADD / FIX KEYS ---
            post['lang'] = 'en'
            post['mass_edited'] = True

            # Write clean output back to file
            clean_output = frontmatter.dumps(post)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(clean_output)
                
            updated_count += 1
            print(f"Fixed: {file}")

print(f"\nDone! Successfully cleaned and formatted {updated_count} files.")