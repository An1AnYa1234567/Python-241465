# Write a program to demonstrate In-Memory Inventory Tracker with Dictionary Merging.
# Inventory Management System
# Inventory of different stores
store1 = {
    "Laptop": 10,
    "Mobile": 20,
    "Keyboard": 15
}

store2 = {
    "Laptop": 5,
    "Mobile": 12,
    "Mouse": 25
}

store3 = {
    "Keyboard": 10,
    "Mouse": 15,
    "Monitor": 8
}

# Display individual store inventory
print("Store 1 Inventory:", store1)
print("Store 2 Inventory:", store2)
print("Store 3 Inventory:", store3)

# Check whether a product exists
product = "Laptop"

print("\nChecking Product:", product)

if product in store1:
    print("Available in Store 1:", store1.get(product))
else:
    print("Product not available in Store 1")

# Safely access a missing product
print("Printer Stock:", store1.get("Printer", 0))

# Merge all product names using dictionary comprehension
all_products = {
    item: 0
    for store in [store1, store2, store3]
    for item in store
}

# Calculate total stock across stores
for store in [store1, store2, store3]:
    for item, quantity in store.items():
        all_products[item] += quantity

# Display combined inventory
print("\nCombined Inventory:")
print(all_products)

# Update inventory with new stock
new_stock = {"Laptop": 5, "Printer": 10}
all_products.update({
    item: all_products.get(item, 0) + quantity
    for item, quantity in new_stock.items()
})

print("\nInventory After Stock Update:")
print(all_products)