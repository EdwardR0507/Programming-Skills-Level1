# 4. The RH Hotels chain has hired you to design the booking algorithm for their mobile application:

# Login; it should be locked after the third failed attempt.
# The RH Hotels chain exists in 5 countries: Spain, France, Portugal, Italy, and Germany.
# Each country has its own hotels located in: Madrid, Barcelona, Valencia, Munich, Berlin, Rome, Milan, Paris, Marseille, Madeira, Lisbon, and Porto.
# All hotels have 24 rooms each: 6 VIP suites, 3 single rooms, 6 double rooms, 6 group rooms, and 3 luxury suites.
# The user can make reservations at any time of the year and at any hour, and book as many rooms as desired.
# Single rooms are priced at $100 per night, double rooms at $200 per night, group rooms at $350 per night, VIP suites at $450 per night, and luxury suites at $550 per night, applicable at any time of the year.
# The algorithm functions as follows: Login, choose country, choose city, choose room type, select the number of nights, collect user data (name, surname, ID/passport), 
# print the total cost, and if the user agrees, print a confirmation message for the reservation. If not, return to the main menu.
credentials = {
    "user":"admin",
    "password":"admin"
}

countries = {
    "Spain": {
        "hotels": ["Madrid", "Barcelona", "Valencia"]
    },
    "France": {
        "hotels": ["Paris", "Marseille"]
    },
    "Portugal": {
        "hotels": ["Madeira", "Lisbon", "Porto"]
    },
    "Italy": {
        "hotels": ["Rome", "Milan"]
    },
    "Germany": {
        "hotels": ["Munich", "Berlin"]
    }
}

rooms = {
    "VIP Suite": 450,
    "Single Room": 100,
    "Double Room": 200,
    "Group Room": 350,
    "Luxury Suite": 550
}


def login():
    attempts = 0
    while attempts < 3:
        user = input("Enter your username: ")
        password = input("Enter your password: ")
        if user == credentials["user"] and password == credentials["password"]:
            print("Login successful.")
            break
        else:
            print("Invalid credentials. Please try again.")
            attempts += 1
    else:
        print("You have exceeded the maximum number of attempts. The system will now lock.")
        return False
    return True

def display_main_menu():
    print("Main menu:")
    print("1. Book a hotel")
    print("2. View reservations")
    print("3. Exit")
    

def choose_country():
    print("Countries:")
    for i, country in enumerate(countries.keys(), start=1):
        print(f"{i}. {country}")
    while True:
        try:
            choice = int(input("Enter the number corresponding to the country you want to book a hotel in: "))
            if choice < 1 or choice > len(countries):
                raise ValueError("Invalid choice. Please enter a number corresponding to the displayed countries.")
        except ValueError as e:
            print("Invalid choice. Please enter a number corresponding to the displayed countries.")
            continue
        return list(countries.keys())[choice - 1]


def choose_city(country):
    print("Cities:")
    for i, city in enumerate(countries[country]["hotels"], start=1):
        print(f"{i}. {city}")
    while True:
        try:
            choice = int(input("Enter the number corresponding to the city you want to book a hotel in: "))
            if choice < 1 or choice > len(countries[country]["hotels"]):
                raise ValueError("Invalid choice. Please enter a number corresponding to the displayed cities.")
        except ValueError as e:
            print("Invalid choice. Please enter a number corresponding to the displayed cities.")
            continue
        return countries[country]["hotels"][choice - 1]


def choose_room():
    print("Room types:")
    for i, room in enumerate(rooms.keys(), start=1):
        print(f"{i}. {room}")
    while True:
        try:
            choice = int(input("Enter the number corresponding to the room type you want to book: "))
            if choice < 1 or choice > len(rooms):
                raise ValueError("Invalid choice. Please enter a number corresponding to the displayed room types.")
        except ValueError as e:
            print("Invalid choice. Please enter a number corresponding to the displayed room types.")
            continue
        return list(rooms.keys())[choice - 1]

def select_nights():
    while True:
        try:
            nights = int(input("Enter the number of nights you want to book: "))
            if nights < 1:
                raise ValueError("Invalid choice. Please enter a positive number of nights.")
        except ValueError as e:
            print("Invalid choice. Please enter a positive number of nights.")
            continue
        return nights

def collect_user_data():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    id_number = input("Enter your ID/passport number: ")
    return name, surname, id_number

def calculate_total_cost(room, nights):
    return rooms[room] * nights

def confirm_reservation():
    while True:
        choice = input("Do you want to confirm your reservation? (yes/no): ")
        if choice.lower() == "yes":
            print("Your reservation has been confirmed.")
            return True
            break
        elif choice.lower() == "no":
            print("Your reservation has been cancelled.")
            return False
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            continue

def display_reservation(country, city, room, nights, name, surname, id_number, total_cost):
    print(f"Country: {country}")
    print(f"City: {city}")
    print(f"Room type: {room}")
    print(f"Number of nights: {nights}")
    print(f"Name: {name}")
    print(f"Surname: {surname}")
    print(f"ID/Passport number: {id_number}")
    print(f"Total cost: ${total_cost}")

def book_hotel():
    if not login():
        return
    while True:
        display_main_menu()
        try:
            choice = int(input("Enter the number corresponding to the action you want to perform: "))
            if choice < 1 or choice > 3:
                raise ValueError("Invalid choice. Please enter a number corresponding to the displayed actions.")
        except ValueError as e:
            print("Invalid choice. Please enter a number corresponding to the displayed actions.")
            continue
        if choice == 1:
            country = choose_country()
            city = choose_city(country)
            room = choose_room()
            nights = select_nights()
            name, surname, id_number = collect_user_data()
            total_cost = calculate_total_cost(room, nights)
            display_reservation(country, city, room, nights, name, surname, id_number, total_cost)
            confirmation = confirm_reservation()
            if not confirmation:
                continue
        elif choice == 2:
            print("No reservations have been made yet.")
        elif choice == 3:
            print("Exiting the application.")
            break
    


def main():
    book_hotel()

if __name__ == "__main__":
    main()