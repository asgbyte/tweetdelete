from functions import connect_api,get_user_id,remove_tweets,remove_likes
import sys


if len(sys.argv)==2:
    user_name = sys.argv[1]
else:
    print("Fail...\nFirst argument with your username needed.")
    sys.exit(-1)


print("{}, choose an option:".format(user_name))
print("     (1) Remove tweets and retweets.")
print("     (2) Remove likes.")
print("     (3) Exit.")
option = int(input("Enter a number: \n"))

api = connect_api()
user_id = get_user_id(api, user_name)
if option == 1:
    remove_tweets(api, user_id)
if option == 2:
    remove_likes(api, user_id)


