# 5. Turkish Airlines has just launched an offer to travel among the following destinations: Turkey, Greece, Lebanon, Spain, and Portugal. Develop an algorithm with the following characteristics:
# It must have a login and validate the data; after the third failed attempt, it should be locked.
# The user must choose the origin country and the destination country, the flight date, and the condition: Economy or First Class.
# The user must choose if they want to check an additional piece of luggage into the hold.
# Hand luggage is free of charge.
# The user must purchase both the outbound and return tickets.
# The user can choose their preferred meal: Regular, Vegetarian, Kosher.
# The program must collect the following data: Name, country of origin, passport, and destination country.
# Upon completing the process, the system will display everything the user has previously chosen along with their information. 
# The system will provide the option to confirm the reservation or cancel it. If the user chooses YES, a confirmation message will appear. If not, it will return to the main menu.

credentials = {
    "user":"admin",
    "password":"admin"
}

countries = {
    "Turkey": {
        "destinations": ["Greece", "Lebanon", "Spain", "Portugal"]
    },
    "Greece": {
        "destinations": ["Turkey", "Lebanon", "Spain", "Portugal"]
    },
    "Lebanon": {
        "destinations": ["Turkey", "Greece", "Spain", "Portugal"]
    },
    "Spain": {
        "destinations": ["Turkey", "Greece", "Lebanon", "Portugal"]
    },
    "Portugal": {
        "destinations": ["Turkey", "Greece", "Lebanon", "Spain"]
    }
}

meals = ["Regular", "Vegetarian", "Kosher"]

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
    print("1. Book a flight")
    print("2. Exit")

def book_flight():
    print("Book a flight:")
    print("Origin countries:")
    for i, country in enumerate(countries.keys(), start=1):
        print(f"{i}. {country}")
    try:
        origin = int(input("Enter the number corresponding to the origin country: "))
        if origin < 1 or origin > len(countries):
            raise ValueError("Invalid choice. Please enter a number corresponding to the displayed countries.")
    except ValueError as e:
        print("Invalid choice. Please enter a number corresponding to the displayed countries.")
        return

    origin_country = list(countries.keys())[origin - 1]
    print(f"Destination countries from {origin_country}:")
    for i, destination in enumerate(countries[origin_country]["destinations"], start=1):
        print(f"{i}. {destination}")
    try:
        destination = int(input("Enter the number corresponding to the destination country: "))
        if destination < 1 or destination > len(countries[origin_country]["destinations"]):
            raise ValueError("Invalid choice. Please enter a number corresponding to the displayed destinations.")
    except ValueError as e:
        print("Invalid choice. Please enter a number corresponding to the displayed destinations.")
        return

    destination_country = countries[origin_country]["destinations"][destination - 1]
    flight_date = input("Enter the flight date (dd/mm/yyyy): ")
    condition = input("Enter the condition (Economy or First Class): ")
    luggage = input("Do you want to check an additional piece of luggage into the hold? (yes/no): ")
    meal = input("Choose your preferred meal (Regular, Vegetarian, Kosher): ")
    name = input("Enter your name: ")
    country_of_origin = input("Enter your country of origin: ")
    passport = input("Enter your passport: ")

    print("Summary:")
    print(f"Origin country: {origin_country}")
    print(f"Destination country: {destination_country}")
    print(f"Flight date: {flight_date}")
    print(f"Condition: {condition}")
    print(f"Luggage: {luggage}")
    print(f"Meal: {meal}")
    print(f"Name: {name}")
    print(f"Country of origin: {country_of_origin}")
    print(f"Passport: {passport}")

    confirmation = input("Do you want to confirm the reservation? (yes/no): ")
    if confirmation == "yes":
        print("Reservation confirmed.")
    else:
        print("Reservation canceled.")

def main():
    if not login():
        return
    while True:
        display_main_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > 1:
                raise ValueError("Invalid choice. Please enter a number corresponding to the displayed options.")
        except ValueError as e:
            print("Invalid choice. Please enter a number corresponding to the displayed options.")
            continue

        if choice == 1:
            book_flight()
            break

        if choice == 2:
            break

if __name__ == "__main__":
    main()

