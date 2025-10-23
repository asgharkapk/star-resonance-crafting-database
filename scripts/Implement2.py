# artisanry data
items_cost = {
    "Pine Timber": {"L": 174, "H": 58},
    "Charcoal": {"L": 660, "H": 220},
    "Burning Powder": {"L": 133, "H": 0},
}

recipes = [
    {"inputs": {"Pine Timber": 28}, "output": {"Charcoal": 10}, "F": 0},
    {"inputs": {"Charcoal": 1}, "output": {"Burning Powder": 15}, "F": 20},
    {"inputs": {"Pine Timber": 28}, "output": {"Charcoal": 10, "Burning Powder": 150}, "F": 200},
]

def calc_cost(recipe):
    total_L = 0
    total_H = 0
    total_F = recipe["F"]

    # sum cost of inputs
    for item, qty in recipe["inputs"].items():
        if item in items_cost:
            total_L += items_cost[item]["L"] * qty
            total_H += items_cost[item]["H"] * qty
        else:
            total_L += 0
            total_H += 0

    # calculate cost per output item
    costs = []
    for out_item, out_qty in recipe["output"].items():
        costs.append({
            "output": out_item,
            "quantity": out_qty,
            "L_per_item": total_L / out_qty if out_qty else 0,
            "H_per_item": total_H / out_qty if out_qty else 0,
            "F_per_item": total_F / out_qty if out_qty else 0
        })
    return costs

# calculate and display all options
all_options = []
for r in recipes:
    all_options.extend(calc_cost(r))

# print results
for option in all_options:
    print(f"Output: {option['output']} x{option['quantity']} -> "
          f"L: {option['L_per_item']:.2f}, H: {option['H_per_item']:.2f}, F: {option['F_per_item']:.2f}")
