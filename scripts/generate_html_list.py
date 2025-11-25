import os
import json

DATA_DIR = "data"
INDEX_FILE = os.path.join(DATA_DIR, "index.json")

def generate_index_json():
    if not os.path.exists(DATA_DIR):
        print(f"Error: '{DATA_DIR}' folder does not exist.")
        return

    # List all HTML files
    html_files = [f for f in os.listdir(DATA_DIR)
                  if f.lower().endswith((".html", ".htm")) and os.path.isfile(os.path.join(DATA_DIR, f))]

    if not html_files:
        print("No HTML files found in data folder.")

    # Optional: sort alphabetically
    html_files.sort()

    # Prepare JSON structure
    index_data = {"files": html_files}

    # Write to index.json
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2)

    print(f"index.json generated successfully with {len(html_files)} file(s):")
    for f in html_files:
        print(f" - {f}")

if __name__ == "__main__":
    generate_index_json()
