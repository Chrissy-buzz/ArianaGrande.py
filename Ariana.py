
import tweepy
from twilio.rest import Client

#Authentification from Twilio
account_sid = "Please access with your account_sid"
# Your Auth Token from twilio.com/console
auth_token  = "Please access with your auth_token"

client = Client(account_sid, auth_token)

#Authentification for Tweepy
auth = tweepy.OAuthHandler("Please access with your account_sid", "Please access with your account_sid")
auth.set_access_token("Please access with your auth_token", "Please access with your auth_token")

# DEBUG To Verify Twitter Credentials
#try:
#    api.verify_credentials()
#    print("Authentication OK")
#except:
#    print("Error during authentication")

#Filters out mentions and RTs
def from_creator(status):
    if hasattr(status, 'retweeted_status'):
        return False
    elif status.in_reply_to_status_id != None:
        return False
    elif status.in_reply_to_screen_name != None:
        return False
    elif status.in_reply_to_user_id != None:
        return False
    else:
        return True

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, status):
        if from_creator(status):
            print("🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍")
            print(f"{status.text}")
            txt=status.text
            if txt=="tour" or "Tour":
                print("Shes going on tour 😄")
            username = status.user.screen_name
            print(username)
            hashtags = status.entities['hashtags']
            if hashtags:
                print(hashtags)
            else:
                print("☀")
            acctdesc = status.user.description
            if acctdesc:
                print(acctdesc)
            else:
                print("⭐")
            location = status.user.location
            if location:
                print(location)
            else:
                print("❣")
            print("🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍")
            message = client.messages.create(to="+1yournumber", from_ ="+1twilionumber", body = txt)
            print(message)
            following = status.user.friends_count
            followers = status.user.followers_count
            totaltweets = status.user.statuses_count
            usercreatedts = status.user.created_at
            tweetcreatedts = status.created_at
            retweetcount = status.retweet_count


    def on_error(self, status):
        print("Error detected")

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(follow=["34507480"]) #you can change the user ID to track other twitter users
