import json, re

json_path = "/Users/pnwemd/Desktop/Websites/cnx-cigars/src/data/cigars.json"
with open(json_path) as f:
    cigars = json.load(f)

JUNK_PATTERNS = [
    r'(?:smoking|oking)\s*time\s*:.*',         # "oking time: 45 mins ..."
    r'size\s*:\s*\S[^\.]+',                     # "Size: Pyramides ..."
    r'strength\s*:\s*\S[^\.]+',                 # "Strength: Medium ..."
    r'length\s*:.*',
    r'ring\s*gauge\s*:.*',
    r'\d+\s*/\s*5',                             # rating "3/5"
    r'the\s+\w+\s+no\b.*',                      # "The Montecristo No..."
    r'endu\w+',                                 # "enduontecristo"
    r'ost\s+best\s+selling',                    # "ost best selling"
    r'^[a-z]\s*/\s*\d',                         # "m / 5"
    r'oke\s+with',
]

MANUAL_NOTES = {
    "montecristo-edmundo": "A rich, full-bodied Robusto Extra with cedar and dark chocolate nuances.",
    "montecristo-no-2": "The world's most celebrated torpedo — earthy, complex, and perfectly balanced.",
    "montecristo-no-4": "The best-selling Cuban cigar of all time. Smooth, creamy, and endlessly refined.",
    "partagas-serie-d-no-4": "Bold Cuban robusto with dense, peppery smoke and rich coffee undertones.",
    "bolivar-belicoso-fino": "One of Cuba's most powerful cigars — intensely earthy and full-bodied.",
    "bolivar-royal-corona": "Robust and rich with leather, cedar, and a signature Bolivar spice.",
}

for c in cigars:
    note = c.get("notes", "") or ""
    
    # If we have a manual override, use it
    if c["id"] in MANUAL_NOTES:
        c["notes"] = MANUAL_NOTES[c["id"]]
        continue

    # Strip known junk patterns from the note
    for pat in JUNK_PATTERNS:
        note = re.sub(pat, '', note, flags=re.IGNORECASE).strip()
    
    # Strip leftover boilerplate
    note = note.strip(" .,;:-/")
    
    # If it's too short or just garbage, clear it
    if len(note) < 12 or note.isdigit():
        note = ""
    
    c["notes"] = note

with open(json_path, 'w') as f:
    json.dump(cigars, f, indent=2)

# Print results for review
for c in cigars:
    print(f"[{c['category'][:3]}] {c['name'][:30]:<30} | {c.get('strength','')[:18]:<18} | {c.get('notes','')[:60]}")
