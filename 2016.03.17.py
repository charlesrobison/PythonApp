import DataProcessor, Persons, Customers

print("Test the DataProcessor.File class")
objDP = DataProcessor.File()
objDP.FileName = "Test.txt"
objDP.TextData = "This is a test"
strMessage = objDP.SaveData()
print(strMessage)

print("\n Test the DataProcessor.Database class")
try:
    print("Trying to create an object, but the class is not ready")
    objDP = DataProcessor.Database()
except:
    print("This should fail")


print("\n Test the Persons.Person class")
objP = Persons.Person()
objP.FirstName = "Bob"
objP.LastName = "Smith"
print(objP.ToString())

print("\n Test the Customers.Customer class")
objE = Customers.Customer()
objE.Id = 1
objE.FirstName = "Bob"
objE.LastName = "Smith"
print(objE.ToString())


print("\n Test the Customer.CustomerList class")
objEL = Customers.CustomerList()
try:
    print("Trying the wrong object type")
    objEL.AddCustomer(objP)
except:
    print("This should fail")

try:
    objEL.AddCustomer(objE)
    print("Trying the correct object type")
    print(objEL.ToString())
except:
    print("This should work")
