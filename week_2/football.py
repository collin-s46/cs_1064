from pathlib import Path
import pandas as pd

csv_path = Path(__file__).with_name('students.csv')
df = pd.read_csv(csv_path)

students = df[df['Role'] == 'Student'] 

csv_path_2 = Path(__file__).with_name('fb_roster.csv')
df_2 = pd.read_csv(csv_path_2)

#players = df_2['Name']

players_names = set(df_2['Name'].dropna())
student_names = set(students['Name'].dropna())

# for i in players_names:
#     suspect = i
#     for k in student_names:
#         if suspect == k:
#             print("FOUND! Name: " + suspect)

# players_names = df_2[df_2['Class'].isin([
#     'Freshman',
#     'Sophmore',
#     'Redshirt Freshman',
#     'Redshirt Sophmore'
# ])]

if "T-Ron" in players_names:
    print("FOUND!")


    

# if (df_2[df_2['Class'] == 'Junior', 'Senior', 'Redshirt Junior']):
#     players.remove()



#print(players)