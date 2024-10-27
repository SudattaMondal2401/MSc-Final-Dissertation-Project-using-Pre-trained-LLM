from PIL import Image
from IPython.display import clear_output
import matplotlib.pyplot as plt
import time
import numpy as np
import random
import re

def WordPairQuestions():
    original = ["Tree and Leaf", "Music and Dance", "Fire and Smoke", "Thunder and Storm", "Mountain and Valley", "Bird and Feather", "Heart and Soul", "Sand and Sea", "Star and Sky", "Soap and Water", "Shirt and Pant", "Toothbrush and Toothpaste", "Pillow and Blanket", "Cake and Candle", "Suit and Tie", "Moon and Tide", "Flower and Garden", "Time and Clock", "Road and Journey", "Chocolate and Vanilla"]
    questions = ["Leaf", "Music", "Smoke", "Thunder", "Valley", "Bird", "Soul", "Sand", "Sky", "Soap", "Pant", "Toothbrush", "Blanket", "Cake", "Tie", "Moon", "Garden", "Time", "Journey", "Chocolate"]
    answers = ["Tree", "Dance", "Fire", "Storm", "Mountain", "Feather", "Heart", "Sea", "Star", "Water", "Shirt", "Toothpaste", "Pillow", "Candle", "Suit", "Tide", "Flower", "Clock", "Road", "Vanilla"]
    answers_given = []
    score = 0
    
    r = range(0, 20)
    random_indices = random.sample(r, 10)
    
    for i in random_indices:
        print(original[i])
        time.sleep(3)
        clear_output(wait=True)
        
    np.random.shuffle(random_indices)
    answers_actual = []
    
    for i in random_indices:
        answers_actual.append(answers[i])
    
    for i in random_indices:
        print(questions[i])
        a = input("Enter the corresponding pair that was seen in question: ")
        a_processed = a.replace(" ", "").replace(".", "").title()
        answers_given.append(a)
        clear_output(wait=True)
        
    for i, j in zip(answers_actual, answers_given):
        if (i==j):
            score = score + 1
    return score