import json
import re

json_path = "/Users/pnwemd/Desktop/Websites/cnx-cigars/src/data/cigars.json"

with open(json_path, 'r') as f:
    cigars = json.load(f)

brands = [
    "Davidoff", "Montecristo", "Cohiba", "Romeo", "Partagas", "Hoyo", 
    "Trinidad", "Punch", "Bolivar", "H.Upmann", "Arturo Fuente", 
    "Rocky Patel", "Joya", "Quai", "Ashton", "AJ Fernandez", 
    "Henry Clay", "Cusano", "Villa Zamorano", "Plasencia", "My Father", 
    "E.P. Carrillo", "Esteban Carreras", "Brick House", "Alec Bradley", 
    "Quintero", "Jose L. Piedra", "Juan Lopez"
]

for c in cigars:
    name_lower = c["name"].lower()
    found_brand = "Other Brands"
    for brand in brands:
        if brand.lower() in name_lower:
            # Special case for Romeo
            if brand == "Romeo":
                found_brand = "Romeo y Julieta"
            elif brand == "Hoyo":
                found_brand = "Hoyo de Monterrey"
            elif brand == "Quai":
                found_brand = "Quai d'Orsay"
            else:
                found_brand = brand
            break
            
    # Fix H.Upmann spacing
    if "upmann" in name_lower and found_brand == "Other Brands":
        found_brand = "H.Upmann"
        
    c["category"] = found_brand

# Sort the cigars so that Davidoff is first, then Cuban brands, etc.
def brand_priority(b):
    order = ["Davidoff", "Cohiba", "Montecristo", "Partagas", "Romeo y Julieta", "Hoyo de Monterrey", "H.Upmann", "Trinidad"]
    if b in order:
        return order.index(b)
    return 100

cigars.sort(key=lambda x: (brand_priority(x["category"]), x["category"], x["name"]))

with open(json_path, 'w') as f:
    json.dump(cigars, f, indent=2)

print(f"Categorized {len(cigars)} cigars.")
