#Weight converter
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