import bs4
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

website_content = response.text

soup = bs4.BeautifulSoup(website_content, "html.parser")

movies_list = soup.findAll(name="h3", class_="title")

movie_titles = [movie.getText() for movie in movies_list]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as movie_file:
    for movie in movies:
        movie_file.write(f"{movie}\n")
