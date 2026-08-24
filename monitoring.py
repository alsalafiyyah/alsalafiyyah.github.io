import os
import json
import time
import subprocess

POSTS_DIR = "_posts"
STATE_FILE = ".workflow_state.json"
DELAY_SECONDS = 5  # Slow down execution between posts

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return set(json.load(f))
    return set()

def save_state(processed_posts):
    with open(STATE_FILE, "w") as f:
        json.dump(list(processed_posts), f)

def run_workflow_for_post(post_path):
    print(f"--> Processing post: {post_path}")
    
    # Example: Run a command or trigger your specific tool/workflow
    # subprocess.run(["bundle", "exec", "jekyll", "build"], check=True)
    
    # Simulate workflow step completion
    time.sleep(DELAY_SECONDS)
    print(f"--> Completed: {post_path}\n")

def main():
    processed_posts = load_state()
    
    if not os.path.exists(POSTS_DIR):
        print(f"Error: Directory '{POSTS_DIR}' not found.")
        return

    all_posts = {os.path.join(POSTS_DIR, f) for f in os.listdir(POSTS_DIR) if f.endswith(('.md', '.markdown'))}
    
    # Identify posts that haven't been processed yet
    new_posts = sorted(list(all_posts - processed_posts))
    
    if not new_posts:
        print("No new Jekyll posts found to process.")
        return

    print(f"Found {len(new_posts)} new post(s). Starting slow workflow...")

    for post in new_posts:
        run_workflow_for_post(post)
        processed_posts.add(post)
        save_state(processed_posts)  # Save progress incrementally

    print("All workflows completed successfully!")

if __name__ == "__main__":
    main()