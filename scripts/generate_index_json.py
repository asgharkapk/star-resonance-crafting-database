import os
import json

# Path to the data folder (relative to script)
DATA_DIR = "data"
INDEX_FILE = os.path.join(DATA_DIR, "index.json")

def generate_index_json():
    if not os.path.exists(DATA_DIR):
        print(f"Error: '{DATA_DIR}' folder does not exist.")
        return

    # List all CSV files
    csv_files = [f for f in os.listdir(DATA_DIR)
                 if f.lower().endswith(".csv") and os.path.isfile(os.path.join(DATA_DIR, f))]

    if not csv_files:
        print("No CSV files found in data folder.")
    
    # Prepare JSON structure
    index_data = {"files": csv_files}

    # Write to index.json
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2)

    print(f"index.json generated successfully with {len(csv_files)} file(s).")

if __name__ == "__main__":
    generate_index_json()
