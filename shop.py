####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "shaafal"
signature_flavors = ["tuna" , "salmon" , "red herring "]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    for item in menu:
      print ("-  '%s' " "( KD %s)" % (item , menu[item]))

def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for original in original_flavors:
        print ( "-  '%s' "  % original)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for signature in signature_flavors:
        print ( "-  '%s' "  % signature)

def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!

    if order in menu or order in signature_flavors or order in original_flavors:
        return True 
    else:
        return False 
        



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    
    print("ENTERE YOUR ORDER FROM THE MENUE OR PRESS Exit")

    while  True:
        order_l =input()
        if (order_l)== "Exit":
            print("THANK YOU FOR VISITING")
            break
        elif is_valid_order(order_l)== True:
            order_list.append(order_l)
            print("ENTERE ANOTHER OREDER")
        else :
            print (" PRINT THE ORDER CORRECTLY")

    return order_list       



def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >5:
        return False
    else :
        return True


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0.0
    # your code goes here!
    for order in order_list:
        if order in menu:
            total += menu[order]
        elif order in original_flavors:
            total += original_price
        else:
            total = signature_price
    return total      
    


def print_order(order_list):
    """
    Print the order of the customer.
    """

    print()
    print("Your order is: ")
    # your code goes here!
    for order in order_list:
        print(order)

    total = get_total_price(order_list) 
    print("That\'ll be KD %s " % (total))

    if accept_credit_card(total):
        print("this order is eligible for credit card ")
    else:
        print("this order is eligible for cash only ") 

    print(" THANK YOU For SHOPPING AT %s  : " %  (cupcake_shop_name))    



