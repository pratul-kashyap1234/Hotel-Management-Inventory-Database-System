# --- DATA STORAGE (IN MEMORY) ---
categories = [
    {"id": 1, "name": "Housekeeping"},
    {"id": 2, "name": "Kitchen"},
    {"id": 3, "name": "Maintenance"}
]

products = []     # Will store dictionaries like: {'id': 1, 'name': 'Soap', ...}
transactions = [] # Will store transaction history

# --- FUNCTIONAL MODULES ---

def add_product():
    """
    Module 1: Inventory Item Management (Create)
    """
    print("\n--- ADD NEW PRODUCT ---")
    name = input("Enter Product Name (e.g., Soap): ")
    
    # Show categories
    print("\nSelect Category:")
    for cat in categories:
        print(f"{cat['id']}. {cat['name']}")
    
    cat_id = int(input("Enter Category ID: "))
    price = float(input("Enter Unit Price: "))
    reorder = int(input("Enter Reorder Level (default 5): ") or 5)

    # Generate a simple auto-increment ID
    new_id = len(products) + 1

    # Create the product dictionary
    new_product = {
        "id": new_id,
        "name": name,
        "category_id": cat_id,
        "price": price,
        "reorder_level": reorder,
        "stock": 0 # Default starting stock
    }

    products.append(new_product)
    print(f"Success! '{name}' added to inventory with ID {new_id}.")

def view_inventory():
    """
    Module 1: Read/View Data
    """
    print("\n--- CURRENT INVENTORY STATUS ---")
    print(f"{'ID':<5} {'Name':<20} {'Stock':<10} {'Price':<10} {'Status'}")
    print("-" * 60)

    for p in products:
        status = "LOW STOCK!" if p["stock"] <= p["reorder_level"] else "OK"
        print(f"{p['id']:<5} {p['name']:<20} {p['stock']:<10} ${p['price']:<9} {status}")

    if not products:
        print("(No items in inventory yet)")

def update_stock():
    """
    Module 2: Transaction Processing (Stock In/Out)
    """
    print("\n--- UPDATE STOCK ---")
    view_inventory() 
    
    if not products:
        return

    
    p_id = int(input("\nEnter Product ID to update: "))
    
    # Find the product in our list
    selected_product = None
    for p in products:
        if p["id"] == p_id:
            selected_product = p
            break
    
    if not selected_product:
        print("Error: Product ID not found.")
        return

    action = input("Type 'IN' to add stock (Purchase) or 'OUT' to issue stock: ").upper()
    qty = int(input("Enter Quantity: "))

    if action == 'IN':
        selected_product["stock"] += qty
    elif action == 'OUT':
        if selected_product["stock"] >= qty:
            selected_product["stock"] -= qty
        else:
            print(f"ERROR: Insufficient stock! You only have {selected_product['stock']}.")
            return
    else:
        print("Invalid action. Use IN or OUT.")
        return

    # Log the transaction
    transactions.append({
        "product_id": p_id,
        "type": action,
        "quantity": qty
    })
    
    print("Stock updated successfully.")

# --- MAIN CONTROLLER ---

def hotel_inventory_system():
    # No database setup needed anymore!
    
    while True:
        print("\n=== HOTEL INVENTORY SYSTEM (In-Memory) ===")
        print("1. Add New Item")
        print("2. View Inventory")
        print("3. Update Stock (In/Out)")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            update_stock()
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    hotel_inventory_system()