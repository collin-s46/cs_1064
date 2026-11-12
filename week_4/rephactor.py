# check = input("Enter word: ")
#################################This is from Quick Check
# left = 0
# right = len(check) - 1
# palindrome = True

# while left < right and palindrome:
#     if check[left] == check[right]:
#         left += 1
#         right -= 1
#     else:
#         palindrome = False

# if palindrome: 
#     print(f'"{check}" is a palindrome!')
# else:
#     print(f'"{check}" is not a palindrome')

#####################
#####Problem #1
#####################
# def compute_pay(wage, hours):
#     wage = float(wage)
#     hours = float(hours)

#     if hours > 40:
#         regular_pay = wage * 40
#         overtime = hours - 40
#         overtime_pay = wage * 1.5 * overtime
#         pay = regular_pay + overtime_pay
#     else:
#         pay = (wage * hours)

#     pay -= pay * 0.3
#     #pay -= pay * 0.1
    
    

#     return round(pay, 2)

# print(compute_pay(12.25, 45))

####################
######Problem 2
####################
# total = 0
# for i in range(500, 600):
#     total += i

# print(total)

####################
######Problem 3
####################

# even_sum = 0
# for i in range(2, 101):
#     if i % 2 == 0:
#         even_sum += i
# print(even_sum)

####################
######Problem 4
####################

# sum_select = 0
# for i in range(100, 401):
#     if i % 5 == 0 or i % 7 == 0:
#         sum_select += i
# print(sum_select)

####################
######Problem 5
####################

# word = 'python'
# double_word = ''
# for i in word:
    # double_word += i * 2
# print(double_word)

####################
######Problem 6
####################

# def is_prime(num):
    # if num < 2:
        # return False
    # for i in range(2, int(num**0.5) + 1):
        # if num % i == 0:
            # return False
    # return True
# 
# print(is_prime(33))
# 
####################
######Problem 7
####################

#the number of corresponding characters that do not match

# def hamming_distance(str1, str2):
#     total = 0
#     if len(str1) == len(str2):
#         for i in range(len(str1)):
#             if str1[i] != str2[i]: 
#                 total += 1
#     return total
                
# print(hamming_distance('piecey', 'peacee'))
