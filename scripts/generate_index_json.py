import os
import json

DATA_DIR = "data"
INDEX_FILE = os.path.join(DATA_DIR, "index.json")

def generate_index_json():
    if not os.path.exists(DATA_DIR):
        print(f"Error: '{DATA_DIR}' folder does not exist.")
        return

    # List all CSV or CVS files
    csv_files = [f for f in os.listdir(DATA_DIR)
                 if f.lower().endswith((".csv", ".cvs")) and os.path.isfile(os.path.join(DATA_DIR, f))]

    if not csv_files:
        print("No CSV/CVS files found in data folder.")

    # Optional: sort alphabetically
    csv_files.sort()

    # Prepare JSON structure
    index_data = {"files": csv_files}

    # Write to index.json
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2)

    print(f"index.json generated successfully with {len(csv_files)} file(s):")
    for f in csv_files:
        print(f" - {f}")

if __name__ == "__main__":
    generate_index_json()
