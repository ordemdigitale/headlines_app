import feedparser

Y_FEED = "https://www.yahoo.com/news/rss"

x = feedparser.parse(Y_FEED)

feed = x.entries[2].title

print(feed)