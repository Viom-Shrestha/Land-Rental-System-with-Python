'''
Read.py file
for readinf data from text files
'''
#Reading and storing the land details in a dictionary
def read_data():
    """ 
    Reads the land data stored in text file
    Creates a dictionary (land_dictionary) and stores the data in that dictionary
    Returns land_dictionary
    """
    try:
        #Creating a dictionary to store the land details
        land_dictionary = {}
        kitta_no = 101
        #Readin from file
        with open("Land.txt","r") as file:
            for line in file:
                line = line.replace("\n"," ")
                line = line.replace(" ","")    
                land_dictionary[kitta_no]=(line.split(","))
                kitta_no += 1
        return(land_dictionary)
    except:
        print("File not found") 

