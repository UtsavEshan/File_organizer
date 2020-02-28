import os
import shutil


files = os.listdir('Desktop')
phrases = ['physics', 'chemistry', 'biology',
           'french', 'ICT', 'maths', 'english']

for phrase in phrases:
    for file in files:
        if 'py' in file:
            shutil.move(f'Desktop/{file}', f'Desktop/Coding/Python')
        elif phrase in file:
            shutil.move(f'Desktop/{file}', f'Desktop/school/Subjects/{phrase}')
            print(f'File: {file} and the phrase is {phrase}')
