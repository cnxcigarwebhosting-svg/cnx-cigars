import json

data = [
  {
    "id": "partagas-serie-d-no4",
    "name": "Partagas Serie D No.4",
    "category": "Full-Bodied",
    "price": 2270,
    "strength": "Full-bodied",
    "format": "Robusto",
    "smokingTime": "45-60 mins",
    "notes": "The most best selling Cuban robusto cigar in the world! Classic Robusto with unique flavor profile.",
    "featured": True
  },
  {
    "id": "hoyo-epicure-no2",
    "name": "Hoyo de Monterrey - Epicure No. 2",
    "category": "Beginner Friendly",
    "price": 2195,
    "strength": "Mild to Medium",
    "format": "Robusto",
    "smokingTime": "45 mins",
    "notes": "Using tobacco from the premium Vuelta Abajo region. A long-established favourite and popular 'turn to' cigar.",
    "featured": False
  },
  {
    "id": "hoyo-epicure-especial",
    "name": "Hoyo de Monterrey - Epicure Especial",
    "category": "Cuban Classics",
    "price": 2260,
    "strength": "Mild to Medium",
    "format": "Gordito",
    "smokingTime": "45-60 mins",
    "notes": "Rich, creamy, and complex. Prominent notes of cedar, leather, coffee, cocoa powder, and subtle spices with a sweet woody aftertaste.",
    "featured": False
  },
  {
    "id": "quai-dorsay-50",
    "name": "Quai d'Orsay 50",
    "category": "Beginner Friendly",
    "price": 1550,
    "strength": "Mild to Medium",
    "format": "Petite Robusto",
    "smokingTime": "45-60 mins",
    "notes": "Smooth, creamy, and elegant. Specifically crafted for the French market. Subtle notes of cedar, vanilla, and hazelnut.",
    "featured": False
  },
  {
    "id": "ryj-no2-tubo",
    "name": "Romeo y Julieta - No.2 (Tubo)",
    "category": "Beginner Friendly",
    "price": 1080,
    "strength": "Medium",
    "format": "Petit Corona",
    "smokingTime": "20 mins",
    "notes": "Delivers notes of cedar, leather, and earth, with a subtle sweetness on the finish. A consistent burn and draw.",
    "featured": False
  },
  {
    "id": "ryj-short-churchill",
    "name": "Romeo Y Julieta - Short Churchill",
    "category": "Cuban Classics",
    "price": 1950,
    "strength": "Medium",
    "format": "Robusto",
    "smokingTime": "45 mins",
    "notes": "A popular medium strength cigar from a pre-Revolution brand officially registered in 1873.",
    "featured": False
  },
  {
    "id": "ryj-churchill",
    "name": "Romeo Y Julieta - Churchill",
    "category": "Cuban Classics",
    "price": 2730,
    "strength": "Medium",
    "format": "Churchill",
    "smokingTime": "60-75 mins",
    "notes": "An exclusive blend of tobaccos from the Vuelta Abajo region. A totally handmade cigar of larger size.",
    "featured": False
  },
  {
    "id": "bolivar-royal-corona",
    "name": "Bolivar - Royal Corona",
    "category": "Full-Bodied",
    "price": 1885,
    "strength": "Medium-Full",
    "format": "Robusto",
    "smokingTime": "45 mins",
    "notes": "Highly-regarded Cuban cigar. Complex and full-bodied with notes of bold pepper spices, woody and herbal flavors, and a luscious smoke.",
    "featured": False
  },
  {
    "id": "bolivar-belicoso-fino",
    "name": "Bolivar - Belicoso Fino",
    "category": "Full-Bodied",
    "price": 2260,
    "strength": "Full Bodied",
    "format": "Belicoso",
    "smokingTime": "60 mins",
    "notes": "One of the strongest cigars in the Bolivar range. Notes of spice, wood, leather, chocolate, salt, and hints of fruit.",
    "featured": False
  },
  {
    "id": "juan-lopez-sel-no2",
    "name": "Juan Lopez - Seleccion No.2",
    "category": "Full-Bodied",
    "price": 1675,
    "strength": "Medium-Full",
    "format": "Robusto",
    "smokingTime": "45 mins",
    "notes": "Medium to full strength with a complex flavor profile featuring notes of wood, herbs, and earthiness.",
    "featured": False
  },
  {
    "id": "montecristo-edmundo",
    "name": "Montecristo - Edmundo",
    "category": "Cuban Classics",
    "price": 2360,
    "strength": "Medium-Full",
    "format": "Robusto",
    "smokingTime": "45-60 mins",
    "notes": "Named after Alexandre Dumas' hero. Big and rewarding with classic peppery and punchy notes.",
    "featured": False
  },
  {
    "id": "montecristo-no2",
    "name": "Montecristo - No.2",
    "category": "Cuban Classics",
    "price": 2450,
    "strength": "Medium-Full",
    "format": "Pyramides",
    "smokingTime": "60 mins",
    "notes": "A highly acclaimed and iconic cigar. Renowned for its rich flavor profile and exceptional craftsmanship.",
    "featured": False
  },
  {
    "id": "montecristo-no4",
    "name": "Montecristo No.4",
    "category": "Beginner Friendly",
    "price": 1320,
    "strength": "Medium-Full",
    "format": "Petit Corona",
    "smokingTime": "30 mins",
    "notes": "Combines richness, immense taste, and value into a great all-around cigar smoking experience.",
    "featured": False
  },
  # New items
  {
    "id": "quintero-favoritos",
    "name": "Quintero - Favoritos",
    "category": "Cuban Classics",
    "price": 670,
    "strength": "Medium-bodied",
    "format": "Petit Robusto",
    "smokingTime": "30-45 mins",
    "notes": "From the south of Cuba comes the Quintero Favoritos. Intense and complex.",
    "featured": False
  },
  {
    "id": "jose-l-piedra-cazadores",
    "name": "Jose L. Piedra - Cazadores",
    "category": "Beginner Friendly",
    "price": 615,
    "strength": "Light-Medium",
    "format": "Cazadores",
    "smokingTime": "45 mins",
    "notes": "Tobacco grown in the Remedios region. Very popular traditional Cuban shape.",
    "featured": False
  },
  {
    "id": "punch-short-de-punch",
    "name": "Punch - Short de punch",
    "category": "Cuban Classics",
    "price": 1985,
    "strength": "Medium-bodied",
    "format": "Petit Robusto",
    "smokingTime": "30 mins",
    "notes": "Well-balanced flavor profile and smooth, consistent burn with notes of cedar, spice, and earth.",
    "featured": False
  },
  {
    "id": "punch-punch-tubo",
    "name": "Punch - Punch (Tubo)",
    "category": "Cuban Classics",
    "price": 2150,
    "strength": "Medium-bodied",
    "format": "Coronas Gordas",
    "smokingTime": "60-90 mins",
    "notes": "Delivering a medium-bodied, creamy, and complex smoking experience with notes of honey and baking spices.",
    "featured": False
  },
  {
    "id": "punch-super-selection-no1",
    "name": "Punch Super Selection No.1 Edición Regional",
    "category": "Cuban Classics",
    "price": 2270,
    "strength": "Medium-bodied",
    "format": "Coronas Grandes",
    "smokingTime": "60 mins",
    "notes": "Limited-edition regional release. Medium-strength with flavors of wood, cedar, coffee, and spices.",
    "featured": False
  },
  {
    "id": "montecristo-open-regata",
    "name": "Montecristo OPEN - Regata",
    "category": "Cuban Classics",
    "price": 2100,
    "strength": "Medium-Full",
    "format": "5 3/4\"",
    "smokingTime": "40 mins",
    "notes": "Premium, hand rolled. Lighter, less aggressive character whilst retaining classic flavor.",
    "featured": False
  },
  {
    "id": "h-upmann-mag-46",
    "name": "H.Upmann - Mag 46",
    "category": "Cuban Classics",
    "price": 2110,
    "strength": "Medium",
    "format": "Coronas Gordas",
    "smokingTime": "60-95 mins",
    "notes": "Known for a medium-bodied, creamy, and refined smoke with cedar and toasted nuts.",
    "featured": False
  },
  {
    "id": "h-upmann-magnum-54",
    "name": "H.Upmann - Magnum 54",
    "category": "Cuban Classics",
    "price": 2200,
    "strength": "Light to Medium",
    "format": "Magnum 54",
    "smokingTime": "60 mins",
    "notes": "Medium bodied despite its young age, develops lots of creaminess, chocolate and hay.",
    "featured": False
  },
  {
    "id": "partagas-serie-pyramides-no2",
    "name": "Partagas - Serie Pyramides No.2",
    "category": "Full-Bodied",
    "price": 2420,
    "strength": "Full-bodied",
    "format": "Piramides",
    "smokingTime": "60 mins",
    "notes": "Popular Cuban cigar known for full-bodied flavor, notes of cedar, cocoa, pepper, and sweet spice.",
    "featured": False
  },
  {
    "id": "trinidad-vigia",
    "name": "Trinidad - Vigia",
    "category": "Cuban Classics",
    "price": 3100,
    "strength": "Medium-Full",
    "format": "Petit Robusto",
    "smokingTime": "45 mins",
    "notes": "Started as a commercially unavailable cigar for diplomats. Introduced in 2014.",
    "featured": False
  },
  {
    "id": "trinidad-media-luna",
    "name": "Trinidad - Media Luna",
    "category": "Cuban Classics",
    "price": 2730,
    "strength": "Medium-Full",
    "format": "Petit Robusto",
    "smokingTime": "40 mins",
    "notes": "Notes of cedar, honey, leather, and nuttiness. Known for its signature pigtail cap.",
    "featured": False
  },
  {
    "id": "h-upmann-half-corona",
    "name": "H.Upmann - Half Corona",
    "category": "Beginner Friendly",
    "price": 910,
    "strength": "Light-medium",
    "format": "Half Corona",
    "smokingTime": "30 mins",
    "notes": "Smooth, subtle, mild to medium smoke. Great for beginners.",
    "featured": False
  },
  {
    "id": "partagas-serie-d-no5",
    "name": "Partagas - Serie D No.5",
    "category": "Full-Bodied",
    "price": 1660,
    "strength": "Full-bodied",
    "format": "Petite Robusto",
    "smokingTime": "40 mins",
    "notes": "Features a rich, earthy, and spicy profile. Notes include cedar, oak, roasted nuts.",
    "featured": False
  }
]

with open("/Users/pnwemd/Desktop/Websites/cnx-cigars/src/data/cigars.json", "w") as f:
    json.dump(data, f, indent=2)
