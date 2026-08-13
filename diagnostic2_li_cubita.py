def  calculate_fuel(cargo_weight):
    base_ship_weight = 50000
    total_weight = base_ship_weight + cargo_weight
    fuel_needed = total_weight * 3
    return fuel_needed
total_cargo_weight = 0
while total_cargo_weight <= 10000:
    cargo_item = input("Enter cargo item (satellite, rover, supplies) or type 'launch' to finish: ")
    if cargo_item == "launch":
        break
    elif cargo_item == "satellite":
        print("Satellite added to cargo.")
        total_cargo_weight += 1000
    elif cargo_item == "rover":
        print("Rover added to cargo.")
        total_cargo_weight += 2500
    elif cargo_item == "supplies":
        print("Supplies added to cargo.")
        total_cargo_weight += 500
    else:
        print(f"{cargo_item} is not approved for the mission.")

    if total_cargo_weight > 10000:
        print("MAX WEIGHT REACHED")
        break
    





