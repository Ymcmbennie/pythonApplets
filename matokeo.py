__author__ = "Benson Sanga"

import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Welcome to your results")

iNumber = input("Please enter your student number e.g S0189/0001")
iSchoolnumber = iNumber[:5].lower()
iLink = "https://matokeo.necta.go.tz/csee/results/{}.htm".format(iSchoolnumber)


#Getting results from pages
request = requests.get(iLink)
content = request.content
soup = BeautifulSoup(content, "html.parser")
student = soup.find("font", string=iNumber.upper())
studentReport = student.parent.parent
studentResults = studentReport.find_all("font")
studentNumber = studentResults[0].text
studentSex = studentResults[1].text
studentDivisionPoint = studentResults[2].text
studentDivision = studentResults[3].text
studentGrades = studentResults[4].text


print("Your number is ",
      studentNumber,". Your have got Division ",
      studentDivision," by ",
      studentDivisionPoint,
      ". And your grades are ",
      studentGrades)

