import feedparser
from typing import List

RSS_FEEDS = [
    "http://feeds.bbci.co.uk/news/education/rss.xml",
    "https://www.npr.org/rss/rss.php?id=1004"
]

def fetch_top_articles(max_articles=3):
    articles = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:max_articles]:
            articles.append({
                "title": entry.get("title"),
                "summary": entry.get("summary", ""),
                "link": entry.get("link")
            })
    return articles
