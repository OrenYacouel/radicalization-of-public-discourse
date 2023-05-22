
import requests

API_KEY = '203bf6d9bf8241309fa87bc6eecb4b0a'

# check if the url contains one of the words from group "words"
def are_words_in_url(url, words):
    for word in words:
        if word in url:
            return False
    return True

def get_top_political_article_urls():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us',
        'category': 'politics',
        'apiKey': API_KEY,
        'pageSize': 30
    }

    response = requests.get(url, params=params)
    data = response.json()

    top_articles = data.get('articles', [])

    # Extract the URLs of the top 10 political articles
    top_article_urls = []
    bad_words = ["movies", "movie", "hollywood", "youtube", "sport", "sports", "athletic", "horoscope", "lifestyle", "boxing", "health", "wellness", "finance", "deadline"]
    for article in top_articles:
        article_url = article.get('url')
        if (article_url and are_words_in_url(article_url, bad_words)):
            top_article_urls.append(article_url)

    return top_article_urls

# Call the function to get the top 10 political article URLs
political_article_urls = get_top_political_article_urls()

# Print the URLs
for i in range(10):
    print(political_article_urls[i])

