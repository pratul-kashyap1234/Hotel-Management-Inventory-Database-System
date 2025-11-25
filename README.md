# 🏨 Hotel Management Inventory System (HMIS)

## 📖 1. Project Overview

The **Hotel Management Inventory System (HMIS)** is a specialized, lightweight software solution designed to digitize asset tracking for small to mid-sized hotels. In the hospitality industry, managing the flow of consumables—such as housekeeping toiletries, kitchen ingredients, and maintenance tools—is critical for operational efficiency.

This project serves as a **standalone console application** that replaces traditional, error-prone paper logbooks. It provides hotel staff with a centralized platform to:
1.  📋 Register products.
2.  📊 Monitor stock levels in real-time.
3.  🚚 Record the movement of goods (purchases and issuances) with precision.

> **🚀 Key Differentiator:** By utilizing **In-Memory Data Storage (Python Lists and Dictionaries)**, the system offers lightning-fast performance and zero-configuration setup, making it ideal for immediate deployment where complex SQL servers are not feasible.

---

## 🚩 2. Problem Statement

Hotels manage thousands of individual items daily. Without a proper digital system, they face several operational challenges:

| Challenge | Description |
| :--- | :--- |
| **👀 Operational Blindness** | Managers cannot verify stock levels without physically walking to the storage room. |
| **💸 Revenue Leakage** | Unrecorded consumption or theft often goes unnoticed until end-of-month audits. |
| **✍️ Human Error** | Manual calculation (e.g., `Previous + Purchase - Issue`) is prone to mathematical mistakes. |
| **📉 Stockouts** | Critical items run out unexpectedly due to lack of automated "Low Stock" alerts. |

**The Solution:** HMIS enforces a strict digital workflow for every item that enters or leaves storage.

---

## ⚙️ 3. Functional Requirements

The system is divided into three core modules, each handling a specific aspect of inventory control.

### 📦 Module 1: Item Management (CRUD)
Allows the administrator to define trackable items.
* **Product Registration:** Add items with specific attributes:
    * *Name* (e.g., "Shampoo 50ml")
    * *Category* (Housekeeping, Kitchen)
    * *Unit Price* (Financial tracking)
    * *Reorder Level* (Alert threshold)
* **Auto-Incrementing IDs:** Automatically assigns unique IDs to prevent duplicates.

### 📊 Module 2: Inventory Tracking
Provides visibility into the current state of assets.
* **Real-Time Dashboard:** Tabular view of all registered products.
* **Smart Status Indicators:**
    * 🔴 If `Stock <= Reorder Level`: Displays **"LOW STOCK!"**
    * 🟢 If `Stock > Reorder Level`: Displays **"OK"**
* **Financial Overview:** Displays unit prices for stock valuation.

### 🔄 Module 3: Stock Transactions
Handles the core logic of inventory flow.
* **📥 Stock In (Procurement):** Adds quantity when suppliers deliver goods.
* **📤 Stock Out (Issuance):** Deducts quantity when departments request items.
* **🛡️ Validation Logic:** Prevents **Negative Stock**. You cannot issue 10 items if you only have 5.

---

## ⚡ 4. Non-Functional Requirements

* **Performance:** Uses In-Memory storage (RAM), ensuring read/write operations occur in $O(1)$ or $O(n)$ time complexity.
* **Usability:** The CLI utilizes clear prompts and descriptive error messages (e.g., "Insufficient stock"), making it accessible to non-technical staff.
* **Reliability:** Strict validation prevents logical errors (e.g., negative counts, duplicate IDs).
* **Portability:** Built using only the **Python Standard Library**. No external databases required. Runs on Windows, macOS, and Linux.

---

## 🏗️ 5. Technical Architecture

This project is built using **Python 3** and follows a procedural programming paradigm.

### Data Structures
Instead of a heavy SQL database, HMIS uses efficient Python native data structures in **RAM**.

#### 1. The Product Repository (List of Dictionaries)
Mimics a NoSQL document structure:
```python
products = [
    {
        "id": 1, 
        "name": "Bath Towel", 
        "category_id": 1, 
        "price": 15.50, 
        "reorder_level": 10, 
        "stock": 100
    },
    {
        "id": 2, 
        "name": "Tomato Ketchup", 
        "category_id": 2, 
        "price": 2.50, 
        "reorder_level": 20, 
        "stock": 45
    }
]
2. The Category ReferencePythoncategories = [
    {"id": 1, "name": "Housekeeping"},
    {"id": 2, "name": "Kitchen"},
    {"id": 3, "name": "Maintenance"}
]
```

Algorithmic LogicSearch: Updates use a Linear Search ($O(n)$) to locate products by ID.Persistence: Variables are global. Note: RAM is volatile; data clears when the script terminates.
💻 6. Installation & SetupPrerequisitesOS: 
Windows, macOS, or Linux.
Language: Python 3.6+.
Steps:
Clone the Repository:git clone [https://github.com/pratul-kashyap1234/Hotel-Management-Inventory-Database-System](https://github.com/pratul-kashyap1234/Hotel-Management-Inventory-Database-System)
Navigate to Directory:cd hotel-inventory-system
Verify Python:python --version
# Output: Python 3.x.x

🎮 7. Usage GuideStarting the AppRun the main script:Bashpython main.py
Main Menu:
=== HOTEL INVENTORY SYSTEM (In-Memory) ===
1. Add New Item
2. View Inventory
3. Update Stock (In/Out)
4. Exit
Select an option (1-4):
workflows
Add Product: Enter Name, Category ID, Price, and Reorder Level.
View Inventory: Check the table for "LOW STOCK!" warnings.
Update Stock: Select Product ID -> Type IN or OUT -> Enter Quantity.

🧪 9. Testing InstructionsManual testing script to verify system integrity:
[ ] Test Case 1: New Item Flow
      Add "Test Item" (Stock: 0, Reorder: 5).
      Verify: Status is "LOW STOCK!".
[ ] Test Case 2: Stock In
      Update "Test Item" -> IN -> Qty 20.
      Verify: Stock is 20, Status "OK".
[ ] Test Case 3: Stock Out
     Update "Test Item" -> OUT -> Qty 5.
     Verify: Stock is 15.
[ ] Test Case 4: Safety Check
     Update "Test Item" -> OUT -> Qty 100.
     Verify: System error "Insufficient stock!", Stock remains 15.
     
⚠️ 10. Limitations & Known Issues
       Data Volatility: Data is lost upon application closure (In-Memory limitation).
       Input Sensitivity: Inputs must be exact (e.g., "10" not "Ten") or the program will crash (no try/except blocks).
       Concurrency: Single-user only; not networked.🔮 

11. Future Enhancements (v2.0)💾
    File Persistence: Save to .json or .csv to retain data.
    🔍 Search: Find items by Name (e.g., "Soap").
    📜 Audit Log: Track history of all transactions.
    🖥️ GUI: Graphical interface using Tkinter.
