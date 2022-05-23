# Write your code here :-)
import requests
import bs4
result=requests.get('https://quotes.toscrape.com/')
soup=bs4.BeautifulSoup(result.text,'lxml')

quotes=soup.select('span.text')
for q in quotes:
   print(q.getText())


