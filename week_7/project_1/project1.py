'''
Project 1 - Hotel Reservation System (Part 1) - Spring 2026  
Author: Collin Steele, collinsteele

This program simulates a hotel reservation system. The program presents an intial system for user interaction with basic input values. 
The program asks for value like, name, age, number of nights. Then the program computes and prints the total cost of the users stay.

I have neither given or received unauthorized assistance on this assignment.
Signed:  Collin Steele
'''
def main():
    ''' Runs the hotel reservation program's main menu.
    This function has no parameters and returns no value. '''

    print("Welcome to the Python hotel reservation system!\n")
    while True:
        print_menu()
        first_option = int(input("What is your selection? "))
        if first_option == 1: 
            print('\n--------------------------------------------------\n')
            create_reservation()
            print('--------------------------------------------------\n')
        elif first_option == 2:
            print('\nNow exiting program. Thanks for visiting!')
            break
        else:
            print('\nInvalid choice. Please try again.\n')
    
def calculate_discounted_rate(nightly_rate, age):
    ''' Computes and returns the discounted nightly rate using the
    nightly_rate and guest age values passed as parameters. '''

    if age < 22:
        return nightly_rate * 0.9
    elif age > 64:
        return nightly_rate * 0.85
    else:
        return nightly_rate



def calculate_reservation_total(nights, age):
    ''' Computes and returns the reservation total, including tax, using
    the number of nights and guest age values passed as parameters. '''

    nightly_rate = 120
    discounted_rate = calculate_discounted_rate(nightly_rate, age)
    subtotal = discounted_rate * nights
    total_cost = subtotal + subtotal * 0.06

    return total_cost


def create_reservation():
    ''' Gets reservation information from the user and prints the total cost.
    This function has no parameters and returns no value. '''

    print('Creating new reservation...')
    first_name = input("What is the guest's first name? ")
    last_name = input("What is the guest's last name? ")
    nights = int(input("How many nights? "))
    age = int(input("What is the age of the primary guest? "))

    total_cost = calculate_reservation_total(nights, age)
    print(f"\nThe cost of this reservation for {first_name} {last_name} is ${total_cost:.2f}.\n")


def print_menu():
    ''' Prints the hotel reservation menu options.
    This function has no parameters and returns no value. '''

    print("Select an option from the following menu:")
    print('1. Create a reservation')
    print('2. Exit the program\n')


if __name__ == '__main__':
    main()
