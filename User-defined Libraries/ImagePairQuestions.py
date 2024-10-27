from PIL import Image
from IPython.display import clear_output
import matplotlib.pyplot as plt
import time
import numpy as np
import random
import re

def ImagePairQuestions(question_filename, answer_filename):
    answers = ["pepper", "moon", "bread", "fork", "lock", "cup", "orange", "pen", "door", "comb", "umbrella", "horse", "cat", "table", "sugar", "shoe", "needle", "fish", "sunflower", "cloud"]
    answers_given = []
    score = 0
    
    r = range(1, 21)
    random_indices = random.sample(r, 10)
    
    image_path = []
    for i in random_indices:
        image_path.append(question_filename + f'/{i}.jpg')
    
    fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(12, 6))
    
    for ax, img_path in zip(axes.flat, image_path):
        image = Image.open(img_path)
        ax.imshow(image)
        ax.axis('off')
    
    plt.show()
    time.sleep(20)
    clear_output(wait=True)
        
    np.random.shuffle(random_indices)
    answers_actual = []
    for i in random_indices:
        answers_actual.append(answers[i-1])
        
    for i in random_indices:
        image_path = answer_filename + f'/{i}.jpg'
        image = Image.open(image_path)
        plt.imshow(image)
        plt.axis('off')
        plt.show()
        a = input("Enter the corresponding pair that was seen in question: ")
        a_processed = a.replace(" ", "").replace(".", "").lower()
        answers_given.append(a)
        clear_output(wait=True)

    for i, j in zip(answers_actual, answers_given):
        if (i==j):
            score = score + 1
    return score