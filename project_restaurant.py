def restaurant():

    ##--------------Greet--------------

    print("---------------Welcome To The Mr.MOMO Restrunt----------------")


    menu = {
        
            "Paneer Pizza" : 100,
            " Chicken Pizza" : 150,
            
            
        
            "Cold Coffee" : 140,
            "Hot Coffee" : 120,
            
        
        
            "Masala Chai" : 25,
            "Tandoori Chai" : 30,
            "Normal Chai" : 10,
    
        
        
            "Veg Burger" : 70,
            " Chicken Burger" : 80,
        
            
        
            "Paneer Momo" : 80,
            "Chicken Momo" : 90,
            "Steam Momo" : 70,
            
            
        
            "Chocolate Pastry" : 70,
            "Vanilla Pastry" : 65,
        
            
    }


    print(" This Is The Menu ----> \n Paneer Pizza : 100,\n Chicken Pizza : 150,\n Cold Coffee : 140 ,\n Hot Coffee : 120,\n Masala Chai : 25,\n Tandoori Chai : 30,\n Normal Chai : 10, \n Veg Burger : 70,\n Chicken Burger : 80,\n Paneer Momo : 80,\n Chicken Momo : 90,\n Steam Momo : 70,\n Chocolate Pastry : 70,\n Vanilla Pastry : 65,")

   
    
    ## TO ADD ON ALL THE PRICES FOR BILL
    
    
    order_total = 0
    
    
    
    while True:
        item_1 = input(" Enter The Item You Want To Order ---> ") ## you also write item_1 ----> item
        if item_1 in menu:
           order_total += menu[item_1] 
           print(f" Your Item '{item_1}' Has Been Added To Your Order !")
           
        else:
            print(f" Ordered Item '{item_1}' Is not Avaiblale Yet ! ")
        
        another_order = input(" Do You Want To Add Anything More ? ( Yes / No ) ---> ")
        
        if another_order.lower() != "yes":
            break
            
    print (f" Your Total Bill Is ---> {order_total}")

    #print a sweet note
    print("-------------------THANK YOU FOR VISITING OUR RESTAURANT----------------------")   
restaurant()



















































































