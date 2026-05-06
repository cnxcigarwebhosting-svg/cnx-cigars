import json, re

json_path = "/Users/pnwemd/Desktop/Websites/cnx-cigars/src/data/cigars.json"
with open(json_path) as f:
    cigars = json.load(f)

# Fix strength field - clean up "Mi" -> "Mild", "3/5" -> remove, etc.
def fix_strength(s):
    if not s: return ""
    s = s.strip()
    if s in ("3/5", "2/5", "4/5", "5/5"): return ""
    if re.match(r'^mi$', s, re.I): return "Mild"
    if re.match(r'^meduim', s, re.I): return "Medium"
    # Cap length
    if len(s) > 30: return s[:27] + "..."
    return s

# Fix notes - strip remaining OCR junk
def fix_notes(n):
    if not n: return ""
    # Remove "Strenght :" / "Strength" prefixes 
    n = re.sub(r'(?:strenght?\s*:?\s*|stregnth\s*:?\s*)', '', n, flags=re.I).strip()
    # Remove "Size:", "Vitola:", "wrapper:", "Binder:", etc.
    n = re.sub(r'(?:size|vitola|wrapper|binder|filler)\s*:', '', n, flags=re.I).strip()
    # Remove "m (4 ¾ inches) agnum 54" type fragments
    n = re.sub(r'\bm\s*\(\s*[\d\s¾½¼]+inches?\s*\)[^\.]*', '', n, flags=re.I).strip()
    n = n.strip(" .,;:-/")
    if len(n) < 8:
        return ""
    # First sentence only, capped at 120 chars
    sentence = re.split(r'[.!?]', n)[0].strip()
    if len(sentence) > 120: sentence = sentence[:117] + "..."
    return sentence

# Remove badly-named OCR ghost entries
BAD_IDS = {"nch-punci", "rie-d-no", "churchills", "henry", "magnum-54", "nande", "original", "quintero"}

cleaned = []
for c in cigars:
    if c["id"] in BAD_IDS:
        print(f"Removing ghost: {c['name']}")
        continue
    c["strength"] = fix_strength(c.get("strength", ""))
    c["notes"] = fix_notes(c.get("notes", ""))
    cleaned.append(c)

with open(json_path, 'w') as f:
    json.dump(cleaned, f, indent=2)

from collections import Counter
cats = Counter(c["category"] for c in cleaned)
print(f"\nFinal counts: {dict(cats)}")
print(f"Total cigars: {len(cleaned)}")
