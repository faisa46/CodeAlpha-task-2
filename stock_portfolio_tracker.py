import csv

# Example prices are fixed sample values, not live market prices.
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

def track_portfolio():
    portfolio = []
    total_investment = 0

    print("=== STOCK PORTFOLIO TRACKER ===")
    print("Available stocks:", ", ".join(STOCK_PRICES))
    print("Enter 'done' when you have finished.")

    while True:
        stock = input("\\nEnter stock symbol: ").upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not found. Choose a symbol from the list.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a whole number for quantity.")
            continue

        price = STOCK_PRICES[stock]
        value = price * quantity
        total_investment += value

        portfolio.append({
            "Stock": stock,
            "Quantity": quantity,
            "Price": price,
            "Total": value
        })

        print(f"{stock}: {quantity} x ${price} = ${value}")

    if not portfolio:
        print("\\nNo stocks were added.")
        return

    print("\\n--- PORTFOLIO SUMMARY ---")
    for item in portfolio:
        print(
            f"{item['Stock']}: {item['Quantity']} shares x "
            f"${item['Price']} = ${item['Total']}"
        )

    print(f"Total investment: ${total_investment}")

    with open("portfolio_summary.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["Stock", "Quantity", "Price", "Total"]
        )
        writer.writeheader()
        writer.writerows(portfolio)

    print("Saved details to portfolio_summary.csv")

if __name__ == "__main__":
    track_portfolio()
