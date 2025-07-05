'''
Operation.py file
To handle all the logical operations of the system like:
Getting customer details, printing land details, getting and validating kitta number, renting out land, returning land
Manipulate text file to make land "Available and "NotAvailable " accordingly, print details of rented and returned land,
Calculate total cost, calculate total fine, calculate grand total and print bill in terminal. Most try, except blocks are used here
'''
import Read

#Function to get customer details
def customer_details():
    """
    Gets and validates customer name and phone number
    Returns customer_name, and customer_number
    """
    loop = True 
    #Loop until valid name is entered
    while loop:
        try:
            customer_name = input("Please enter your name: ")
            #Validate name
            if customer_name.isalpha():
                break
            else:
                print("Invalid Name")
        except ValueError:
            print("Invalid input. Please enter a valid name.")
    
    #Loop until valid phone number is entered
    while loop:
        try:
            customer_number = input("Please enter your phone number: ")
            # Validate phone number
            if len(customer_number) == 10 and customer_number.isdigit():
                break
            else:
                print("Invalid Number, try again")
        except ValueError:
            print("Invalid input. Please enter a valid phone number.")
    
    # Print separator
    print("\n")
    print("." * 232)
    print("\n\n")
    
    # Print welcome message
    print("Welcome, ", customer_name)
    print("Please look at the land details below,")
    print("\n")
    
    # Return customer name and phone number
    return customer_name, customer_number


#Function to print land details
def print_land_details():
    """
    Reads and stores land data in a dictoinary(Land_details)
    Prints the details of land from text file
    """
    #Land details
    Land_details = Read.read_data()
    Kitta_no = 101
    #Printing the land details in format
    for line in Land_details:
        print(Kitta_no,"\t\t  ",Land_details[Kitta_no][0],"\t\t  ",Land_details[Kitta_no][1],"\t\t ",Land_details[Kitta_no][2],"\t\t     ",Land_details[Kitta_no][3],"\t\t     ",Land_details[Kitta_no][4])
        Kitta_no += 1
        
#Function to rent land
def rent_land():
    """
    Reads and stores land data in a dictoinary(Land_details)
    Asks the user to input the kitta number of the land they wish to rent and validates it
    After renting stores the details of rented land in a list(rented_land_list)
    Loops the renting process if user wants to rent more land
    Returns rented_land_list
    """
    #List to store rented land details
    rented_land_list = []
    #Infinite loop to keep renting land until the user decides to exit
    while True:
        try:
            #Read land details from file
            Land_details = Read.read_data()
            print("Note that you can only rent land which is available!")
            #Ask the user to input the kitta number of the land they wish to rent
            Kitta_no = int(input("Please enter the kitta number of the land you wish to rent:"))
            print("\n")

            #Check if the entered kitta number exists in the land details
            if Kitta_no in Land_details:
                #Print the status of the land
                print("Land status:", Land_details[Kitta_no][4])
                #Check if the land is available for rent
                if Land_details[Kitta_no][4].lower() == "available":
                    print("\n")
                    print("This land is available for rent.")
                    #Ask the user if they want to rent the land
                    print("This property contains ", Land_details[Kitta_no][2], "Annas of land. Do you want to rent this property?")
                    user_choice = input("Enter YES or NO: ")
                    print("\n")

                    #If the user chooses to rent the land
                    if user_choice.lower() == "yes":
                        #Add renting details to the rented_land_list
                        rented_land_list.append(renting_details(Kitta_no))
            
                        #Update the land status to "Not Available"
                        modify_to_NotAvailable(Kitta_no)
                        print("\n")
                        
                        #Ask the user if they want to rent more property or exit
                        user_choice = input("Do you want to rent more property? Enter No to exit: ")
                        if user_choice.lower() == "no":
                            print("Thank you for renting land, please continue browsing our system")
                            break
                else:
                    #If the land is not available for rent
                    print("Sorry, the land with Kitta number", Kitta_no, "is not available for rent.")
            else:
                #If the entered kitta number does not exist
                print("Land with this Kitta number does not exist. Please enter a valid kitta number.")
        
        #Handle the case of invalid input (non-integer kitta number)
        except ValueError:
            print("Invalid input. Please enter a valid Kitta number.")
    return rented_land_list

#Function to gather details of rented property
def renting_details(Kitta_no):
    """
    Asks the user the number of months to rent the land
    Validates it
    Calculates total cost
    Returns laand details and total cost
    """
    #Infinite loop to keep asking for input until valid input is provided
    while True:
        try:
            #Ask the user for the number of months they wish to rent the property for
            months_rented = int(input("Please enter the number of months for which you wish to rent this property: "))
            #Check if the entered value is valid (greater than 0)
            if months_rented <= 0:
                print("Invalid entry for Months. Please enter a value greater than 0.")
                continue
            #Read land details from file
            Land_details = Read.read_data()
            
            #Take the price per month from dictionary
            price_per_month = int(Land_details[Kitta_no][3])
            
            #Calculate the total cost of renting the property for the specified number of months
            total_cost = price_per_month * months_rented
            
            #Return a list containing the renting details
            return [str(Kitta_no), Land_details[Kitta_no][0], Land_details[Kitta_no][1], Land_details[Kitta_no][2], Land_details[Kitta_no][3], str(months_rented), str(total_cost)]
        
        #Handle the case of invalid input (non-integer input for months)
        except ValueError: 
            print("Invalid entry for Months.")

    

#Function to modify the status of a rented property to "Not Available"
def modify_to_NotAvailable(rented_no):
    """
    Reads land data
    Modifies "Available" status of rented land to "NotAvailable"
    Rewrites the land data in text file with modified data
    """
    try:
        #Read land details from file
        Land_details = Read.read_data()
        
        #Open the 'land.txt' file in write mode
        with open("Land.txt", "w") as file:
            #Iterate through the land details
            for Kitta_no, line in Land_details.items():
                #Check if the current kitta number matches the rented number
                if Kitta_no == rented_no:
                    #Update the status of the rented property to "Not Available"
                    line[4] = "Not_Available"
                #Write the updated line to the file
                file.write(','.join(line) + '\n')
    
    #Handle the case where the 'land.txt' file is not found
    except FileNotFoundError:
        print("Error: land.txt file not found")


#Function to print details of rented properties
def print_rented_land_details(rented_land_list):
    """
    Itterates the rented_land_list
    Prints the details of rented land in format
    Calculates grand total
    """
    grand_total = 0
    
    #Iterate over rented_land_list and print details of each rented property
    for property_details in rented_land_list:
        #Print property details
        print(property_details[0],"\t\t  ",property_details[1],"\t\t  ",property_details[2],"\t\t ",property_details[3],"\t\t     ",property_details[4],"\t\t\t   ",property_details[5],"\t\t\t   ",property_details[6])
        
        #Add the total cost of the current property to grand total
        grand_total += int(property_details[6])
        print("\n")
        
    #Printing grand total and thank you message
    print("." * 232)
    print("Grand Total: Rs.", grand_total)
    print("." * 232)
    print("\n\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tTHANK YOU FOR RENTING!")



#Function to return rented land
def return_land():
    """
    Reads and stores land data in a dictoinary(Land_details)
    Asks the user to input the kitta number of the land they wish to return and validates it
    After returning, stores the details of returned land in a list(returned_land_list)
    Loops the returning process if user wants to return more land
    Returns returned_land_list
    """
    #List to store returned land details
    returned_land_list = []
    
    #Infinite loop to keep returning land until the user decides to exit
    while True:
        try:
            #Read land details from file
            Land_details = Read.read_data()
            print("Note that you can only return land which is not available!")
            #Ask the user to input the kitta number of the land they wish to return
            Kitta_no = int(input("Please enter the kitta number of the land you wish to return:"))
            print("\n")
            
            #Check if the entered kitta number exists in the land details
            if Kitta_no in Land_details:
                #Print the status of the land
                print("Land status:", Land_details[Kitta_no][4])
                
                #Check if the land is not available
                if Land_details[Kitta_no][4].lower() == "not_available":
                    print("\n")
                    print("This land can be returned.")
                    #Ask the user if they want to return the land
                    print("Do you want to return this property?")
                    user_choice = input("Enter YES or NO: ")
                    print("\n")

                    #If the user chooses to return the land
                    if user_choice.lower() == "yes":
                        #Add returning details to the returned_land_list
                        returned_land_list.append(returning_details(Kitta_no))
                        
                        #Update the land status to "Available"
                        modify_to_Available(Kitta_no)
                        print("\n")
                        
                        #Ask the user if they want to return more property or exit
                        user_choice = input("Do you want to return more property? Enter No to exit: ")
                        if user_choice.lower() == "no":
                            print("Thank you for returning land, please continue browsing our system")
                            break
                else:
                    #If the land has not been rented
                    print("Sorry, the land with Kitta number", Kitta_no, "has not been rented.")
            else:
                #If the entered kitta number does not exist
                print("Land with this Kitta number does not exist. Please enter a valid kitta number.")
        
        #Handle the case of invalid input (non-integer kitta number)
        except ValueError:
            print("Invalid input. Please enter a valid Kitta number.")
    
    #Return the list of returned land details
    return returned_land_list


#Function to gather details for returned property
def returning_details(Kitta_no):
    """
    Asks the user the number of months the land was rented for
    Asks the number of months after which the land is returned
    Validates it
    Calculates total cost
    Calculates total fine
    Returns kitta number, land details, total cost and fine

    """
    #Infinite loop to keep asking for input until valid input is provided
    while True:
        try:
            #Read land details from file
            Land_details = Read.read_data()
            
            #Extract the price per month for the rented property
            price_per_month = int(Land_details[Kitta_no][3])
            
            #Ask the user for the number of months they initially rented the property for
            months_rented = int(input("Please enter the number of months for which you rented this property: "))
            
            #Ask the user for the number of months after which they are returning the property
            returned_after = int(input("Please enter the number of months after which you are returning this property: "))
            
            #Check if the entered values are valid
            if months_rented <= 0 or returned_after <= 0:
                print("Invalid entry for Months. Please enter a value greater than 0.")
                continue
            
            #Calculate the total cost based on the number of months rented
            if(months_rented >= returned_after):
                fine = 0
                total_cost = (price_per_month * months_rented) 
                print("You will be charged for the full duration of rent")

            elif(months_rented < returned_after):
                months_delayed = returned_after - months_rented
                total_cost = price_per_month * returned_after
                fine =  0.1 * (months_delayed * price_per_month)
            #Return a list containing the returning details
            return (str(Kitta_no), Land_details[Kitta_no][0], Land_details[Kitta_no][1], Land_details[Kitta_no][2], Land_details[Kitta_no][3], str(months_rented), str(returned_after), str(total_cost), str(fine))
        
        #Handle the case of invalid input (non-integer input for months)
        except ValueError:
            print("Invalid input")


#Function to modify the status of a returned property to "Available"
def modify_to_Available(return_no):
    """
    Reads land data
    Modifies "NotAvailable" status of returned land to "Available"
    Rewrites the land data in text file with modified data
    """
    try:
        #Read land details from a data source (assuming a function named 'read_data' from a module named 'Read')
        Land_details = Read.read_data()
        
        #Open the 'land.txt' file in write mode
        with open("land.txt", "w") as file:
            #Iterate through the land details
            for kitta_no, line in Land_details.items():
                #Check if the current kitta number matches the returned number
                if kitta_no == return_no:
                    #Update the status of the returned property to "Available"
                    line[4] = "Available"
                
                #Write the updated line to the file
                file.write(','.join(line) + '\n')
    
    #Handle the case where the 'land.txt' file is not found
    except FileNotFoundError:
        print("File not found")


#Function to print details of returned land
def print_returned_land_details(returned_land_list):
    """
    Itterates the returned_land_list
    Prints the details of returned land in format
    Calculates total, total fine and grand total
    """
    #Initialize total price and total fine
    total_price = 0
    total_fine = 0
    
    #Iterate over returned_land_list and print details of each returned property
    for property_details in returned_land_list:
        #Print property details
        print(property_details[0],"\t\t  ",property_details[1],"\t\t  ",property_details[2],"\t\t ",property_details[3],"\t\t     ",property_details[4],"\t\t\t   ",property_details[5],"\t\t\t      ",property_details[6],"\t\t\t  ", property_details[7],"\t\t", property_details[8])
        
        #Add the total price of the current property to total price
        total_price += int(property_details[7])
        
        #Add the total fine of the current property to total fine
        total_fine += float(property_details[8])
    
    #Calculate grand total
    grand_total = total_price + total_fine
    print("." * 232)
    print("\n")
    
    #Print total price, total fine, and grand total
    print("Total Price: Rs.", total_price)
    print("Total Fine: Rs.", total_fine)
    print("."*232)
    print("Grand Total: Rs.", grand_total )
    print("."*232)
    print("\n\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tTHANK YOU FOR RETURNING!")

