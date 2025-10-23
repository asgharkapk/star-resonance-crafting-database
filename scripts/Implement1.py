import pandas as pd

# Load item costs (L/H)
items_cost = pd.DataFrame({
    "item": ["Pine Timber", "Charcoal", "Burning Powder"],
    "L": [174, 660, 133],
    "H": [58, 220, 0]
})

# Recipes (crafting)
recipes = [
    {"inputs": {"Pine Timber": 28}, "output": {"Charcoal": 10}, "F": 0},
    {"inputs": {"Charcoal": 1}, "output": {"Burning Powder": 15}, "F": 20},
    {"inputs": {"Pine Timber": 28}, "output": {"Charcoal": 10, "Burning Powder": 150}, "F": 200},
]

# Function to calculate cheapest route
def calc_cost(recipe):
    total_L = 0
    total_H = 0
    total_F = recipe["F"]
    
    for item, qty in recipe["inputs"].items():
        row = items_cost[items_cost["item"] == item].iloc[0]
        total_L += row["L"] * qty
        total_H += row["H"] * qty
    
    # cost per output
    output_item, output_qty = list(recipe["output"].items())[0]
    return {
        "output": output_item,
        "quantity": output_qty,
        "L_per_item": total_L / output_qty,
        "H_per_item": total_H / output_qty,
        "F_per_item": total_F / output_qty
    }

for r in recipes:
    cost = calc_cost(r)
    print(cost)
