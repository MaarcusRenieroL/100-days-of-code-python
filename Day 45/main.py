import bs4
import requests


with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = bs4.BeautifulSoup(contents, "html.parser")

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.a)
print(soup.prettify())
name = soup.select_one(selector="#name")
print(name)

print(soup.select(selector=".heading"))

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = bs4.BeautifulSoup(yc_web_page, "html.parser")
articles = soup.findAll(name="a", class_="titlelink")
article_links = []
article_texts = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(scores.getText().split()[0]) for scores in soup.findAll(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

max_index = article_upvotes.index(max(article_upvotes))
print(article_texts[max_index])
print(article_upvotes[max_index])