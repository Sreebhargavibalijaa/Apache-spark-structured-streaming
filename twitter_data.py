import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
# import pykafka
from afinn import Afinn
import sys

class TwitterListener(StreamListener):
	def __init__(self):
    
		self.client = pykafka.KafkaClient("localhost:9092")
		self.producer = self.client.topics[bytes('twitter','ascii')].get_producer()

	def on_data(self, data):
		try:
			json_data = json.loads(data)

			send_data = '{}'
			json_send_data = json.loads(send_data)			
			json_send_data['text'] = json_data['text']
			json_send_data['senti_val']=afinn.score(json_data['text'])

			print(json_send_data['text'], "--", json_send_data['senti_val'])

			self.producer.produce(bytes(json.dumps(json_send_data),'ascii'))
			return True
		except KeyError:
			return True

	def on_error(self, status):
		print(status)
		return True

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: PYSPARK_PYTHON=python3 /bin/spark-submit ex.py <YOUR WORD>", file=sys.stderr)
		exit(-1)
	
	word = "Global warming"#sys.argv[1] # topic for which we have to perform sentimental analysis

	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	

	afinn = Afinn() 	# create AFINN object for sentiment analysis

	twitter_stream = Stream(auth, TwitterListener())
	twitter_stream.filter(languages=['en'], track=[word])
