import csv

def load_currency_rates(filename='currency.csv'):
    currency_rates = {}
    try:
        with open(filename, mode='r', encoding='utf-8-sig', errors='replace') as file:
            reader = csv.reader(file)
            next(reader, None)  
            for row in reader:
                if len(row) < 2:  
                    continue  

                currency = row[0].strip().upper()  
                rate = row[-1]  

                try:
                    currency_rates[currency] = float(rate)
                except ValueError:
                    print(f"Skipping invalid rate value: {row}")  

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"Unexpected error while loading currency rates: {e}")
        return None
    
    return currency_rates

def convert_currency(amount, currency, rates):
    currency = currency.upper()
    if rates and currency in rates:
        return amount * rates[currency]
    else:
        print("Currency not found in the exchange rates.")
        return None

def main():
    filename = 'currency.csv'
    currency_rates = load_currency_rates(filename)
    
    if not currency_rates:
        return  
    
    try:
        usd_amount = float(input("How much USD do you have? "))
        target_currency = input("What currency you want to have? ").strip().upper()
        
        converted_amount = convert_currency(usd_amount, target_currency, currency_rates)
        
        if converted_amount is not None:
            print(f"\nDollar: {usd_amount} USD")
            print(f"{target_currency}: {converted_amount:.9f}")
    except ValueError:
        print("Invalid input. Please enter a valid number for USD.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
