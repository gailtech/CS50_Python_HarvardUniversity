def main():
    total_price = 0
    prices = price()
    while True:
        try:
            item = input("Item: ").title()
            if item in prices:
                total_price += prices[item]
                print(f"Total: ${total_price:.2f}")

        except EOFError:
            print()
            break

def price():
    prices = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    return prices


main()
