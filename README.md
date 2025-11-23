**Hotel Management Inventory Database System**



**Overview:**



**This project is a comprehensive Inventory Management System designed specifically for the hospitality industry. It replaces manual logbooks with a robust SQL-based database to track assets, manage suppliers, and monitor stock levels in real-time. This solution addresses the issues of revenue leakage and operational inefficiencies caused by traditional paper-based tracking.**



**Features:**



* **Product Management: Create, Read, Update, and Delete (CRUD) inventory items with categorization.**
* **Stock Tracking: Real-time updates of stock levels via "Check-in" (Purchase) and "Check-out" (Issue) transactions.**
* **Reporting: Automatic detection of items below reorder levels (Low Stock Alerts).**
* **Department Allocation: Track which department (Kitchen, Laundry, etc.) is consuming the most resources.**
* **Role-Based Access: Security separation between Admin (full access) and General Staff (transaction access only).**
* 
* 

**Technologies Used:**



* **Language: Python (for application logic)**
* **Database: SQL (MySQL / SQLite)**
* **Tools: VS Code, Git, Mermaid.js (for documentation)**



**Steps to Install \& Run:**



**Clone the repository:**

**git clone: https://github.com/pratul-kashyap1234/Hotel-Management-Inventory-Database-System**



**Install dependencies:(Ensure you have Python installed)**

**pip install -r requirements.txt**



**Initialize the database: Run the SQL script to create the tables and relationships.**

**# If using SQLite via a setup script**

**python setup\_database.py**

**# OR import 'database\_schema.sql' into your MySQL Workbench**



**Run the application:**

**python main.py**



**Instructions for Testing:**



**Test Add Item:**

* **Navigate to the "Add Item" menu.**
* **Input a new product (e.g., "Liquid Soap 5L") with a quantity of 10.**
* **Verify it appears in the "View All Inventory" list.**



**Test Transaction (Stock Out):**

* **Select "Issue Stock".**
* **Choose the item "Liquid Soap 5L" and issue 2 units to "Housekeeping".**
* **Check the "View All Inventory" list again; the quantity should now be 8.**



**Test Low Stock Alert:**

* **Manually issue enough stock so the remaining quantity falls below the reorder level (e.g., below 5).**
* **Navigate to "Reports" -> "Low Stock"; the item should appear there.**
