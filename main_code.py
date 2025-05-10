# Project Name: Automated Billing Software


# Team Details (Sorted by Name):
# 1. Naveen S (naveen9819687@gmail.com)
# 2. Pon Prathakshana G (pponprathakshana@gmail.com)
# 3. Razeena Tasneem B (razeenatasneem@gmail.com)
# 4. ResheKumar V (vrk1711@gmail.com)
# 5. Rishapthi J (rishapthi2007@gmail.com)
# 6. Sanjay Kumar S (sanjaykumarsk162007@gmail.com)
# 7. Sanjai M S (sanjaims103@gmail.com)


# import necessary modules
import support as m1
import time, os
import pandas as pd


'''The admin() function allows adminstrators to manage the systems by performing various tasks that include adding new 
employees,adding new products,updating existing product prices,deleting products and viewing all products'''

def admin():
    # Get admin credentials
    uid = input("Enter your user id : ")
    pas = input("Enter your password : ")
    # Verify admin credentials
    result = m1.check_admin(uid,pas)
    if result == "verified":
        # Loop until admin chooses to exit
        ch = "y"
        while ch.lower() == "y":
            # Clear the screen and display admin menu
            os.system('cls')
            print("1.Add Employee\n2.Add Data\n3.Update Data\n4.Delete Data\n5.View Data\n6.Exit")
            # Gets admin's choice
            choice = int(input("Enter your choice (1/2/3/4/5/6) : "))
            # Handle admin's choice
            match choice:
                case 1:
                    # Add a new employee
                    os.system('cls')
                    new_user = input("Enter the new ID :")
                    new_pass = input("Enter the new Password :")
                    m1.add_employee(new_user,new_pass)
                    print("The employee is added successfully !")
                    time.sleep(2)
                    m1.view_employee()
                    ch = input("Do you want to continue (y/n)? ")
                case 2:
                    # Add a new product
                    os.system('cls')
                    name = input("Product Name : ")
                    price = int(input("Price : "))
                    m1.add_data(name, price)
                    print("The product has been added to the list !")
                    ch = input("Do you want to continue (y/n)? ")
                case 3:
                    # Update an existing product
                    os.system('cls')
                    name = input("Enter the product name : ")
                    price = int(input("Enter the altered price : "))
                    m1.update_data(name, price)
                    print("The product price has been modified successfully !")
                    ch = input("Do you want to continue (y/n)? ")
                case 4:
                    # Delete a product
                    os.system('cls')
                    name = input("Enter the name of the item to be removed : ")
                    m1.del_data(name)
                    print("The product has been removed successfully !")
                    ch = input("Do you want to continue (y/n)? ")
                case 5:
                    # View all products
                    os.system('cls')
                    m1.display_data()
                    time.sleep(5)
                    os.system('cls')
                    ch = input("Do you want to continue (y/n)? ")
                case 6:
                    # Exit admin menu
                    print("Exited successfully !")
                    break
                case _:
                    # Handle invalid input
                    print("Invalid input")
                    break
    else:
        # Display error message for invalid credentials
        print("Invalid username or password")
        time.sleep(2)

'''The employee() function allows employees to manage products by performing tasks such as adding new products,updating 
existing product prices,viewing all product'''
def employee ():
    # Get employee credentials
    uid = input("Enter your user id : ")
    pas = input("Enter your password : ")
    # Verify employee credentials
    result = m1.check_employee(uid,pas)
    if result == "verified":
        # Display success message
        print("Employee login successful !")
        # Loop until employee chooses to exit
        ch = "y"
        while ch.lower() == "y":
            os.system('cls')
            # Get employee choice
            print("1.Add product\n2.Update product\n3.View products\n4.Exit")
            choice = int(input("Enter your choice (1/2/3/4): "))
            # Handle employee's choice
            match choice:
                case 1:
                    # Add a new product
                    os.system('cls')
                    name = input("Enter product name: ")
                    price = int(input("Enter product price: "))
                    m1.add_data(name, price)
                    print("Product has been added successfully !")
                    ch = input("Do you want to continue(y/n)? ")
                case 2:
                    # update an existing product
                    os.system('cls')
                    name = input("Enter the product name to be updated: ")
                    price = int(input("Enter price to be updated: "))
                    m1.update_data(name, price)
                    print("Product has been updated successfully !")
                    ch = input("Do you want to continue(y/n)? ")
                case 3:
                    # View all products
                    os.system('cls')
                    m1.display_data()
                    time.sleep(5)
                    os.system('cls')
                    ch = input("Do you want to continue(y/n)? ")
                case 4:
                    #To exit the option
                    print("Exited successfully !")
                    break
                case _:
                    # Handle invalid input for user type
                    print("Invalid input")
                    # Break out of the loop
                    break
    else:
        # Print error messsage for invalid username or password
        print("Invalid username or password")
        # Pause execution for 2 seconds
        time.sleep(2)

'''The customer() function simulates an ecommerce experience  and allow customers to view available products,add products 
to their cart,vie their vart and proceed to billing and payment'''

def customer ():
    # Welcome message for customer
    print("Welcome, Customer!")
    # Intialize a variable to track user's choice to continue
    ch = "y"
    # Initialize an empty cart
    cart = []
    # Initialize total price and discount
    total_price = 0
    discount = 0
    # Loop until user chooses to exit
    while ch.lower() == "y":
        # clear the console
        os.system('cls')
        # Display menu options
        print("1. View Products\n2. Add to Cart\n3. View Cart\n4. Billing\n5. Exit")
        try:
            # Get users choice
            choice = int(input("Enter your choice (1/2/3/4/5): "))
            # Use match statement to handle different choices
            match choice:
                # Handle view products option
                case 1:
                    # Clear the console
                    os.system('cls')
                    # Display products
                    m1.display_data()
                    # Pause execution for 5 seconds
                    time.sleep(5)
                    # Ask user idf they want to continue
                    ch = input("Do you want to continue (y/n)? ")
                    # Handle add to cart option
                case 2:
                    # Clear the console
                    os.system('cls')
                    # Prompt user to enter item numbers to add to cart
                    print("Enter item numbers to add to cart (enter -1 to finish):")
                    # Display the products
                    m1.display_data()
                    # Loop until user finishes adding items
                    while True:
                        # Get item number from the user
                        try:
                            num = int(input("Enter the item number: "))
                            # Check if user wants to finish adding items
                            if num == -1:
                                # Break out of the loop
                                break
                            # Read database.csv file
                            df = pd.read_csv("database.csv",index_col=0)
                            # Check if the item number is valid
                            if num in df.index:
                                # Get item name and price
                                item_name = df.loc[num, "item_name"]
                                item_price = df.loc[num, "price"]
                                # Add item to cart
                                cart.append((num, item_name, item_price))
                                # Update total price
                                total_price += item_price
                                # Print conformation message
                                print(f"Added {item_name} to cart!")
                            else:
                                # Print error message for invalid item number
                                print("Invalid item number.")
                        except ValueError:
                            # print error message for invalid input
                            print("Please enter a valid number.")
                    # print cart total
                    print(f"Cart total: {total_price}")
                    # Ask user if they want to continue
                    ch = input("Do you want to continue (y/n)? ")

                # Handle view cart option
                case 3:
                    # clear the console
                    os.system('cls')
                    # Check if the cart is empty
                    if not cart :
                        # print message the cart is empty
                        print("Your cart is empty.")
                    else:
                        # print cart contents
                        print("Your Cart:")
                        for item in cart:
                            # Print each item in the cart
                            print(f"Item {item[0]}: {item[1]} - ₹{item[2]}")
                        # Print total price
                        print(f"Total: {total_price}")
                    # Pause execution for 5 seconds
                    time.sleep(5)
                    # Ask user if they want to continue
                    ch = input("Do you want to continue (y/n)? ")
                case 5:
                    #Print thankyou message for the customer
                    print("Thank you for shopping!")
                    break
                case 4:
                    #Clear the console
                    os.system('cls')
                    # Check if cart is empty
                    if not cart:
                        print("Your cart is empty. Please add items before proceeding to billing.")
                    else:
                        # Print billing summary
                        print("=== Billing Summary ===")
                        for item in cart:
                            print(f"Item {item[1]} - ₹{item[2]}")
                        tax = total_price * 0.18
                        if total_price >1000:
                            discount = total_price*0.1
                        print("="*40)
                        print(f"Total Price : ₹{total_price}")
                        print(f"Tax : ₹{tax}")
                        print(f"Discount : ₹{discount}")
                        print(f"Final prize : ₹{total_price - discount + tax}")
                        # Ask user to confirm purchase
                        confirm = input("Confirm purchase (y/n)? ")
                        if confirm.lower() == "y":
                            # Print successful message
                            print("Purchase successful! Thank you for shopping!")
                            # Reset cart and total price
                            cart = []
                            total_price = 0
                        else:
                            print("Purchase cancelled.")

                    # Pause execution for 5 seconds
                    time.sleep(5)
                    # Ask if the user want to continue
                    ch = input("Do you want to continue (y/n)? ")
                # Handle invalid input
                case _:
                    # Print eror message
                    print("Invalid input")
                    # Ask if they want to continue
                    ch = input("Do you want to continue (y/n)? ")
        except ValueError:
            # Printing the error message
            print("Please enter a valid number.")
            # Ask the user if they want to continue
            ch = input("Do you want to continue (y/n)? ")

'''The main() function serves as the entry point of the automated billing software and it displays a menu to select user
 type,cals the correponding function baseed on user input,handles invalid inputs and exceptions and asks the user if they 
 want to continue using the software'''
def main ():
    ch = 'y'
    # Loop until user chooses to exit
    while ch.lower() == "y":
        try:
            #Clear the console
            os.system('cls')
            # Display title and menu
            print("An automated billing software created by students of CSE - C".center(170))
            # Get the user type from user
            print("1.Admin\n2.Employee\n3.Customer\n4.Exit")
            user_type = int(input("Enter user type(1/2/3/4): "))
            # Use match statement to handle different user types
            match user_type:
                case 1:
                    # Clear console and call admin function
                    os.system("cls")
                    admin()
                case 2:
                    # Clear console and call employee function
                    os.system("cls")
                    employee()
                case 3:
                    # Clear the console and call customer function
                    os.system("cls")
                    customer()
                    print("Thankyou for using our service. Visit us again!")
                case 4:
                    # Clear the console and print exit message
                    os.system("cls")
                    print("Exited. Thankyou for using our service".center(170))
                    break
                case _:
                    # Print the error message
                    print("Invalid input. Enter a valid choice.")
        # Handle value error exception
        except ValueError:
            print("Please enter a valid number.")
            # Ask the user if they want to continue
            ch = input("Do you want to continue (y/n)? ")
#Check if the script is being run directly
if __name__ == "__main__":
    main()
