def display_banner():
    title = "AutoCountry Vehicle Finder v0.1"
    border = "*" * len(title)
    print(border)
    print(title)
    print(border)

def display_menu():
    print("Please Enter the following number below from the following menu:")
    print()
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")


def list_vehicles(vehicles):
    print()
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for v in vehicles:
        print(v)
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
            print()
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print()
            print("Invalid selection. Please enter 1 or 2.")
            print()

if __name__ == '__main__':
    main()
