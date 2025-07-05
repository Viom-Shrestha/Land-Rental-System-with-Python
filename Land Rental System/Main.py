'''
Main.py file
It is the main module that runs the system and call on all the other modules.
based on user's choice it calls on different functions
'''
import Write
#Printing the main interface of the system
Write.main_GUI()

loop=True
while loop == True:
    try:
        #Asking the user to select the option
        user_selection = int(input("Enter your choice to continue:"))
        #Calling the functions based on the user selection
        if user_selection == 1:
            #Calling the rentGUI function to print the interface for renting and getting customer's name and number
            customer_name, customer_number = Write.rent_GUI()
            #Calling the rented_land_details function to get the details of the lands rented
            rented_land_list = Write.rented_land_details(customer_name, customer_number)
            #Calling the print_rent_invoice function to print the rent invoice
            Write.print_rent_invoice(customer_name, customer_number, rented_land_list)
        elif user_selection == 2:
            #Calling the returnGUI function to print the interface for returning and getting customer's name and number
            customer_name, customer_number = Write.return_GUI()
            #Calling the returned_land_details function to get the details of the lands returned
            returned_land_list = Write.returned_land_details(customer_name, customer_number)
            #Calling the print_return_invoice function to print the return invoice
            Write.print_return_invoice(customer_name, customer_number, returned_land_list)
        elif user_selection == 3:
            #Exiting from the system
            print("Thank you for your visit!")
            break
        else:
            print("Please enter correct option")
    except:
        print("Please enter valid input")


