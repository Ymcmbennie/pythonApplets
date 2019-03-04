__author__ = "Benson Sanga"

import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Welcome to your results")

iNumber = input("Please enter your student number e.g S0189/0001")
iYear = input("Enter year")
iSchoolnumber = iNumber[:5].lower()
iLink = "https://maktaba.tetea.org/exam-results/{exam}{year}/{number}.htm".format(year=iYear, exam='CSEE', number=iSchoolnumber)
if (request = requests.get(iLink)):
      iLink = iLink
else:
    iLink = "https://maktaba.tetea.org/exam-results/{exam}{year}/{number}.htm".format(year=iYear, exam='CSEE', number=iSchoolnumber.upper())  

print(iLink)

'''
#Getting results from pages
request = requests.get(iLink)
content = request.content
soup = BeautifulSoup(content, "html.parser")
if (soup.find("font", string=iNumber.upper())):
      student = soup.find("font", string=iNumber.upper())
else:
      student = soup.find("font", string=iNumber[6:10].upper())
studentReport = student.parent.parent
studentResults = studentReport.find_all("font")
studentNumber = studentResults[0].text
studentSex = studentResults[1].text
studentDivisionPoint = studentResults[2].text
studentDivision = studentResults[3].text
studentGrades = studentResults[4].text



#print("Your number is ",
 #    studentDivision," by ",
  #    studentDivisionPoint,
   #   ". And your grades are ",
    #  studentGrades)
    '''

