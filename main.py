def display_banner():
    title = "AutoCountry Vehicle Finder v0.2"
    border = "*" * len(title)
    print(border)
    print(title)
    print(border)

def display_menu():
    print("Please Enter the following number below from the following menu:")
    print()
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. Exit")

def list_vehicles(vehicles):
    print()
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for v in vehicles:
        print(v)
    print()

def search_vehicle(vehicles):
    # Prompt for vehicle name and report authorization status
    title = "AutoCountry Vehicle Finder v0.2"
    border = "*" * len(title)
    print(border)
    print("Please Enter the full Vehicle name:")
    name = input().strip()
    if name in vehicles:
        print(f"{name} is an authorized vehicle")
    else:
        print(f"{name} is not an authorized vehicle, if you received this in error please check the spelling and try again")
    print()

def main():
    allowed_vehicles = [
        'Ford F-150',
        'Chevrolet Silverado',
        'Tesla CyberTruck',
        'Toyota Tundra',
        'Nissan Titan'
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
            print()
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break

        else:
            print()
            print("Invalid selection. Please enter 1, 2, or 3.")
            print()

if __name__ == '__main__':
    main()