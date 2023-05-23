import tweepy
import api_keys

def api():
    auth = tweepy.OAuthHandler(api_keys.barakadizibros.apikey, api_keys.barakadizibros.api_secret)
    auth.set_access_token(api_keys.barakadizibros.access_token, api_keys.barakadizibros.access_token_secret)
    api = tweepy.API(auth)
    return api

def tweet(api, tweet, image_path=None):
    if image_path:
        api.update_status_with_media(tweet, image_path)
    else:
        api.update_status(tweet)
    print("Tweeted: " + tweet)


if __name__ == "__main__":
    api = api()
    tweet(api, "Hello, Twitter!")