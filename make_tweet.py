"""
@author: pswjt
"""
import random

def make_tweet():
    tweet = 'fucked up in the crib'
    food_or_drink = random.random()
    if food_or_drink > 0.19:
        file = open("foods.txt","r")
        verb = ' eating '
    else:
        file = open("drinks.txt","r")
        verb = ' drinking '
    arr = file.readlines()
    index = random.randint(0, len(arr) - 1)
    tweet = tweet + verb + arr[index].lower()
    file.close()
    return tweet
    
print(make_tweet())