'''
Write.py file
To handle all the printing and displaying work of the system like:
Displaying the main GUI, GUI for rent and return, displaying land details,
Displaying details of land after renting and returning including the invoice
Printing the rent and return Invoice in a unique Text file
'''
import Operations
from datetime import datetime

#Function to print main gui
def main_GUI():    
    """
    Displays the Main GUI of the system including option for rent, return and exit
    """
    print("\n\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t    Techno Property Nepal")
    print("\n")
    print("\t\t\t\t\t\t\t\t\t Kausaltar,Bhaktapur | Phone no: 9808688665 | E-mail: technoproperty2070@gmail.com")
    print("\n\n")
    print("." *232)
    print("\t\t\t\t\t\t\t\t Welcome to Techno Property Nepal: Your gateway to Explore, Rent and Manage land properties all over Nepal")
    print("." *232)
    print("\n")
    print("." *232)
    print("Please select one of the following options to nagivate through our system:")
    print("." *232)
    print("\n\n")
    print("Press 1 to Rent land")
    print("Press 2 to Return land")
    print("Press 3 to Exit our system")
    print("\n")
    print("." *232)

#function to display GUI for renting
def rent_GUI():
    """
    Displays the renting interface of the system 
    Calls on function to get customer details
    Prints land details in tabular format
    Returns customer_name, customer_number
    """
    try:
        print("\n\n")
        print("\t\t\t\t\t\t\t\t\t\t\t\t    Techno Property Nepal")
        print("\n")
        print("\t\t\t\t\t\t\t\t\t Kausaltar,Bhaktapur | Phone no: 9808688665 | E-mail: technoproperty2070@gmail.com")
        print("\n\n")
        print("." *232)
        print("\t\t\t\t\t\t\t\t\t\t\t Before renting land please fill in the following details:")
        print("." *232)
        print("\n")
        #Calls on function to get customer details
        customer_name, customer_number=Operations.customer_details()
        print("." *232)
        print("Kitta                City                Direction               Anna                Price/mo                Availability")
        print("." *232)
        #Function to print land details in tabular format
        Operations.print_land_details()
        print("."*232)
        print("\n")
        return customer_name, customer_number;
    except:
        print("Error in rent_GUI")

#Function to display details of rented land
def rented_land_details(customer_name, customer_number):
    """
    Calls a function rent_land() to get the list of rented land
    Displays customer details
    Displays the detail of the land the customer rented in tabular format
    Returns rented_land_list
    """
    try:
        rented_land_list = Operations.rent_land()
        print("\n\n")
        print("\t\t\t\t\t\t\t\t\t\t\t\t    Techno Property Nepal")
        print("\n")
        print("\t\t\t\t\t\t\t\t\t Kausaltar,Bhaktapur | Phone no: 9808688665 | E-mail: technoproperty2070@gmail.com")
        print("\n\n")
        print("." *232)
        print("Customer Details:")
        print("." *232)
        print("Name of Customer: ", customer_name)
        print("Phone Number: ", customer_number)
        print("Date and time of Rent: ", datetime.now())
        print("." * 232)
        print("\n")
        print("Details of the land you rented: ")
        print("." *232)
        print("Kitta                City                Direction               Anna                Price/mo                Rented Period                Total Price")
        print("." *232)
        Operations.print_rented_land_details(rented_land_list)
        return rented_land_list
    except:
        print("Error in rented_land_details")

#function to print rent invoice in unique text file
def print_rent_invoice(customer_name, customer_number, rented_land_list):
    """
    Creates a unique text file
    Prints the Rent Invoice in the text file
    """
    try:
        #getting seconds
        time = str(datetime.now().second)
        #opening a text file with unique name
        with open (customer_name+customer_number+time+ ".txt" , "w") as file:
            file.write("\n\n")
            file.write("\t\t\t\t\t\t\t\t\t\t\t\t\tTechno Property Nepal")
            file.write("\n")
            file.write("\t\t\t\t\t\t\t\t\tKausaltar,Bhaktapur | Phone no: 9808688665 | E-mail: technoproperty2070@gmail.com")
            file.write("\n\n")
            file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t   RENT INVOICE")
            file.write("\n\n\n")
            file.write("." *232)
            file.write("\n")
            file.write("Customer Details:")
            file.write("\n")
            file.write("." *232)
            file.write("\n\n")
            file.write("Name of Customer: "+ customer_name)
            file.write("\n")
            file.write("Phone Number: "+ customer_number)
            file.write("\n")
            file.write("Date and time of Rent: "+ str(datetime.now()))
            file.write("\n\n\n")
            file.write("Details of the land you rented: ")
            file.write("\n")
            file.write("." *232)
            file.write("\n")
            file.write("Kitta                City                Direction               Anna                    Price/mo                Rented Period                Total Price")
            file.write("\n")
            file.write("." *232)
            file.write("\n")
            grand_total = 0
            for property_details in rented_land_list:
                file.write(str(property_details[0]) + "\t\t   " + str(property_details[1]) + "\t\t  " + str(property_details[2]) + "\t\t\t  " + str(property_details[3]) + "\t\t\t  " + str(property_details[4]) + "\t\t\t" + str(property_details[5]) + "\t\t\t " + str(property_details[6])+"\n")
                grand_total += int(property_details[6])
            file.write("." * 232)
            file.write("\n\n\n")
            file.write("Grand Total: Rs."+ str(grand_total))
            file.write("\n")
            file.write("."*232)
            file.write("\n\n\n")
            file.write("\t\t\t\t\t\t\t\t\t\t\t\t   THANK YOU FOR RENTING!")
    except:
        print("Error in writing to file")

#Function to display GUI for returning
def return_GUI():
    """
    Displays the returning interface of the system 
    Calls on function to get customer details
    Prints land details in tabular format
    Returns customer_name, customer_number
    """
    try:
        print("\n\n")
        print("\t\t\t\t\t\t\t\t\t\t\t\t    Techno Property Nepal")
        print("\n")
        print("\t\t\t\t\t\t\t\t\t Kausaltar,Bhaktapur | Phone no: 9808688665 | E-mail: technoproperty2070@gmail.com")
        print("\n\n")
        print("." *232)
        print("\t\t\t\t\t\t\t\t\t\t\t Before returning land please fill in the following details:")
        print("." *232)
        print("\n")
        #Calls on function to get customer details
        customer_name, customer_number=Operations.customer_details()
        print("." *232)
        print("Kitta                City                Direction               Anna                Price/mo                Availability")
        print("." *232)
        #Function to print land details in tabular format
        Operations.print_land_details()
        print("."*232)
        print("\n")
        return customer_name, customer_number;
    except:
        print("Error in return_GUI")    

#Function to display details of returned land
def returned_land_details(customer_name, customer_number):
    """
    Calls a function return_land() to get the list of returned land
    Displays customer details
    Displays the detail of the land the customer returned in tabular format along with fine
    Returns returned_land_list
    """
    try:
        returned_land_list = Operations.return_land()
        print("\n\n")
        print("\t\t\t\t\t\t\t\t\t\t\t\t    Techno Property Nepal")
        print("\n")
        print("\t\t\t\t\t\t\t\t\t Kausaltar,Bhaktapur | Phone no: 9808688665 | E-mail: technoproperty2070@gmail.com")
        print("\n\n")
        print("." *232)
        print("Customer Details:")
        print("." *232)
        print("Name of Customer: ", customer_name)
        print("Phone Number: ", customer_number)
        print("Date and time of Return: ", datetime.now())
        print("." * 232)
        print("\n")
        print("Details of the land you returned: ")
        print("." *232)
        print("Kitta                City                Direction               Anna                Price/mo                Rented Period                Returned After                Total Price              Fine")
        print("." *232)
        Operations.print_returned_land_details(returned_land_list)
        return returned_land_list
    except:
        print("Error in returned_land_details")

#function to print return invoice in unique text file
def print_return_invoice(customer_name, customer_number, returned_land_list):
    """
    Creates a unique text file
    Prints the Return Invoice in the text file
    """
    try:
        #Getting seconds
        time = str(datetime.now().second)
        #Opening text file with unique name
        with open (customer_name+customer_number+time+ ".txt" , "w") as file:
            file.write("\n\n")
            file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\tTechno Property Nepal")
            file.write("\n")
            file.write("\t\t\t\t\t\t\t\t\t\tKausaltar,Bhaktapur | Phone no: 9808688665 | E-mail: technoproperty2070@gmail.com")
            file.write("\n\n")
            file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t  RETURN INVOICE")
            file.write("\n\n\n")
            file.write("." *232)
            file.write("\n")
            file.write("Customer Details:")
            file.write("\n")
            file.write("." *232)
            file.write("\n\n")
            file.write("Name of Customer: " + customer_name)
            file.write("\n")
            file.write("Phone Number: " + customer_number)
            file.write("\n")
            file.write("Date and time of Return: " + str(datetime.now()))
            file.write("\n\n\n")
            file.write("Details of the land you returned: ")
            file.write("\n")
            file.write("." *232)
            file.write("\n")
            file.write("Kitta                     City                  Direction               Anna                Price/mo                Rented Period                Returned After                Total Price            Fine")
            file.write("\n")
            file.write("." *232)
            file.write("\n")
            total_price = 0
            total_fine = 0
            for property_details in returned_land_list:
                file.write(property_details[0]+"\t\t\t" + property_details[1] + "\t\t  " + property_details[2] + "\t\t\t" + property_details[3] + "\t\t     " + property_details[4] + "\t\t\t  " + property_details[5] + " \t\t\t\t" + property_details[6] + "\t\t\t  " + property_details[7] + "\t\t" + property_details[8])
                file.write("\n")
                total_price += int(property_details[7])
                total_fine += float(property_details[8])
            grand_total = total_price + total_fine
            file.write("\n")
            file.write("." * 232)
            file.write("\n\n")
            file.write("Total Price: Rs." + str(total_price))
            file.write("\n")
            file.write("Total Fine: Rs." + str(total_fine))
            file.write("\n")
            file.write("."*232)
            file.write("\n")
            file.write("Grand Total: Rs." + str(grand_total ))
            file.write("\n")
            file.write("."*232)
            file.write("\n\n\n")
            file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\tTHANK YOU FOR RETURNING!")
    except:
        print("Error in writing to file")