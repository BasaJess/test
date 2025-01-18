from bs4 import BeautifulSoup
import requests
URL = "https://www.cs.cmu.edu/~rgs/alice-I.html" 
html = requests.get(URL, {}).text
#getting the text from html
soup = BeautifulSoup(html)
alice_book = soup.text
lines = alice_book.split("\n")

file = open("myfile.txt","w")

for line in lines:
  if "Alice" in line:
    file.write(line+'\n')

file.close()

alice_count = sum(line.count('Alice') for line in lines)
print(alice_count)

file = open("myfile.txt","r")
lines = file.readlines()

for line in lines:
    print(line)