from PIL import Image
from IPython.display import clear_output
import matplotlib.pyplot as plt
import time
import numpy as np
import random
import re

def RecallWordsInReverse():
    words_list = ["chair", "coffee mug", "lamp", "notebook", "bicycle", "wallet", "toothbrush", "sunglasses", "keychain", "umbrella", "newspaper", "brick", "headphones", "watch", "water bottle", "refrigerator", "clock", "pencil", "basket", "remote control", "pillow", "plant", "jacket", "scissors", "soap", "spoon", "mirror", "plate", "tissue box", "calculator","shoes", "television", "flower", "book", "cup", "knife", "pen", "laptop", "hat", "bulb", "keyboard", "glasses", "bag", "picture", "razor", "phone", "table", "highway", "paper", "mansion", "brush", "socks", "chocolate", "bed", "vase", "remote", "calendar", "candle", "marble", "door"]
    
    r = range(0, 60)
    random_indices = random.sample(r, 10)
    new_word_list = []
    for i in random_indices:
        new_word_list.append(words_list[i])
        
    word_list_reverse = new_word_list[: : -1]
    
    print("This is the original list of words. Memorise it well!!")
    for word in new_word_list:
        print(word, end = " ")
        
    time.sleep(30)
    clear_output(wait=True)
    
    print("Now write the list of words in reverse. Write one word, then press enter to enter next one.")
    answer_given = []
    for i in range (10):
        word = input("Enter word: ")
        word = word.replace(".", "").lower()
        answer_given.append(word)
    
    score = 0  
    for i, j in zip(word_list_reverse, answer_given):
        if (i==j):
            score = score + 1
            
    return score