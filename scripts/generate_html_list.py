import os
import json

INDEX_FILE = "html.json"

def generate_index_json():
    html_files = []

    for root, dirs, files in os.walk("."):
        for f in files:
            if f.lower().endswith((".html", ".htm")):
                # store path like folder/file.html
                html_files.append(os.path.relpath(os.path.join(root, f)))

    html_files.sort()

    with open(INDEX_FILE, "w", encoding="utf-8") as out:
        json.dump({"files": html_files}, out, indent=2)

    print(f"html.json generated with {len(html_files)} files:")
    for f in html_files:
        print(" -", f)

if __name__ == "__main__":
    generate_index_json()
