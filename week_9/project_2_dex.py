'''
Project 2 - Hotel Reservation System (Part 2) - Spring 2026
Author: Collin Steele, collinsteele

This program manages hotel reservations for several room types. It can create,
display, save, and load reservations while calculating discounts and taxes.

I have neither given or received unauthorized assistance on this assignment.
Signed: Collin Steele
'''


def main():
    ''' Runs the hotel reservation program and manages the master reservation
    list. This function has no parameters and returns no value. '''

    all_reservations = []

    print("Welcome to the Python hotel reservation system!\n")
    while True:
        print_menu()
        menu_choice = int(input("What is your selection? "))

        if menu_choice == 1:
            print('\n--------------------------------------------------\n')
            reservation = create_reservation()
            all_reservations.append(reservation)
            print('--------------------------------------------------\n')
        elif menu_choice == 2:
            view_reservations(all_reservations)
        elif menu_choice == 3:
            save_reservations(all_reservations)
        elif menu_choice == 4:
            all_reservations = load_reservations()
        elif menu_choice == 5:
            print('\nNow exiting program. Thanks for visiting!')
            break
        else:
            print('\nInvalid choice. Please try again.\n')


def calculate_discounted_rate(nightly_rate, age):
    ''' Computes and returns the discounted nightly rate using the nightly_rate
    and guest age values passed as parameters. '''

    if age < 22:
        return nightly_rate * 0.9
    elif age > 64:
        return nightly_rate * 0.85
    else:
        return nightly_rate


def determine_standard_rate(room_type):
    ''' Returns the standard nightly rate for the room_type passed as a
    parameter. '''

    room_rates = {
        'single': 100.00,
        'double': 125.00,
        'king': 150.00,
        'suite': 200.00
    }
    return room_rates[room_type]


def calculate_reservation_total(room_type, nights, age):
    ''' Computes and returns the reservation total, including any age discount
    and tax, using the room_type, nights, and age parameters. '''

    standard_rate = determine_standard_rate(room_type)
    discounted_rate = calculate_discounted_rate(standard_rate, age)
    subtotal = discounted_rate * nights
    total_cost = subtotal + subtotal * 0.06

    return total_cost


def create_reservation():
    ''' Gets reservation information from the user, prints the total cost, and
    returns the reservation information in a list. This function has no
    parameters. '''

    print('Creating new reservation...')
    first_name = input("What is the guest's first name? ")
    last_name = input("What is the guest's last name? ")
    room_type = input("What type of room (single, double, king, suite)? ")

    valid_room_types = ['single', 'double', 'king', 'suite']
    while room_type not in valid_room_types:
        room_type = input("Invalid room type. Please reenter: ")

    nights = int(input("How many nights? "))
    age = int(input("What is the age of the primary guest? "))

    total_cost = calculate_reservation_total(room_type, nights, age)
    print(f"\nThe cost of this reservation for {first_name} {last_name} is ${total_cost:.2f}.\n")

    reservation = [first_name, last_name, room_type, nights, age]
    return reservation


def print_menu():
    ''' Prints the five hotel reservation menu options. This function has no
    parameters and returns no value. '''

    print("Select an option from the following menu:")
    print('1. Create a reservation')
    print('2. View reservations')
    print('3. Save reservations')
    print('4. Load reservations')
    print('5. Exit the program\n')


def view_reservations(all_reservations):
    ''' Prints every reservation in the all_reservations list. This function
    returns no value. '''

    print('Current reservations:\n')
    for reservation in all_reservations:
        print(f'Guest: {reservation[0]} {reservation[1]} (age {reservation[4]})')
        print(f'Room type: {reservation[2]}')
        print(f'Number of nights: {reservation[3]}\n')


def save_reservations(all_reservations):
    ''' Saves the all_reservations list to reservations.txt. This function
    returns no value. '''

    try:
        output_file = open('reservations.txt', 'w')
        for reservation in all_reservations:
            reservation_line = (reservation[0] + ' ' + reservation[1] + ' '
                                + reservation[2] + ' ' + str(reservation[3])
                                + ' ' + str(reservation[4]) + '\n')
            output_file.write(reservation_line)
        output_file.close()
        print('Data saved successfully.')
    except:
        print('There was an error saving the data.')


def load_reservations():
    ''' Loads and returns reservations from reservations.txt in a list. This
    function has no parameters. '''

    all_reservations = []

    try:
        input_file = open('reservations.txt', 'r')
        for line in input_file:
            reservation = line.split()
            reservation[3] = int(reservation[3])
            reservation[4] = int(reservation[4])
            all_reservations.append(reservation)
        input_file.close()
        print('Data loaded successfully')
        return all_reservations
    except:
        print('There was an error loading the data.')
        return []


# Call main like this to keep Web-CAT happy:
if __name__ == '__main__':
    main()
