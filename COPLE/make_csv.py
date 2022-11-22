import csv
import os

csv_filename = 'cople_ortho.csv'
fields = ['Id', 'Proficiency', 'Text']
rows = []

path = r"/home/joao/Desktop/KUL/MThesis/COPLE/ortho"
dir_list = os.listdir(path)

for filename in dir_list:
    proficiency = filename[-2:]
    row = None
    with open(path + '/' + filename, 'r') as f:
        rows.append([filename[:-3], proficiency, f.read()])

with open(csv_filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
