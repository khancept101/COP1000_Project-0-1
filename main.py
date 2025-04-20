import os

VEHICLE_FILE = 'AllowedVehiclesList.txt'

def load_vehicles():
    if not os.path.exists(VEHICLE_FILE):
        open(VEHICLE_FILE, 'w').close()
    with open(VEHICLE_FILE, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def save_vehicles(vehicles):
    with open(VEHICLE_FILE, 'w') as f:
        for v in vehicles:
            f.write(v + '\n')

def display_banner():
    title = "AutoCountry Vehicle Finder v0.6"
    border = "*" * len(title)
    print(border)
    print(title)
    print(border)

def display_menu():
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit\n")

def list_vehicles(vehicles):
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for v in vehicles:
        print(v)
    print()

def search_vehicle(vehicles):
    print("*" *  len("AutoCountry Vehicle Finder v0.6"))
    name = input("Please Enter the full Vehicle name: ").strip()
    if name in vehicles:
        print(f"{name} is an authorized vehicle")
    else:
        print(f"{name} is not an authorized vehicle, if you received this in error please check the spelling and try again")
    print()

def add_vehicle(vehicles):
    print("*" *  len("AutoCountry Vehicle Finder v0.6"))
    name = input("Please Enter the full Vehicle name you would like to add: ").strip()
    if name and name not in vehicles:
        vehicles.append(name)
        save_vehicles(vehicles)
        print(f'You have added "{name}" as an authorized vehicle')
    else:
        print(f'"{name}" is already in the authorized list or invalid entry')
    print()

def delete_vehicle(vehicles):
    print("*" *  len("AutoCountry Vehicle Finder v0.6"))
    name = input("Please Enter the full Vehicle name you would like to REMOVE: ").strip()
    confirm = input(f'Are you sure you want to remove "{name}" from the Authorized Vehicles List? ').lower()
    if confirm in ("y","yes"):
        if name in vehicles:
            vehicles.remove(name)
            save_vehicles(vehicles)
            print(f'You have REMOVED "{name}" as an authorized vehicle')
        else:
            print(f'"{name}" was not found in the list')
    print()

def exit_app(vehicles):
    print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
    # Returning False will break the main loop
    return False

def main():
    vehicles = load_vehicles()

    # Map menu choices to the corresponding functions
    actions = {
        "1": list_vehicles,
        "2": search_vehicle,
        "3": add_vehicle,
        "4": delete_vehicle,
        "5": exit_app
    }

    running = True
    while running:
        display_banner()
        display_menu()
        choice = input("Enter choice: ").strip()
        action = actions.get(choice)
        if action:
            # Call the function; exit_app returns False to stop the loop
            result = action(vehicles)
            if choice == "5":
                running = False
        else:
            print("\nInvalid selection. Please enter 1, 2, 3, 4, or 5.\n")

if __name__ == '__main__':
    main()