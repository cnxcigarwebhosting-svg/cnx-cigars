import json, re

json_path = "/Users/pnwemd/Desktop/Websites/cnx-cigars/src/data/cigars.json"
with open(json_path, 'r') as f:
    cigars = json.load(f)

SIGNATURE = {"cohiba", "montecristo", "romeo y julieta", "romeo", "partagas", "bolivar"}
PREMIUM    = {"h. upmann", "upmann", "hoyo de monterrey", "hoyo", "trinidad", "davidoff"}

def get_category(name):
    n = name.lower()
    for k in SIGNATURE:
        if k in n:
            return "Signature Collection"
    for k in PREMIUM:
        if k in n:
            return "Premium Selection"
    return "Curated Selection"

def short_note(notes):
    if not notes:
        return ""
    # Take first sentence only
    sentence = re.split(r'[.!?]', notes)[0].strip()
    # Cap at 100 chars
    if len(sentence) > 100:
        sentence = sentence[:97] + "..."
    return sentence

for c in cigars:
    c["category"] = get_category(c["name"])
    c["notes"] = short_note(c.get("notes", ""))
    # Remove price from data too
    c.pop("price", None)

# Sort: Signature first, then Premium, then Curated
order = {"Signature Collection": 0, "Premium Selection": 1, "Curated Selection": 2}
cigars.sort(key=lambda c: order[c["category"]])

with open(json_path, 'w') as f:
    json.dump(cigars, f, indent=2)

from collections import Counter
cats = Counter(c["category"] for c in cigars)
print("Re-categorized cigars:")
for k, v in cats.items():
    print(f"  {k}: {v}")
print(f"Total: {len(cigars)}")
