"""
File:    twitter.py
Author:  Pooja Rajamanikandan
Date:    03/04/2024
Section: 16 
E-mail:  le64534@umbc.edu
Description: 
"""
UNIQUE_CHARACTERS = ["@","#"]
EXIT_STRING = "quit"

def twitter_ats(the_tweet):
    users = []
    hashtags = []
    tweet_values =[users,hashtags]
    temp = the_tweet.split()

    for index in range(len(temp)):
        if UNIQUE_CHARACTERS[0] in temp[index]:
            users.append(temp[index][1:])
        elif UNIQUE_CHARACTERS[1] in temp[index]:
       
            hashtags.append(temp[index][1:])
    
    return tweet_values

if __name__ == "__main__":
    tweet = input("What do you want to tweet? ")
    while tweet != EXIT_STRING:
        values = twitter_ats(tweet)
        print("The users were:",", ".join(values[0]))
        print("The hash-tags were:",", ".join(values[1]))
        tweet = input("What do you want to tweet? ")

