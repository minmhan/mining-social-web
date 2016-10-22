import urllib
import json

def print_tweet(page=1):
	response = urllib.request.urlopen("http://search.twitter.com/search.json?q=microsoft&page=" + str(page));
	data = json.load(response);
	try:
		tweets = data['results'];
		for t in tweets:
			print(t['text']);
	except:
		print('error in retrieving tweet data');

for i in range(1,11):
	#print(i);	
	print_tweet(i);
