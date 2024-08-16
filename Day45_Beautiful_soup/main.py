from bs4 import BeautifulSoup
import requests
response = requests.get("https://natnael.dk")
website_data= response.text
soup = BeautifulSoup(website_data,"html.parser")
linkes= soup.findAll(name="a")

article_text = []
article_link = []

for a in linkes:
    a_text = a.getText()
    article_text.append(a_text)
    a_link= a.get("href")
    article_link.append(a_link)

print(article_text)
print(article_link)



#
# with open("website.html",encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents,"html.parser")
# print(soup.title)
# print((soup.title.string))
