import os

VEHICLE_FILE = 'AllowedVehiclesList.txt'


def load_vehicles():
    # Ensure the file exists
    if not os.path.exists(VEHICLE_FILE):
        open(VEHICLE_FILE, 'w').close()
    vehicles = []
    with open(VEHICLE_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                vehicles.append(line)
    return vehicles

def save_vehicles(vehicles):
    with open(VEHICLE_FILE, 'w') as f:
        for v in vehicles:
            f.write(v + '\n')

def display_banner():
    title = "AutoCountry Vehicle Finder v0.5"
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
    print()
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for v in vehicles:
        print(v)
    print()

def search_vehicle(vehicles):
    border = "*" * len("AutoCountry Vehicle Finder v0.5")
    print(border)
    print("Please Enter the full Vehicle name:")
    name = input().strip()
    if name in vehicles:
        print(f"{name} is an authorized vehicle")
    else:
        print(f"{name} is not an authorized vehicle, if you received this in error please check the spelling and try again")
    print()

def add_vehicle(vehicles):
    border = "*" * len("AutoCountry Vehicle Finder v0.5")
    print(border)
    print("Please Enter the full Vehicle name you would like to add:")
    name = input().strip()
    if name and name not in vehicles:
        vehicles.append(name)
        save_vehicles(vehicles)
        print(f"You have added \"{name}\" as an authorized vehicle")
    else:
        print(f"\"{name}\" is already in the authorized list or invalid entry")
    print()

def delete_vehicle(vehicles):
    border = "*" * len("AutoCountry Vehicle Finder v0.5")
    print(border)
    print("Please Enter the full Vehicle name you would like to REMOVE:")
    name = input().strip()
    print(f"Are you sure you want to remove \"{name}\" from the Authorized Vehicles List?")
    confirm = input().strip().lower()
    if confirm in ("y", "yes"):
        if name in vehicles:
            vehicles.remove(name)
            save_vehicles(vehicles)
            print(f"You have REMOVED \"{name}\" as an authorized vehicle")
        else:
            print(f"\"{name}\" was not found in the list")
    print()

def main():
    vehicles = load_vehicles()

    while True:
        display_banner()
        display_menu()
        choice = input().strip()

        if choice == '1':
            list_vehicles(vehicles)

        elif choice == '2':
            search_vehicle(vehicles)

        elif choice == '3':
            add_vehicle(vehicles)

        elif choice == '4':
            delete_vehicle(vehicles)

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