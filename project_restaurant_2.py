def restaurant():

    # --------------Greet--------------
    print("---------------Welcome To The Mr. MOMO Restaurant----------------")

    # Menu dictionary with categories and items
    menu = {
        "Pizza": {
            "Paneer Pizza": 100,
            "Chicken Pizza": 150,
        },
        "Coffee": {
            "Cold Coffee": 140,
            "Hot Coffee": 120,
        },
        "Chai": {
            "Masala Chai": 25,
            "Tandoori Chai": 30,
            "Normal Chai": 10,
        },
        "Burger": {
            "Veg Burger": 70,
            "Chicken Burger": 80,
        },
        "Momo": {
            "Paneer Momo": 80,
            "Chicken Momo": 90,
            "Steam Momo": 70,
        },
        "Pastry": {
            "Chocolate Pastry": 70,
            "Vanilla Pastry": 65,
        },
    }

    # Display the categories
    print(" Please select a category from the following: ")
    for category in menu.keys():
        print(f" - {category}")

    # Initialize the total order cost
    order_total = 0

    while True:
        # Ask for a category to order from
        selected_category = input(" Enter the category you want to order from ---> ")

        if selected_category in menu:
            # Display the items in the selected category
            print(f" You selected {selected_category}. Here are the items available:")
            for item, price in menu[selected_category].items():
                print(f" {item} : {price}")

            # Ask for an item from the selected category
            item_1 = input(" Enter the item you want to order ---> ")

            # Check if the item exists in the selected category
            if item_1 in menu[selected_category]:
                order_total += menu[selected_category][item_1]  # Add item price to total
                print(f" Your item '{item_1}' has been added to your order!")
            else:
                print(f" Ordered item '{item_1}' is not available in {selected_category}!")
        else:
            print(f" Selected category '{selected_category}' is not available!")

        # Ask if the user wants to order more items
        another_order = input(" Do you want to order from another category? (Yes/No) ---> ")

        # Exit the loop if the user doesn't want to order more
        if another_order.lower() != "yes":
            break

    # Print the total bill
    print(f" Your total bill is ---> {order_total}")

    #print a sweet note
    print("-------------------THANK YOU FOR VISITING OUR RESTAURANT----------------------")

# Call the restaurant function to start the program
restaurant()
