import bs4
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
contents = response.text

soup = bs4.BeautifulSoup(contents, "html.parser")
song_names = soup.find_all("span", class_="")
song_names_list = [song.getText() for song in song_names]

print(song_names_list)
