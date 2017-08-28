'''
RIT SPEX:  Twitter posting basic.

Basic python script for posting to twitter.

Pre-Req:
    Python3
    Tweepy library twitter

Contributors:
    Evan Putnam
    Henry Yaeger
    John LeBrun
    Helen O'Connell
'''

import tweepy



def tweetPicture(api ,picUrl):
    '''
    Tweets picture from url
    :param api: API object
    :param picUrl: String-File Path on Machine
    :return:
    '''
    api.update_with_media(picUrl)

def tweetPost(api, postStr):
    '''
    Tweets text from postStr.
    :param api:  API object
    :param postStr: String
    :return:
    '''
    api.update_status(postStr)

def apiSetUp(conKey, conSec, accTok, accSec):
    '''
    Sets up the api object.
    :param conKey:
    :param conSec:
    :param accTok:
    :param accSec:
    :return:
    '''
    #Authenicates keys...
    auth = tweepy.OAuthHandler(conKey, conSec)
    auth.set_access_token(accTok, accSec)

    #Api object
    api = tweepy.API(auth)
    return api


def main():
    """
    NOTE: Do not send code to others with the consumer keys and access tokens.  It will allow them to access your twitter
    application.  This program is simple.  Enter 1 to post a twitter text post and 2 for an image post...
    :return:
    """

    #REPLACE WITH CONSUMER KEYS
    conKey = ""
    conSec = ""

    #REPLACE WITH ACCESS TOKENS
    accTok = ""
    accSec = ""

    if conKey == "" or conSec == "" or accTok == "" or accSec == "":
        print("WARNING YOU HAVE NOT ENTERERED YOUR INFORMATION")

    #Authenicates keys...
    auth = tweepy.OAuthHandler(conKey, conSec)
    auth.set_access_token(accTok, accSec)

    #Api object
    api = tweepy.API(auth)

    print("Press and enter 1 to post a text tweet")
    print("Press and enter 2 to post an image tweet")
    option = int(input("Enter Option(1 or 2):"))
    if option == 1:
        post = (input("Enter Post:"))
        tweetPost(api, post)
    elif option == 2:
        print("Image must be in folder of program")
        imagePath = (input("Enter Image Path:"))
        tweetPicture(api,imagePath)


if __name__ == '__main__':
    main()
