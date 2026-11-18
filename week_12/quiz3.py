#1
print('Kirk\nSpock\nMcCoy')

#2
my_nums = [1, 2, 3, 4, 5, 6]

new_list = [12 * i for i in my_nums]
print(new_list)

#3
products = {
    'XJ247': 'Milk',
    'CS1064': 'Bread'
}
#they do the same thing
for i in products:
    if i == 'XJ247':
        print(products[i])
if 'XJ247' in products:
    print(products['XJ247'])

#4
first_names = ['Bob', 'Jim', 'Joe', 'John', 'Bob', 'Joe', 'Bob']
count_names = {}
for i in first_names:
    count_names[i] = count_names.get(i, 0) + 1

print(count_names)


#5
needed_tools = {'hammer', 'saw', 'wrench'}
tools_on_hand = {'hammer', 'saw', 'wrench'}

if needed_tools.issubset(tools_on_hand):
    print('Ready to work!')

#6
class Animal:
    def __init__(self, animal_type):
        self.animal_type = animal_type
    

pet = Animal('dog')


#7
class Course:
    def __init__(self, title, department):
        self.title = title
        self.department = department

    def get_department(self):
        return self.department

