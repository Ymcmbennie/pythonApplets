import csv

with open('result.csv', 'r') as csv_file:
      csv_reader = csv.reader(csv_file)


      #next(csv_reader) to skip header

      #to rewrite file with -
      with open('new_results.csv', 'w') as new_file:
            fieldnames=['div', 'div_points', 'div_grades', 'stats', 'school_name']
            
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
            
            line = [('div','1'),
                    ('div_points','25'), ('div_grades',"ENGL - 'D'   PHY - 'F'   CHEM - 'F'"),
                    ('stats','DIV-I = 1;  DIV-II = 3;  DIV-III = 18;  DIV-IV = 85;  DIV-0 = 26'),
                    ('school_name','P0712 BARIADI SECONDARY SCHOOL CENTRE')]
            csv_writer.writerow(row)
      
      #print Columns
      #for line in csv_reader:
      #      print(line[0])
