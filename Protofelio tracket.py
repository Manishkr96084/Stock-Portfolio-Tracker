import csv

def load_stock_prices(filename):
    stock_prices = {}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            stock = row['stock'].strip().upper()
            price = float(row['price'].strip())
            stock_prices[stock] = price

    return stock_prices


def main():
    stock_prices = load_stock_prices("stock_prices.csv")

    while True:
        stock_name = input("\nEnter stock name (or type STOP to exit): ").strip().upper()

        if stock_name == "STOP":
            print("👋 Program stopped.")
            break

        if stock_name in stock_prices:
            print(f"💰 Price of {stock_name} is ${stock_prices[stock_name]}")
        else:
            print("❌ Stock not found. Try again.")


if __name__ == "__main__":
    main()
