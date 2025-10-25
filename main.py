import json

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def calculate_total(portfolio, rates):
    total = 0
    for coin, amount in portfolio.items():
        if coin in rates:
            total += amount * rates[coin]
        else:
            print(f"⚠️ No rate for {coin}")
    return total

def main():
    portfolio = load_json("data/portfolio.json")
    rates = load_json("data/rates.json")
    total = calculate_total(portfolio, rates)
    print(f"\n💼 Your total crypto portfolio is worth: ${total:,.2f} 💰\n")

if __name__ == "__main__":
    main()
