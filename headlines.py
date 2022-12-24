import feedparser
from flask import Flask

app = Flask(__name__)

RSS_FEEDS = {'yahoo': 'https://www.yahoo.com/news/rss',
            'cnn': 'http://rss.cnn.com/rss/edition.rss'}
#Y_FEED = "https://www.yahoo.com/news/rss"


@app.route('/')
@app.route('/yahoo')
def yahoo_news():
    return get_news('yahoo')


@app.route('/cnn')
def cnn_news():
    return get_news('cnn')


def get_news(publication):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1>News Headlines</h1> </br>
            <b>{0}</b> 
            <i>{1}</i> </br>
            <p>{2}</p> </br>
        </body>
    </html>""".format(first_article.get('title'), first_article.get('published'), first_article.get('link'))

if __name__ == "__main__":
    app.run(debug=True)