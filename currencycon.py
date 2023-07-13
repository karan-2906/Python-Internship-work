c = open('C:\Coding\Internship\python\currencydata.txt','r')
lines = c.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter amount: "))
print("Available Options:")
[print(item) for item in currencyDict.keys()]
print("\nEnter the name of currency you want the convert amount")
currency = input("Please Enter Any one of the option: ")
print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency}")