import requests
from bs4 import BeautifulSoup


url = 'http://ahoy.re/top/all'
response = requests.get(url)
bersaglio = response.text
soup = BeautifulSoup(bersaglio)

links = soup.find_all('a', class_="detLink")

file = open("top_all_five.txt", "w")


for link in links[0:5]:
    titoli = link.contents[0]
    print >>file, titoli

print "operazione completata"



file.close()
