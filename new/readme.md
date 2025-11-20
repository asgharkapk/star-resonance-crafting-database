# **Recipe Dependency Visualizer**

A floating, interactive, visual tree that displays crafting dependencies, costs, shop interactions, and farming/buying rules for game items.
This tool reads data from your server’s database (via JSON API) and renders a draggable graph showing where each item comes from, how it is obtained, and what it is used for.

---

## **✨ Features**

### **🌳 Floating Visual Craft Tree**

* Every item is displayed as a draggable floating node.
* Items are connected with lines showing component → result relationships.
* Nodes can be rearranged freely to explore the crafting network.

### **📡 Live Data From Your Database**

* Recipes are fetched from your backend using an API endpoint.
* No file upload required; the tree updates automatically when backend data changes.

### **💰 Multi-Currency System**

Supports complex item economics including:

* Multiple currencies (gold, gems, crystals, etc.)
* Craft-energy cost per craft
* Shop-specific currencies (3 shops supported)
* Buy-only items
* Farmable items
* Craftable items with ingredient chains

### **🔗 Clear Dependency Links**

Each item shows:

* Ingredients (what it is crafted from)
* Usage (what crafts require this item)
* Multiple cost types (craft, shop, buy)
* Special flags like **farmable**, **shop-only**, etc.

### **🖱️ Drag & Drop Interface**

* Hold left mouse button to drag nodes around.
* Lines dynamically connect nodes regardless of placement.

---

## **📁 Project Structure**

```
project/
│
├── index.html        # Main visualizer webpage
├── README.md         # Documentation
└── /api/recipes      # Backend API endpoint returning item data
```

---

## **🧩 API Data Format**

The webpage expects an endpoint returning JSON like:

```json
{
  "items": {
    "Iron Bar": {
      "cost": { "gold": 12, "craft_energy": 3 },
      "from": ["Iron Ore", "Coal"],
      "shop": "Blacksmith",
      "buy_cost": { "gold": 30, "crystals": 0 },
      "farmable": false,
      "craft_energy": 1,
      "used_in": ["Iron Sword"]
    }
  }
}
```

### Required Fields per Item

| Field          | Type        | Description                          |
| -------------- | ----------- | ------------------------------------ |
| `cost`         | object      | Craft cost using any currencies      |
| `from`         | array       | Crafting ingredients                 |
| `shop`         | string/null | Shop name or null if not shop-bought |
| `buy_cost`     | object      | Cost to directly buy item            |
| `farmable`     | boolean     | Whether item can be farmed           |
| `craft_energy` | number      | Energy required per craft            |
| `used_in`      | array       | Items that use this item             |

---

## **🚀 Getting Started**

### 1. **Place the `index.html` in your webserver**

Any static server works:

* Apache / Nginx
* Node.js `http-server`
* GitHub Pages
* Vercel / Netlify

### 2. **Configure the API endpoint**

Inside `index.html` update:

```js
const API_URL = "/api/recipes";
```

Change to match your server:

```js
const API_URL = "https://yourdomain.com/api/recipes";
```

### 3. **Run the project**

Just open the webpage in a browser.

---

## **🛠️ Customization**

You can customize:

### Layout

* Automatic hierarchical layout
* Force-directed physics layout
* Canvas or WebGL rendering

### UI

* Node colors based on shop or currency
* Icons for items
* Item rarity borders
* Tooltips on hover

### Data Processing

* Full recursive crafting cost calculation
* Profit/loss detection
* Highlighting bottleneck items

Just tell me what you want added!

---

## **📌 Roadmap**

* [ ] Zoom & pan support
* [ ] Search bar (find item anywhere in the tree)
* [ ] Shop/craft/farm filters
* [ ] Total recursive crafting cost calculation
* [ ] Export visual tree as PNG

---

## **📄 License**

This project is free to use, modify, and integrate into any game tool or web application.


