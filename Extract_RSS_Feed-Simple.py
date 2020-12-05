# Import feedparser module 
import feedparser

# Parse the google news RSS feed 
rss_url = 'https://news.google.com/rss?hl=en-IN&amp;ned=us&amp;gl=IN&gl=IN&ceid=IN:en'
feed = feedparser.parse(rss_url)

# Display the google news titles
for newsitem in feed['items']:
	print(newsitem['title'])


	