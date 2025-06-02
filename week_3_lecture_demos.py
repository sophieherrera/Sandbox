FILENAME = "guitars.csv"

with open(FILENAME, "r") as file:
    for line in file:
        name, year, price = line.strip().split(",")
        print(f"{name} ({year}) : ${float(price):,.2f}")
