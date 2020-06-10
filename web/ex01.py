from bs4 import BeautifulSoup
fp = open("ex01.html")
soup = BeautifulSoup(fp, 'html.parser')

first_div = soup.find("div")
print(first_div)