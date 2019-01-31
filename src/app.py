__author__ = "Benson Sanga"

import requests
from bs4 import BeautifulSoup

request = requests.get("https://matokeo.necta.go.tz/csee/results/s0189.htm")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("tr")
Student = element.find_all("font", {"face":"Arial"})
for link in soup.find_all('font'):
    print(link.get_text())
#print(names.text.strip())

#<font face="Arial" size = "1">s0189/0001</font>
#"text":"S0189/0001",