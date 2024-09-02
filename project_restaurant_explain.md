### Detailed Explanation of the `restaurant()` Function

This function simulates a simple restaurant order-taking system. Here's a step-by-step breakdown of the code:

#### 1. **Function Definition**
```python
def restaurant():
```
- The `restaurant()` function is defined without any parameters. This function contains the entire logic for interacting with the user, taking orders, and calculating the total bill.

#### 2. **Greeting the Customer**
```python
print("---------------Welcome To The Mr.MOMO Restrunt----------------")
```
- This line prints a welcome message to greet the customer when the function is called.

#### 3. **Menu Creation**
```python
menu = {
    "Paneer Pizza" : 100,
    "Chicken Pizza" : 150,
    "Cold Coffee" : 140,
    "Hot Coffee" : 120,
    "Masala Chai" : 25,
    "Tandoori Chai" : 30,
    "Normal Chai" : 10,
    "Veg Burger" : 70,
    "Chicken Burger" : 80,
    "Paneer Momo" : 80,
    "Chicken Momo" : 90,
    "Steam Momo" : 70,
    "Chocolate Pastry" : 70,
    "Vanilla Pastry" : 65,
}
```
- A dictionary named `menu` is created where each key represents an item on the menu, and each value represents the price of that item.

#### 4. **Displaying the Menu**
```python
print(" This Is The Menu ----> \n Paneer Pizza : 100,\n Chicken Pizza : 150,\n Cold Coffee : 140 ,\n Hot Coffee : 120,\n Masala Chai : 25,\n Tandoori Chai : 30,\n Normal Chai : 10, \n Veg Burger : 70,\n Chicken Burger : 80,\n Paneer Momo : 80,\n Chicken Momo : 90,\n Steam Momo : 70,\n Chocolate Pastry : 70,\n Vanilla Pastry : 65,")
```
- This line prints the menu to the console, showing the user all available items and their prices.

#### 5. **Initializing the Order Total**
```python
order_total = 0
```
- A variable `order_total` is initialized to `0`. This variable will store the cumulative cost of the items ordered by the user.

#### 6. **Taking Orders in a Loop**
```python
while True:
    item_1 = input(" Enter The Item You Want To Order ---> ")
```
- The program enters an infinite loop where it continuously prompts the user to enter an item they want to order. The user's input is stored in the variable `item_1`.

#### 7. **Checking the Availability of the Item**
```python
if item_1 in menu:
   order_total += menu[item_1] 
   print(f" Your Item '{item_1}' Has Been Added To Your Order !")
else:
   print(f" Ordered Item '{item_1}' Is not Avaiblale Yet ! ")
```
- The program checks if the entered item exists in the `menu` dictionary:
  - If the item is available, its price is added to the `order_total`, and a message is printed confirming the addition.
  - If the item is not available, a message informs the user that the item is not available.

#### 8. **Asking for Additional Orders**
```python
another_order = input(" Do You Want To Add Anything More ? ( Yes / No ) ---> ")
```
- After processing the first order, the program asks the user if they want to add more items to their order. The user's response is stored in the variable `another_order`.

#### 9. **Exiting the Loop**
```python
if another_order.lower() != "yes":
    break
```
- The loop continues if the user inputs "yes" (case-insensitive). If the user inputs anything else, the loop breaks, and no more items are added to the order.

#### 10. **Printing the Total Bill**
```python
print(f" Your Total Bill Is ---> {order_total}")
```
- Once the loop exits, the program prints the total amount due, which is stored in `order_total`.

#### 11. **Thanking the Customer**
```python
print("-------------------THANK YOU FOR VISITING OUR RESTAURANT----------------------")
```
- Finally, a thank-you message is printed to the customer, signaling the end of the interaction.

#### 12. **Calling the Function**
```python
restaurant()
```
- The function is called at the end of the script, starting the entire process when the script is run.

### Summary
This Python program is a simple simulation of a restaurant's order system, where a user can order items from a menu, see their total bill, and receive a thank-you message upon completing their order. The use of a dictionary (`menu`) allows easy retrieval of item prices, and the while loop enables the user to keep adding items until they decide to stop.