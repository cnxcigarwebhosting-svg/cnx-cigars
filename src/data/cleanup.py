import json

json_path = "/Users/pnwemd/Desktop/Websites/cnx-cigars/src/data/cigars.json"
with open(json_path, 'r') as f:
    data = json.load(f)

# Filter out empty IDs and obviously wrong OCR like NHS quit lines
filtered = [c for c in data if c["id"] and "quit" not in c["id"] and len(c["name"]) > 3]

with open(json_path, 'w') as f:
    json.dump(filtered, f, indent=2)

print(f"Cleaned up {len(data) - len(filtered)} bad entries.")
