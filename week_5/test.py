#Write code that assigns the string 'hullaballoo' to the variable funny_word and then prints one output line stating 'The funny word is' followed by the value of the variable.

# funny_word = 'hullaballoo'

# print('The funny word is', funny_word)

#Assume the variable cups contains an integer representing a certain number of cups (the liquid measure).
# There are 16 cups in a gallon. 
# Write code that computes and prints the equivalent number of gallons and leftover cups.

# cups = 43

# gallons = cups // 16

# leftover_cups = cups % 16

# print('Gallons:', gallons)
# print('Leftover cups:', leftover_cups)

#Write code that sets the value of the variable product_id to the contents of the variables product_name (a string) 
#concatenated with the product_num (an integer), separated by a dash. 
#For example, if the product_name is 'NetGear' and the product_num is 9204, 
# the string assigned to product_id would be 'NetGear-9204'. 
# Assume that product_name and product_num have already been initialized.

# product_name = 'NetGear'
# product_num = 9204

# product_id = product_name + '-' +  str(product_num)

# print(product_id)

#Write a function called compute_side that accepts an integer parameter representing the area of a square and 
# returns the the length of one side of the square. 
# The length of a side is the square root of the area. 
# You can assume that any necessary library modules have been imported.
# import math

# def compute_side(area_of_square):
#     return math.sqrt(area_of_square)


# print(compute_side(25))

#Write code that reads the number of people at a party from the user,
# then prints that value doubled. 

# people = int(input('How many people at a party: '))

# print(people * 2)

#Write code that prints the shorter of two titles that are stored in the variables title1 and title2. 
# If both titles are equal in length, print the value of title2. 
# Assume that both variables have already been given values.

# title1 = 'Lord of The Rings'
# title2 = 'Star Wars'

# if len(title1) < len(title2):
#     print(title1)

# else: 
#     print(title2)


#Write a function called check_height that accepts a numeric height value as a parameter 
# and returns the string 'short' if it's below 100, 
# 'tall' if it's above 500, and 'in range' if it's in between (inclusive).

def check_height(height):
    if height < 100:
        return 'short'
    elif height > 500:
        return 'tall'
    else:
        return 'in range'

































