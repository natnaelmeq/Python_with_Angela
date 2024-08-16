import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
# print(all_movies)
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
# for n in range(len(movie_titles) -1,-1,-1):
#     print(movie_titles[n])


with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")


