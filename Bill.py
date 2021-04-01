import math  # for using sqrt built in function

#user defined function to calculate BILL
def BILL(units):
    billamount = units * 0.025
    return billamount
    
#user defined function to calculate CITY TAX    
def CITYTAX(city, bill_output):
    if city == 'ibra':
        city_tax = 0.03 * bill_output
        return city_tax
    
    if city == 'muscat':
        city_tax = 0.07 * bill_output
        return city_tax
#function to print separation between input and output       
def pattern():
    print("#################################")

#input of the values
customer_name = input("Enter the customer name ")
address = input("Enter the address ")
city = input("Enter city ").lower()
units = int(input("Enter units "))

#calling function for seapration of input and output
pattern()

# function calling of user defined functions
bill_output = BILL(units)
citytax_output = CITYTAX(city, bill_output)
countryTax = math.sqrt(units)

# calculating total bill
total_bill = bill_output + citytax_output + countryTax
print("Total bill is ",total_bill)


