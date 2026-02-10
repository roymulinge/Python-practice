#Weight converter

while True:
    quit = input("Press Q to quit program or enter to continue: ")
    if quit == "Q":
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

    print(f"You weight is {weight} {unit}")