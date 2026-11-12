# from pathlib import Path
# import pandas as pd

# csv_path = Path(__file__).with_name('students.csv')
# df = pd.read_csv(csv_path)

# students = df[df['Role'] == 'Student'] 



# total = len(students)

# print(total)

message = 'M##t m# @t th# libr@ry @ft#r cl@$$. Bring th# $#cr#t m@p @nd dont t#ll @nyon#'

message = message.replace('#', 'e')
message = message.replace('@', 'a')
message = message.replace('$', 's')

print(message)