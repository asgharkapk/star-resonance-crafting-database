# star-resonance-crafting-database
Community-driven dataset for Star Resonance life skills, crafting materials, and currency costs (Focus, Luno, Homestead). 
Includes mining, crafting, and vendor prices from CN and EN sources. Star Resonance life skill &amp; crafting data: materials, Focus cost, and currency prices.

# https://asgharkapk.github.io/star-resonance-crafting-database/list.html

# 🌌 Star Resonance — Life Skill & Crafting Data

Community-driven dataset for **Star Resonance** covering life skills, materials, stamina (Focus) usage, and currency costs.  
Includes data from in-game observations and Chinese community sources.

---

# 🌟 Star Resonance Crafting Guide

A **community-driven crafting database and cost optimizer** for **Star Resonance**, designed to help players explore material recipes, calculate costs, and find the most efficient crafting paths.

This project combines a **static HTML interface** for browsing crafting data with **Python automation scripts** that dynamically generate indexes and optimize crafting costs using CSV data.

---

## 📘 Features

### 🧭 Interactive Web Guide

* Displays all crafting, shop, and material data from CSV files automatically.
* Click on any item name to open a **modal popup** showing:

  * What it’s **made from** 🔨
  * Where it’s **used** 🧩
  * **Shop prices** 🏪
  * **Best purchase option** 💡

### ⚙️ Automated Data Processing

* Automatically detects and loads all CSV files in the `/data` folder.
* Builds `index.json` dynamically with GitHub Actions.
* Parses recipes, calculates costs, and outputs best/worst value comparisons.

### 🧠 Smart Cost Optimizer

* Reads and analyzes all crafting recipes.
* Identifies **lowest** and **highest-cost** items across all currencies.
* Outputs results to:

  * Console log (for easy CI monitoring)
  * `scripts/best_worst_recipes.csv` for records

---

## 🗂️ Project Structure

```
📦 Star-Resonance-Crafting-Guide
├── index.html                 # Main web interface
├── data/                      # All CSV data lives here
│   ├── artisanry.cvs
│   ├── shop_prices.cvs
│   ├── currencies.cvs
│   └── index.json             # Auto-generated file list
├── scripts/
│   ├── craft_optimizer.py     # Analyzes crafting costs
│   ├── generate_index_json.py # Generates data/index.json
│   └── best_worst_recipes.csv # Summary file (generated)
├── .github/workflows/
│   └── crafting.yml           # GitHub Actions workflow
└── README.md
```

---

## 🧩 Example CSV Format

### **artisanry.cvs**

```csv
action,cin,from,cout,to,cost
craft,28x,Pine Timber,10x,Charcoal,0F
craft,2x,Resin,15x,GemWax,20F
buy,,Exchange,1x,Charcoal,600L
```

### **currencies.cvs**

```csv
action,from,to,cost
define,L,Luno Coin,Used to buy items from Exchange stores
define,F,Focus,Used as stamina to craft
define,H,Homestead Coin,Used in Homestead store
```

---

## 🧰 Python Scripts

### `generate_index_json.py`

Scans `/data` for `.csv` or `.cvs` files and writes:

```json
{
  "files": ["artisanry.cvs", "currencies.cvs", "shop_prices.cvs"]
}
```

### `craft_optimizer.py`

* Loads all CSVs dynamically (no manual imports needed).
* Detects delimiters automatically (`|` or `,`).
* Calculates per-item costs and identifies the most/least expensive recipes.
* Saves summary to `best_worst_recipes.csv`.

---

## 🧪 GitHub Actions Workflow

**Workflow file:** `.github/workflows/crafting.yml`

### Tasks:

1. 🧱 Setup Python environment
2. 📄 Generate `index.json` from CSVs
3. ⚙️ Run crafting optimizer
4. 💾 Upload and commit results

Artifacts include:

* `output/optimizer_output.txt`
* `scripts/best_worst_recipes.csv`
* Updated `data/index.json`

---

## 🖥️ Local Development

### Requirements

* **Python 3.11+**
* **pandas**

### Setup

```bash
pip install pandas
python scripts/generate_index_json.py
python scripts/craft_optimizer.py
```

Then, open `index.html` in a browser to view the live guide.

---

## 🌐 Deployment

You can host this project on:

* **GitHub Pages**
* **Netlify**
* **Vercel**

Simply ensure that:

* The `/data` folder and `index.json` are accessible.
* CSV files are committed to the repo.

---

## 💾 How to Write New Data

Adding new data is simple — just follow these steps:

### 🪶 1. Create a New CSV

Place your file in the `/data` folder.
You can name it however you want, for example:

```
data/materials.cvs
```

Supported formats: `.csv` or `.cvs`
Each file should have a **header row** and **comma-separated** values.

Example:

```csv
action,from,to,cost
craft,Iron Ore,Iron Ingot,15F
buy,Exchange,Iron Ore,250L
```

### 🧾 2. Structure Tips

* `action` → what type of operation (craft, buy, refine, etc.)
* `from` → input material(s)
* `to` → output item
* `cost` → numeric value + currency symbol (e.g., `20F`, `300L`, `120H`)

Additional optional columns like `cin` and `cout` show input/output quantities (e.g., `2x`, `15x`).

### 🔁 3. Automatic Index Update

When you **commit or push**, GitHub Actions automatically:

* Scans the `/data` folder
* Updates `index.json`
* Regenerates optimized crafting summaries

✅ **No manual editing required!** The new CSV appears automatically on the website.

---

## 🌍 Live Website

### 🔗 Visit:

👉 **[Star Resonance Crafting Database](https://asgharkapk.github.io/star-resonance-crafting-database/)**

### 💡 What You’ll See

* Tables for **all CSV files** in the `data` directory
* Searchable, interactive lists of materials and recipes
* Clickable items that open a modal window showing:

  * Crafting sources (`Made From`)
  * Usage recipes (`Used In`)
  * Shop pricing (`🏪 Shop Prices`)
  * Smart recommendation for cheapest option (`💡 Best Option`)

The page updates automatically whenever the repository data changes — thanks to the GitHub Actions workflow.

---

## 🧠 How Data Reading Works (HTML Explained)

The `index.html` file dynamically loads all data from the `/data` folder using JavaScript:

### 🔍 Step-by-Step Process

1. **Load index.json**

   ```js
   const resp = await fetch("./data/index.json");
   const { files } = await resp.json();
   ```

   This tells the site which `.csv` files exist.

2. **Fetch Each CSV File**

   ```js
   const rows = await loadCSV(`${DATA_DIR}/${file}`);
   ```

   Each CSV is read line-by-line, even if it contains commas inside quotes.

3. **Parse CSV**

   * The script detects headers automatically.
   * If a CSV contains **duplicate column names**, it adds suffixes like `_2`, `_3`.

4. **Generate Tables**

   ```js
   createTableSection(file, Object.keys(rows[0]), rows);
   ```

   Each CSV becomes a full HTML table with alternating row colors and styled headers.

5. **Clickable Items**

   * Any cell containing keywords like `"item"`, `"to"`, or `"from"` is turned into a clickable link:

     ```js
     <span class="item-link" data-item="Charcoal">Charcoal</span>
     ```
   * Clicking triggers the modal window to appear.

6. **Modal Item Details**

   * Searches through **all loaded CSVs** to find:

     * Where the item is **crafted**
     * What other items **use** it
     * Where it’s **sold**
   * Builds a full HTML summary inside the modal.

7. **Automatic Refresh**
   Since `index.json` is rebuilt automatically by the workflow, **new CSV files appear instantly** without editing the HTML code.

---

## 🙌 Credits

**Star Resonance Crafting Guide**
Community-maintained fan project inspired by the crafting system of *Star Resonance*.
All data sourced and compiled by players.

**Developed by:** community contributors
**Maintained with love 💙 by:** Star Resonance fans

---

## 📄 License

This project is distributed under the **MIT License**.
Use, modify, and share freely — attribution appreciated.

