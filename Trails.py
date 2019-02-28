
__author__ = "Benson Sanga"

import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

iLink = 'https://necta.go.tz/results/2017/csee/csee.htm'
request0 = requests.get(iLink)
content0 = request0.content
soup0 = BeautifulSoup(content0, "html.parser")
links = soup0.find_all('a')


href = 'https://necta.go.tz/results/2017/csee/'+links[27]['href']
request = requests.get(href)
content = request.content
soup = BeautifulSoup(content, "html.parser","lxml")
student = soup.find_all("font")

html = soup
soup = BeautifulSoup(html)
table = soup.find("table")

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('output.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

print('Done')
'''
studentReport = student.parent.parent
studentResults = studentReport.find_all("font")
studentNumber = studentResults[0].text
studentSex = studentResults[1].text
studentDivisionPoint = studentResults[2].text
studentDivision = studentResults[3].text
studentGrades = studentResults[4].text
print ("Your number is ",
      studentNumber,". Your have got Division ",
      studentDivision," by ",
      studentDivisionPoint,
      ". And your grades are ",
      studentGrades)'''



'''for href in links:
      request = requests.get(href)
      content = request.content
      soup = BeautifulSoup(content, "html.parser")
      students = soup.find_all("font")
      for student in students:
            studentReport = student.parent.parent
            studentResults = studentReport.find_all("font")
            studentNumber = studentResults[0].text
            studentSex = studentResults[1].text
            studentDivisionPoint = studentResults[2].text
            studentDivision = studentResults[3].text
            studentGrades = studentResults[4].text
            print ("Your number is ",
                  studentNumber,". Your have got Division ",
                  studentDivision," by ",
                  studentDivisionPoint,
                  ". And your grades are ",
                  studentGrades)

            with open('new_results2.csv', 'w') as new_file:
                  fieldnames=['div', 'div_points', 'div_grades', 'stats', 'school_name']
                        
                  csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
                  
                  csv_writer.writeheader()
                        
                  line = {'div':'1',
                          'div_points':'25',
                          'div_grades':"ENGL - 'D'   PHY - 'F'   CHEM - 'F'",
                          'school_name':'P0712 BARIADI SECONDARY SCHOOL CENTRE'}

                  csv_writer.writerow(line)'''
