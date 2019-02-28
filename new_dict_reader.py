#DictReader prints out everything according to it key
#Easier to query
import csv

with open('result.csv', 'r') as csv_file:
      csv_reader = csv.DictReader(csv_file)

      for line in csv_reader:
            if line['student_number'] == 'S2135/0001':
                  print(f"You got {line['div']} {line['div_point']}")
