class Restaurant:
    def __init__(self):
        self.orders = []
        self.tables = {1: 'Available', 2: 'Available', 3: 'Available'}
        self.inventory = {'Dish1': 10, 'Dish2': 5, 'Dish3': 20}

    def add_order(self, dish, quantity):
        self.orders.append({'dish': dish, 'quantity': quantity})

    def view_orders(self):
        return self.orders

    def manage_table(self, table_number, status):
        if table_number in self.tables:
            self.tables[table_number] = status
        else:
            print("Invalid table number.")

    def check_inventory(self):
        return self.inventory
