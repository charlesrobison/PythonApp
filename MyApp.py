#-------------------------------------------------#
# Title: CustomersApp
# Dev:   Charles Robison
# Date:  2016.03.23
# Desc: This application manages customer data
# ChangeLog: (Who, When, What)
#
#-------------------------------------------------#
if __name__ == "__main__":
    import DataProcessor, Customers
else:
    raise Exception("This file was not created to be imported")

#-- Data --#
# declare variables and constants
objE = None #an Customer object
intId = 0 #an CustomerId
gIntLastId = 0 #Records the last CustomerId used in the client
strFirstName = "" #an Customer's first name
strLastName = "" #an Customer's last name
strInput = "" #temporary user input

#-- Processing --#
#perform tasks
def ProcessNewCustomerData(Id, FirstName, LastName):
    try:
        #Create Customer object
        objE = Customers.Customer()
        objE.Id = Id
        objE.FirstName = FirstName
        objE.LastName = LastName
        Customers.CustomerList.AddCustomer(objE)
    except Exception as e:
        print(e)

def SaveDataToFile():
    try:
        objF = DataProcessor.File()
        objF.FileName = "CustomerData.txt"
        objF.TextData = Customers.CustomerList.ToString()
        print("Reached here")
        objF.SaveData()
    except Exception as e:
        print(e)
#-- Presentation (I/O) --#
#__main__

#get user input
strUserInput = ""
while(True):
  strUserInput = input("Would you like to add Customer data? (y/n)")
  if(strUserInput == "y"):
      #Get Customer Id from the User
      intId = int(input("Enter an Customer Id (Last id was " + str(gIntLastId) + "): "))
      gIntLastId = intId
      #Get Customer FirstName from the User
      strFirstName = str(input("Enter an Customer First Name: "))
      #Get Customer LastName from the User
      strLastName = str(input("Enter an Customer Last Name: ") )
      #Process input
      ProcessNewCustomerData(intId, strFirstName, strLastName)
  else:
      break

#send program output
print("The Current Data is: ")
print("------------------------")
print(Customers.CustomerList.ToString())

#get user input
strInput = input("Would you like to save this data to the dat file?(y/n)")
if(strInput == "y"):
    SaveDataToFile()
    #send program output
    print("data saved in file")
else:
    print("data was not saved")

print("This application has ended. Thank you!")
