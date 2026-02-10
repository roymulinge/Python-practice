#Weight converter

while True:
    try:
    
        quit = input("Press Q to quit program or enter to continue: ").upper()
        if quit == "Q":
            print("Run app to convert weight!")
            break
        weight = float(input("Enter your weight: "))
        unit = input("Enter unit of measurement(K for kgs, L for lbs): ").upper()

        if unit == "K":
            weight = weight * 2.205
            unit = "L"
        elif unit == "L":
            weight = weight / 2.205
            unit = "K"
        else:
            print("Invalid unit!")
            continue

        print(f"You weight is {round(weight, 1)} {unit}")
    except ValueError:
        print("Invalid weight! Try again")