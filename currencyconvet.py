import requests
 
class Currency_convertor:
    conversion_rates = {}
    def __init__(self, url):
        data = requests.get(url).json()
        # self.conversion_rates = data["conversion_rates"]
 
    # function to do a simple cross multiplication between
    # the amount and the conversion conversion_rates
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'INR' :
            amount = amount / self.conversion_rates[from_currency]
 
        # limiting the precision to 2 decimal places
        amount = round(amount * self.conversion_rates[to_currency], 2)
        print("{} {} = {} {}".format(initial_amount, from_currency, amount, to_currency))
 
# Driver code
if __name__ == "__main__":
 
    YOUR_ACCESS_KEY = 'Your accesss key'
    url = 'URL for conversion' 
    c = Currency_convertor(url)
    from_country = input("From Country: ")
    to_country = input("TO Country: ")
    amount = int(input("Amount: "))
 
    c.convert(from_country, to_country, amount)