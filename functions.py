import tweepy
import os
import sys

def connect_api():
    api = None

    try:
        auth = tweepy.OAuthHandler(os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"))
        auth.set_access_token(os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_SECRET_TOKEN"))

        api = tweepy.API(auth)
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
        sys.exit(-1)
    return api


def get_user_id(api, user_name):
    user = api.get_user(screen_name=user_name)
    return user.id


def remove_tweets(api, user_id):
    time_line = api.user_timeline(user_id =user_id, count=1000, include_rts=True)

    total_tweets = len(time_line)
    r = input("You are going to delete {} tweets/retweets. Are you sure? Y/N:".format(total_tweets))

    if 'Y' == str(r).upper():
        all_tweets_id =  [[s.id, s.retweeted] for s in time_line]
        for s in all_tweets_id:
            if s[1]: #if is a retweet
                api.unretweet(s[0])
            else: #if is a normal tweet
                api.destroy_status(s[0])

        print("Task 'Remove tweets & retweets' completed.")




def remove_likes(api, user_id):
    favorites = api.get_favorites(user_id=user_id, count=3000)
    total_favs = len(favorites)

    r = input("You are going to unlike {} tweets. Are you sure? Y/N:".format(total_favs))

    if 'Y' == str(r).upper():
        all_favs_id =  [f.id for f in favorites]
        
        for f in all_favs_id:
            resp = api.destroy_favorite(f)
        
        print("Task 'Remove likes' completed.")

