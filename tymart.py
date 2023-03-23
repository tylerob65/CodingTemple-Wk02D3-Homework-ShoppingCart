from time import sleep
import sys
def go_shopping():
    """
    Function to simulate shopping.
    """    
    def p(text=""):
        """
        Make texted printed to console look like it is being typed
        The function below was created using knowledge gained from link below
        https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
        """
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.01)
        sleep(0.4)
        print()
        return
    
    def list_valid_commands():
        """
        Outputs a list of valid user commands.
        """
        p("Here are your list of commands...")
        print()
        p("'quit'")
        p(" Enter this to leave TyMart and get a print out of your current shopping cart")
        print()
        p("'show'")
        p(" Shows you your current shopping cart")
        print()
        p("'add'")
        p(" You will be prompted to add an item to your cart")
        print()
        p("'subtract'")
        p(" You will be prompted to subtract an item from your cart")
        print()
        p("'clear")
        p(" You will empty your shopping cart")
        print()
        p("'commands'")
        p(" Lists the commands that you can run")
        print()
        print()
        return

    def get_command():
        """
        Function to handle and route all commands.
        """
        valid_commands = {"quit","show","add","subtract","clear","commands"}
        still_shopping = True
        while still_shopping:
            p("What would you like to do next?: ")
            # Get command from user
            command = input().strip().lower()
            if command not in valid_commands:
                p("That is not a valid command, please try again")
                p("Enter 'commands' for a list of commands you can run")
                continue
            if command == "quit":
                still_shopping = False
                return
            elif command == "show":
                do_show()
            elif command == "add":
                still_shopping = do_add()
            elif command == "subtract":
                still_shopping = do_subtract()
            elif command == "clear":
                cart.clear()
                p("Your cart is now empty")
            elif command == "commands":
                list_valid_commands()
        return

    def do_quit():
        """
        Function to initiate checkout and end shopping trip.
        """
        p("Leaving so soon?")
        p("It was nice of you to stop by!")
        p("Here is what you bought today...")
        print()
        do_show()
        p("Please come again soon")
        return

    def do_show():
        """
        Function to show current contents of shopping cart.
        """
        if not cart:
            p("You don't have anything in your cart")
            p()
            return
        
        # Gets longest length item in list, used in text justification
        longest_item = max(max(len(key) for key in cart),4)

        # Demos format of how cart will be printed
        p(f"{'Item'.ljust(longest_item,' ')} --- Quantity in cart")
        print()

        # Loops through cart, printing all items and quantities
        for item,quantity in cart.items():
            p(f"{item.ljust(longest_item,' ')} --- {quantity}")
        print()
        return
    
    def do_add():
        """
        Function to add items to cart. Returns True if didn't quit shopping
        while adding.
        """
        # Makes sure valid item and quantity
        # Outsources checking to other functions
        # When calling those function, clarifies that
        # call is from the do_add function
        (item,still_shopping) = get_valid_item(add_not_subtract=True)
        if not still_shopping: return False
        (add_amount,still_shopping) = get_valid_quantity(add_not_subtract=True)
        if not still_shopping: return False
        
        # Handles and edge case to avoid items in cart with
        # zero quantity
        if (item not in cart) and add_amount == 0:
            return True
        
        # Adds item to cart
        cart[item] = cart.get(item,0) + add_amount
        return True
    
    def do_subtract():
        """
        Function to subtract items from cart. Returns if True didn't quit shopping
        while adding.
        """
        # First checks if there is anything to subtract. Doesn't let you
        # if cart is empty
        if not cart:
            p("There is nothing in your cart to subtract!")
            return True
        
        # Makes sure valid item and quantity
        # Outsources checking to other functions
        # When calling those function, clarifies that
        # call is from the do_subtract function. Need to
        (item,still_shopping) = get_valid_item(add_not_subtract=False)
        if not still_shopping: return False
        # Item needs to be passed into function to get a 
        # valid quantity
        (subtract_amount,still_shopping) = get_valid_quantity(add_not_subtract=False,item=item)
        if not still_shopping: return False

        # Completely removes items from cart if subtracted everything
        if subtract_amount == cart[item]:
            del cart[item]
        
        else:
            cart[item] -= subtract_amount
        return True

    def get_valid_item(add_not_subtract=True):
        """
        Support function to find an item that can be added or subtracted
        from cart.
        add_not_subtract = True -> Called from do_add, 
        add_not_subtract = False -> Called from do_subtract. 
        Function also returns whether still shopping (ie, did 
        person quit). 
        """
        # Used to customize prompt based on whether adding or subtracting
        question_str = "add" if add_not_subtract else "subtract"

        still_shopping = True

        # Loops until valid item is given or user quits
        while True:
            p(f"What would you like to {question_str}?: ")
            item = input().strip().lower()
            if not item:
                p("You didn't enter anything, please try again.")
                p("Enter 'show' to see what you currently have in your cart")
                print()
                continue
            
            if item == "quit":
                still_shopping = False
                break

            if item == "show":
                do_show()
                continue

            # Makes sure you can subtract an item not in your cart
            if (not add_not_subtract) and (item not in cart):
                p("This item isn't in cart, you can't remove it")
                p("Enter 'show' to see what you currently have in your cart")
                continue
            break
            
        return (item,still_shopping)
    
    def get_valid_quantity(add_not_subtract=True,item=None):
        """
        Support function to find an quantity of an item that
        can be added or subtracted from the cart. 
        add_not_subtract = True -> Called from do_add. 
        add_not_subtract = False -> Called from do_subtract. 
        item -> Only needed when called from do_subtract. 
        Function also returns whether still shopping (ie, did 
        person quit). 
        """
        # Used to customize prompt based on whether adding or subtracting
        question_str = "add" if add_not_subtract else "subtract"

        still_shopping = True

        # Loops until valid quantity is given or user quits
        while True:
            if item:
                p(f"You curently have {cart[item]} in your cart.")
            p(f"How many would you like to {question_str}?")
            quantity = input().strip()
            if not quantity:
                p("Please enter in a non-negative integer")
                continue
            if quantity == "quit":
                still_shopping = False
                break
            try:
                quantity = int(quantity)
            except:
                p("Input must by a non-negative integer")
                continue
            if quantity < 0:
                p("Input must by a non-negative integer")
                continue            
            if (not add_not_subtract) and (quantity > cart[item]):
                p("You are trying to subtract more than you have in your cart")
                p(f"you currently only have {cart[item]} item(s)")
                continue
            break

        return (quantity,still_shopping)
        

    ### This is the actual function ###
    # Welcomes people
    p("..................")
    p("Welcome to TyMart!")
    p("..................")
    p()
    
    # Greets people with a list of valid comments
    list_valid_commands()
    
    # Initializes shopping cart
    cart = dict()
    # cart["tyler"] = 1

    # Starts running commands, initiates main loop
    try:
        get_command()
        do_quit()
    except:
        p()
        p("Shoplifer!!!!!!")
        p("GET BACK HERE!!!")
    
if __name__ == "__main__":
    go_shopping()


