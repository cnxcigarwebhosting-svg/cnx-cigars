import json

json_path = "/Users/pnwemd/Desktop/Websites/cnx-cigars/src/data/cigars.json"
with open(json_path) as f:
    cigars = json.load(f)

# ─── MASTER DESCRIPTION MAP ───────────────────────────────────────────────────
# keyed by cigar ID from the JSON
DESCRIPTIONS = {
    # SIGNATURE COLLECTION
    "cohiba-siglo-ii":
        "Medium-bodied Cuban cigar with refined balance, smooth cedar, subtle spice, and a clean, elegant finish.",
    "cohiba-robusto":
        "Rich, medium-to-full cigar with deep spice, wood, and signature Cohiba complexity from additional fermentation.",
    "montecristo-no-2":
        "Iconic full-flavored pyramides with pepper, cocoa, and a rich, evolving profile.",
    "montecristo-no-4":
        "Balanced and approachable with creamy texture, cocoa, and light spice notes.",
    "montecristo-edmundo":
        "Medium-to-full bodied robusto delivering bold pepper, earth, and satisfying richness.",
    "romeo-y-julieta-short-churchill":
        "Medium-bodied robusto with balanced wood, earth, and light spice.",
    "partagas-serie-d-no-4":
        "Full-bodied classic with bold spice, earth, and deep, rich character.",
    "partagas-serie-pyramides-no-2":
        "Strong pyramides offering cocoa, pepper, earth, and complex spice layers.",
    "bolivar-royal-corona":
        "Medium-full cigar with earthy richness, wood, and herbal complexity.",
    "bolivar-belicoso-fino":
        "Full-bodied cigar with leather, spice, chocolate, and a powerful, smooth profile.",

    # PREMIUM SELECTION
    "hoyo-de-monterrey-epicure-no-2":
        "Mild-medium cigar with creamy texture, cedar, and light, approachable character.",
    "hoyo-de-monterrey-epicure-especial":
        "Smooth, creamy cigar with notes of cocoa, coffee, leather, and soft spice.",
    "h-upmann-mag-46":
        "Medium-bodied refined smoke with cedar, nuts, coffee, and balanced creaminess.",
    "h-upmann-half-corona":
        "Light-medium cigar, smooth and subtle with approachable flavor progression.",
    "trinidad-vigia":
        "Creamy medium-bodied cigar with honey, cedar, and signature smooth richness.",
    "trinidad-media-luna":
        "Balanced cigar with notes of leather, nuttiness, and subtle sweetness.",
    "the-davidoff-signature-2000":
        "Mild and elegant with creamy texture, wood, and floral nuances.",
    "davidoff-churchill-the-late-hour":
        "Medium-full cigar with pepper, oak, espresso, and deep richness.",
    "davidoff-yamasa-petit-churchill":
        "Complex medium-full cigar with spice, earth, and bold character.",

    # CURATED SELECTION
    "juan-lopez-seleccion-no-2":
        "Medium-bodied cigar with woody, herbal, and lightly spiced character.",
    "quai-d-orsay-50":
        "Smooth and elegant with vanilla, cedar, and hazelnut notes.",
    "punch-short-de-punch":
        "Medium-full cigar with cedar, spice, and earthy balance.",
    "jose-l-piedra-cazadores":
        "Light-medium cigar with rustic earth, wood, and traditional Cuban profile.",
    "aj-fernandez-new-world-dorado-robusto":
        "Full-bodied cigar with earth, spice, and natural tobacco richness.",
    "aj-fernandez-dias-de-gloria-brazil-corona":
        "Medium-full cigar with Brazilian sweetness, spice, and complexity.",
    "arturo-fuente-hemingway-short-story":
        "Smooth mild-medium cigar with cedar, spice, and slight sweetness.",
    "ashton-vsg-eclipse":
        "Full-bodied cigar with powerful spice, earth, and refined strength.",
    "oliva-serie-v-double-robusto":
        "Rich medium-full cigar with coffee, spice, and subtle citrus.",
    "rocky-patel-edge-b52-corojo":
        "Medium-full cigar with earthy, creamy, and consistent flavor.",
    "rocky-patel-vintage-1999-connecticut-robusto":
        "Mild cigar with creamy texture and smooth Connecticut profile.",
    "rocky-patel-vintage-1999-connecticut-junior":
        "Mild cigar with creamy texture and smooth Connecticut profile.",
    "e-p-carrillo-pledge-prequel":
        "Full-bodied cigar with spice, espresso, dark fruit, and complexity.",
    "joya-de-nicaragua-red-robusto":
        "Medium-bodied cigar with caramel, nuts, citrus, and soft spice.",
    "the-my-father-flor-de-las-antillas-toro":
        "Full-bodied cigar with coffee, leather, and peppery richness.",
    "my-father-le-bijou-1922-torpedo":
        "Bold cigar with deep earth, spice, and intense character.",
    "henry-clay-warhawk-robusto":
        "Mild-medium cigar with balanced earth, spice, and structure.",
    "esteban-carreras-mr-brownstone":
        "Medium-full cigar with cocoa, coffee, citrus, and pepper.",
    "esteban-carreras-cashmere-boolit":
        "Mild-medium cigar with cream, wood, and soft spice.",
    "jc-newman-brick-house-habano":
        "Medium cigar with cocoa, earth, cedar, and pepper.",
    "league-of-fat-bastards-serie-o":
        "Full-bodied cigar with cherry, cocoa, earth, and spice.",
    "league-of-fat-bastards-serie-l":
        "Medium-bodied cigar with cedar, cocoa, and balanced spice.",
    "cusano-honduras-robusto":
        "Medium-full cigar with spice, oak, and earthy balance.",
    "cusano-honduras-churchill":
        "Medium-full cigar with spice, oak, and earthy balance.",
    "cusano-honduras-toro":
        "Medium-full cigar with spice, oak, and earthy balance.",
    "villa-zamorano-robusto":
        "Medium cigar with smooth complexity and balanced intensity.",
    "nicatabaco-factory-blend-no-2-toro-deluxe":
        "Medium-bodied cigar with aromatic and balanced Nicaraguan profile.",
    "azan-white-campana":
        "Medium-bodied cigar with sweet notes and refined smoothness.",
}

# Apply descriptions
updated = 0
for c in cigars:
    if c["id"] in DESCRIPTIONS:
        c["notes"] = DESCRIPTIONS[c["id"]]
        updated += 1

with open(json_path, 'w') as f:
    json.dump(cigars, f, indent=2)

print(f"Updated {updated} / {len(cigars)} cigars with clean descriptions.")

# Report any missing
missing = [c["id"] for c in cigars if not c.get("notes")]
if missing:
    print(f"\nCigars still without descriptions ({len(missing)}):")
    for m in missing:
        print(f"  {m}")
