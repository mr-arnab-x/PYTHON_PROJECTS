from utils import Restaurant

def main():
    restaurant = Restaurant()

    while True:
        print("\nRestaurant Management System")
        print("1. Add Order")
        print("2. View Orders")
        print("3. Manage Tables")
        print("4. Check Inventory")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            dish = input("Enter dish name: ")
            quantity = int(input("Enter quantity: "))
            restaurant.add_order(dish, quantity)
            print("Order added successfully.")
        elif choice == '2':
            orders = restaurant.view_orders()
            print("\nCurrent Orders:")
            for order in orders:
                print(order)
        elif choice == '3':
            table_number = int(input("Enter table number: "))
            status = input("Enter status (Available/Occupied): ")
            restaurant.manage_table(table_number, status)
            print("Table status updated.")
        elif choice == '4':
            inventory = restaurant.check_inventory()
            print("\nInventory Status:")
            for item in inventory:
                print(f"{item}: {inventory[item]}")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
