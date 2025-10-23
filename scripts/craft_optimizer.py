import os
import pandas as pd

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# --- Markdown-table CSV loader ---
def load_table(path):
    if not os.path.exists(path):
        print(f"❌ Missing file: {path}")
        return pd.DataFrame()
    df = pd.read_csv(path, sep="|", engine="python").dropna(axis=1, how="all")
    df.columns = [c.strip() for c in df.columns]
    df = df.applymap(lambda x: str(x).strip() if isinstance(x, str) else x)
    print(f"📂 Loaded {os.path.basename(path)} → columns: {df.columns.tolist()}")
    return df

# --- Load data ---
life_skills = load_table(os.path.join(DATA_DIR, "life_skills.csv"))
recipes = load_table(os.path.join(DATA_DIR, "recipes.csv"))
currencies = load_table(os.path.join(DATA_DIR, "currencies.csv"))

# --- Helper functions ---
def parse_cost(cost_str, currency_str=None):
    """Convert cost + currency into numeric + code."""
    if pd.isna(cost_str):
        return 0, None
    value = float(cost_str)
    currency = str(currency_str).strip() if pd.notna(currency_str) else None
    return value, currency

def calculate_total_cost(recipe_row):
    """Compute cost from a single recipe line."""
    total_costs = {}
    value, currency = parse_cost(recipe_row.get("cost"), recipe_row.get("currency"))
    if currency:
        total_costs[currency] = total_costs.get(currency, 0) + value
    return total_costs

# --- Apply calculations ---
if "item" not in recipes.columns:
    raise KeyError("❌ The recipes.csv file must contain an 'item' column!")

recipes["total_costs"] = recipes.apply(calculate_total_cost, axis=1)

# --- Summarize costs ---
def summarize_costs(df):
    min_costs, max_costs = {}, {}
    for _, row in df.iterrows():
        for currency, cost in row["total_costs"].items():
            if currency not in min_costs or cost < min_costs[currency][0]:
                min_costs[currency] = (cost, row["item"])
            if currency not in max_costs or cost > max_costs[currency][0]:
                max_costs[currency] = (cost, row["item"])
    return min_costs, max_costs

min_costs, max_costs = summarize_costs(recipes)

# --- Output results ---
print("\n✅ Lowest-cost recipes:")
for currency, (cost, item) in min_costs.items():
    print(f"{currency}: {item} → {cost}{currency}")

print("\n💰 Highest-cost recipes:")
for currency, (cost, item) in max_costs.items():
    print(f"{currency}: {item} → {cost}{currency}")

# --- Save summary CSV ---
summary = []
for currency, (cost, item) in min_costs.items():
    summary.append([currency, "Lowest", item, cost])
for currency, (cost, item) in max_costs.items():
    summary.append([currency, "Highest", item, cost])
out_path = os.path.join(BASE_DIR, "scripts", "best_worst_recipes.csv")
pd.DataFrame(summary, columns=["Currency", "Type", "Item", "Cost"]).to_csv(out_path, index=False)
print(f"\n📄 Saved summary → {out_path}")
