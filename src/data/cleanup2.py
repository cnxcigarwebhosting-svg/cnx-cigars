import json

json_path = "/Users/pnwemd/Desktop/Websites/cnx-cigars/src/data/cigars.json"
with open(json_path, 'r') as f:
    cigars = json.load(f)

# Filter out obvious OCR errors
bad_keywords = ["ter:", "smoking", "quit", "nhs", "cigarilles", "40%", "club", "get help", "maduro", "aniversario", "reserva", "exclusivo"]

cleaned = []
for c in cigars:
    name_lower = c["name"].lower()
    if any(k in name_lower for k in bad_keywords) or len(name_lower) < 5 or "thb" in name_lower or name_lower.startswith("o julieta") or name_lower.startswith("cuba") or name_lower.startswith("open"):
        print(f"Removing: {c['name']}")
        continue
    cleaned.append(c)

with open(json_path, 'w') as f:
    json.dump(cleaned, f, indent=2)

print(f"Remaining cigars: {len(cleaned)}")
