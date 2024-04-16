# 3. 

# The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this application with the following features:

# It must have a login and validate the data; after the third failed attempt, it should be locked.
# The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
# There are 3 doctors for each specialty.
# The user can only book one appointment per specialist. An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty. As a developer, you can choose the doctors' names.
# The maximum limit for appointments, in general, is 3.
# Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours. As a developer, you can choose the hours.
# Display available specialists.
# The user can choose their preferred specialist.
# The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot.

credentials = {
    "user":"admin",
    "password": "admin"
}

specialties = {
    "General Medicine": ["Dr. Smith", "Dr. Johnson", "Dr. Williams"],
    "Emergency Care": ["Dr. Brown", "Dr. Davis", "Dr. Miller"],
    "Clinical Analysis": ["Dr. Wilson", "Dr. Moore", "Dr. Taylor"],
    "Cardiology": ["Dr. Anderson", "Dr. Thomas", "Dr. Jackson"],
    "Neurology": ["Dr. White", "Dr. Harris", "Dr. Martin"],
    "Nutrition": ["Dr. Thompson", "Dr. Garcia", "Dr. Martinez"],
    "Physiotherapy": ["Dr. Robinson", "Dr. Clark", "Dr. Rodriguez"],
    "Traumatology": ["Dr. Lewis", "Dr. Lee", "Dr. Walker"],
    "Internal Medicine": ["Dr. Hall", "Dr. Allen", "Dr. Young"]
}

specialties = {
    "General Medicine": {
        "doctors": ["Dr. Smith", "Dr. Johnson", "Dr. Williams"],
        "hours": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM", "4:00 PM"]
    },
    "Emergency Care": {
        "doctors": ["Dr. Brown", "Dr. Davis", "Dr. Miller"],
        "hours": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM", "4:00 PM"]
    },
    "Clinical Analysis": {
        "doctors": ["Dr. Wilson", "Dr. Moore", "Dr. Taylor"],
        "hours": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM", "4:00 PM"]
    },
    "Cardiology": {
        "doctors": ["Dr. Anderson", "Dr. Thomas", "Dr. Jackson"],
        "hours": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM", "4:00 PM"]
    },
    "Neurology": {
        "doctors": ["Dr. White", "Dr. Harris", "Dr. Martin"],
        "hours": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM", "4:00 PM"]
    },
    "Nutrition": {
        "doctors": ["Dr. Thompson", "Dr. Garcia", "Dr. Martinez"],
        "hours": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM", "4:00 PM"]
    },
    "Physiotherapy": {
        "doctors": ["Dr. Robinson", "Dr. Clark", "Dr. Rodriguez"],
        "hours": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM", "4:00 PM"]
    },
    "Traumatology": {
        "doctors": ["Dr. Lewis", "Dr. Lee", "Dr. Walker"],
        "hours": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM", "4:00 PM"]
    },
    "Internal Medicine": {
        "doctors": ["Dr. Hall", "Dr. Allen", "Dr. Young"],
        "hours": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM", "4:00 PM"]
    }
}

def login(credentials):
    attempts = 0
    while attempts < 3:
        user = input("Enter your username: ")
        password = input("Enter your password: ")
        if user == credentials["user"] and password == credentials["password"]:
            print("Login successful!")
            return True
        else:
            print("Invalid credentials. Please try again.")
            attempts += 1
    print("Maximum number of attempts reached. The system is locked.")
    return False

def display_specialties(specialties):
    print("Specialties:")
    for i, specialty in enumerate(specialties, start=1):
        print(f"{i}. {specialty}")

def display_doctors(specialties, specialty):
    print("Doctors:")
    for i, doctor in enumerate(specialties[specialty]["doctors"], start=1):
        print(f"{i}. {doctor}")

def display_doctors_hours(specialties, specialty, doctor):
    print("Hours:")
    for i, hour in enumerate(specialties[specialty]["hours"], start=1):
        print(f"{i}. {hour}")

def is_valid_appointment_hour(appointments, preferred_specialty, preferred_hour):
    for specialty, appointment in appointments.items():
        if appointment[1] == preferred_hour:
            print(f"You have already booked an appointment for {specialty} at {preferred_hour}.")
            return False
    return True



def book_appointment():
    appointments = {}
    while True:
        specialties_option = specialties.keys()
        display_specialties(specialties_option)
        try:
            choice = int(input("Enter the number corresponding to the specialty you want to book an appointment for: "))
            if choice < 1 or choice > len(specialties_option):
                raise ValueError("Invalid choice. Please enter a number corresponding to the displayed specialties.")
        except ValueError as e:
            print("Invalid choice. Please enter a number corresponding to the displayed specialties.")
            continue

        preferred_specialty = list(specialties_option)[choice - 1]
        if preferred_specialty in appointments:
            print("You have already booked an appointment for this specialty.")
            continue

        display_doctors(specialties, preferred_specialty)
        try:
            choice = int(input("Enter the number corresponding to the doctor you prefer: "))
            if choice < 1 or choice > len(specialties[preferred_specialty]["doctors"]):
                raise ValueError("Invalid choice. Please enter a number corresponding to the displayed doctors.")
        except ValueError as e:
            print("Invalid choice. Please enter a number corresponding to the displayed doctors.")
            continue

        preferred_doctor = specialties[preferred_specialty]["doctors"][choice - 1]
        
        display_doctors_hours(specialties, preferred_specialty, preferred_doctor)
        
        try:
            choice = int(input("Enter the number corresponding to the preferred hour: "))
            if choice < 1 or choice > len(specialties[preferred_specialty]["hours"]):
                raise ValueError("Invalid choice. Please enter a number corresponding to the displayed hours.")
        except ValueError as e:
            print("Invalid choice. Please enter a number corresponding to the displayed hours.")
            continue
        
        preferred_hour = specialties[preferred_specialty]["hours"][choice - 1]

        if not is_valid_appointment_hour(appointments, preferred_specialty, preferred_hour):
            continue

        appointments[preferred_specialty] = (preferred_doctor, preferred_hour)

        print(f"Appointment booked for {preferred_specialty} with {preferred_doctor} at {preferred_hour}")
        if len(appointments) == 3:
            print("You have reached the maximum number of appointments.")
            break
        another = input("Do you want to book another appointment? (yes/no): ")
        if another.lower() != "yes":
            break

def main():
    if not login(credentials):
        return
    book_appointment()

if __name__ == "__main__":
    main()
