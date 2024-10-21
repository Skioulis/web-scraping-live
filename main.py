# a webscraping exercise from https://news.ycombinator.com/news

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all(name='span', class_="titleline")
article_scores = [ int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
article_titles = []
article_links = []



for article in articles:
    link_in_article = article.find(name='a')
    article_titles.append(link_in_article.getText())
    article_links.append(link_in_article.get('href'))

max_index = article_scores.index(max(article_scores))
best_article = {}

best_article = {
        "title": article_titles[max_index],
        "link": article_links[max_index],
        "score": article_scores[max_index],
    }

print(f"The best article is : {best_article['title']} with link: {best_article['link']} and score: {best_article['score']}")



# if True:
#     print(f"The highest voted article is")
# # print(article.find(name="a").get())









# print(len(scores))
# print(scores)
# print(max(scores))
# print(max_index)