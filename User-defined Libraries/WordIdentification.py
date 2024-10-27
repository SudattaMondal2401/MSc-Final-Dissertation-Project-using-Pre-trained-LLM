from PIL import Image
from IPython.display import clear_output
import matplotlib.pyplot as plt
import time
import numpy as np
import random
import re

def WordIdentification():
    actual_words = ["chair", "coffee mug", "lamp", "notebook", "bicycle", "wallet", "toothbrush", "sunglasses", "keychain", "umbrella", "newspaper", "brick", "headphones", "watch", "water bottle", "refrigerator", "clock", "pencil", "basket", "remote control", "pillow", "plant", "jacket", "scissors", "soap", "spoon", "mirror", "plate", "tissue box", "calculator"]
    dummy_words = ["shoes", "television", "flower", "book", "cup", "knife", "pen", "laptop", "hat", "bulb", "keyboard", "glasses", "bag", "picture", "razor", "phone", "table", "highway", "paper", "mansion", "brush", "socks", "chocolate", "bed", "vase", "remote", "calendar", "candle", "marble", "door"]
    
    r_question = range(0, 30)
    random_indices_question = random.sample(r_question, 10)
    print("This is the set of 10 actual words. Memorise them well!!")
    for i in random_indices_question:
        print(actual_words[i], end = "   ")
    print()
    
    time.sleep(20)
    clear_output(wait=True)
    
    r_dummy = range(0, 30)
    random_indices_dummy = random.sample(r_dummy, 5)
    random_indices_actual = random.sample(random_indices_question, 5)
    
    list_actual = []
    list_dummy = []
    
    for i in random_indices_actual:
        list_actual.append(actual_words[i])
        
    for i in random_indices_dummy:
        list_dummy.append(dummy_words[i])
        
    list_final = list_dummy + list_actual
    np.random.shuffle(list_final)
    
    print("This is the list with half actual and half dummy words. Which 5 words amongst these were in the original list??")
    for i in list_final:
        print(i, end = "   ")
    print()
    
    answer_given = []
    score = 0
    
    while True:
        
        for i in range(5):
            a = input()
            a = a.replace(".", "").lower()
            answer_given.append(a)
 
        if len(set(answer_given))==len(answer_given):
            break
        else:
            print("DO NOT WRITE SAME OPTION MULTIPLE TIMES!!")

    for i in answer_given:
        for j in list_actual:
            if(i==j):
                score = score + 1
                
    return score