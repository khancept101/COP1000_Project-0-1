def display_banner():
    title = "AutoCountry Vehicle Finder v0.4"
    border = "*" * len(title)
    print(border)
    print(title)
    print(border)

def display_menu():
    print("Please Enter the following number below from the following menu:")
    print()
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")

def list_vehicles(vehicles):
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for v in vehicles:
        print(v)
    print()

def search_vehicle(vehicles):
    border = "*" * len("AutoCountry Vehicle Finder v0.4")
    print(border)
    print("Please Enter the full Vehicle name:")
    name = input().strip()
    if name in vehicles:
        print(f"{name} is an authorized vehicle")
    else:
        print(f"{name} is not an authorized vehicle, if you received this in error please check the spelling and try again")
    print()

def add_vehicle(vehicles):
    border = "*" * len("AutoCountry Vehicle Finder v0.4")
    print(border)
    print("Please Enter the full Vehicle name you would like to add:")
    name = input().strip()
    vehicles.append(name)
    print(f"You have added \"{name}\" as an authorized vehicle")
    print()

def delete_vehicle(vehicles):
    border = "*" * len("AutoCountry Vehicle Finder v0.4")
    print(border)
    print("Please Enter the full Vehicle name you would like to REMOVE:")
    name = input().strip()
    print(f"Are you sure you want to remove \"{name}\" from the Authorized Vehicles List?")
    confirm = input().strip().lower()
    if confirm in ("y", "yes"):
        if name in vehicles:
            vehicles.remove(name)
        print(f"You have REMOVED \"{name}\" as an authorized vehicle")
    print()

def main():
    allowed_vehicles = [
        'Ford F-150',
        'Chevrolet Silverado',
        'Tesla CyberTruck',
        'Toyota Tundra',
        'Nissan Titan',
        'Rivian R1T',
        'Ram 1500'
    ]

    while True:
        display_banner()
        display_menu()
        choice = input().strip()

        if choice == '1':
            list_vehicles(allowed_vehicles)

        elif choice == '2':
            search_vehicle(allowed_vehicles)

        elif choice == '3':
            add_vehicle(allowed_vehicles)

        elif choice == '4':
            delete_vehicle(allowed_vehicles)

        elif choice == '5':
            print()
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break

        else:
            print()
            print("Invalid selection. Please enter 1, 2, 3, 4, or 5.")
            print()

if __name__ == '__main__':
    main()