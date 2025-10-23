import pandas as pd

# --- Load data ---
life_skills = pd.read_csv("../data/life_skills.csv")
recipes = pd.read_csv("../data/recipes.csv")
currencies = pd.read_csv("../data/currencies.csv")

# --- Helper functions ---

def parse_cost(cost_str):
    """Convert string like '20F' or '660L' into numeric value and currency code."""
    if pd.isna(cost_str):
        return 0, None
    cost_str = str(cost_str).strip()
    if cost_str[-1].isalpha():
        return float(cost_str[:-1]), cost_str[-1]
    return float(cost_str), None

def calculate_total_cost(recipe_row):
    """Calculate total cost in currencies and Focus for a recipe chain."""
    items = recipe_row['item'].split("→")
    total_costs = {}
    
    for i, item in enumerate(items):
        item = item.strip()
        row = life_skills[life_skills['item'].str.contains(item, case=False)]
        if not row.empty:
            for cost in row['mine_or_craft_cost']:
                value, currency = parse_cost(cost)
                if currency:
                    total_costs[currency] = total_costs.get(currency, 0) + value
    return total_costs

# --- Calculate cost for all recipes ---
recipes['total_costs'] = recipes.apply(calculate_total_cost, axis=1)

# --- Find lowest and highest cost recipes ---
def summarize_costs(df):
    min_costs = {}
    max_costs = {}
    for index, row in df.iterrows():
        for currency, cost in row['total_costs'].items():
            if currency not in min_costs or cost < min_costs[currency][0]:
                min_costs[currency] = (cost, row['item'])
            if currency not in max_costs or cost > max_costs[currency][0]:
                max_costs[currency] = (cost, row['item'])
    return min_costs, max_costs

min_costs, max_costs = summarize_costs(recipes)

print("✅ Lowest-cost recipes:")
for currency, (cost, item) in min_costs.items():
    print(f"{currency}: {item} → {cost}{currency}")

print("\n💰 Highest-cost recipes:")
for currency, (cost, item) in max_costs.items():
    print(f"{currency}: {item} → {cost}{currency}")
