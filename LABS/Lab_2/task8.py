
conversion_rates = {
    ("dollar", "euro"): 0.92,
    ("dollar", "pkr"): 280,
    ("dollar", "inr"): 83,
    ("dollar", "yen"): 145,

    ("euro", "dollar"): 1.09,
    ("euro", "pkr"): 305,
    ("euro", "inr"): 90,
    ("euro", "yen"): 158,

    ("pkr", "dollar"): 0.0036,
    ("pkr", "euro"): 0.0033,
    ("pkr", "inr"): 0.30,
    ("pkr", "yen"): 0.52,

    ("inr", "dollar"): 0.012,
    ("inr", "euro"): 0.011,
    ("inr", "pkr"): 3.34,
    ("inr", "yen"): 1.75,

    ("yen", "dollar"): 0.0069,
    ("yen", "euro"): 0.0063,
    ("yen", "pkr"): 1.92,
    ("yen", "inr"): 0.57,
}

a = input("Which currency you want to convert from: ").lower()
b = int(input("Enter amount: "))
c = input("Which currency you want to convert to: ").lower()


rate = conversion_rates.get((a, c))
if rate:
    converted_amount = b * rate
    print(f"{b} {a} is equal to {converted_amount:.2f} {c}")
else:
    print("Conversion rate not available.")
