import tweepy
import api_keys

client = tweepy.Client(consumer_key=api_keys.ruvenovedvsadler.apikey,
                    consumer_secret=api_keys.ruvenovedvsadler.api_secret,
                    access_token=api_keys.ruvenovedvsadler.access_token,
                    access_token_secret=api_keys.ruvenovedvsadler.access_token_secret)



# Replace the text with whatever you want to Tweet about
response = client.create_tweet(text='I believe Yesod Hamaala is the best place in the world')