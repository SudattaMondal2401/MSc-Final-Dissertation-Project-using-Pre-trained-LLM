from PIL import Image
from IPython.display import clear_output
import matplotlib.pyplot as plt
import time
import numpy as np
import random
import re

def PictureIdentification(actual_filename, dummy_filename):
    
    answers_given = []
    score = 0
    
    r = range(1, 31)
    random_indices = random.sample(r, 10)
    
    image_path = []
    for i in random_indices:
        image_path.append(actual_filename + f'/{i}.jpg')
    
    print("This is the set of original images. Memorize them well!!")
    fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(12, 6))
    for ax, img_path in zip(axes.flat, image_path):
        image = Image.open(img_path)
        ax.imshow(image)
        ax.axis('off')
    
    plt.show()
    time.sleep(10)
    clear_output(wait=True)
    
    r = range(31, 61)
    random_indices = random.sample(r, 5)
    
    image_path_dummy = []
    for i in random_indices:
        image_path_dummy.append(dummy_filename + f'/{i}.jpg')
        
    image_path_actual = random.sample(image_path, 5)
    final_image_path = image_path_dummy + image_path_actual
    np.random.shuffle(final_image_path)
    
    indices = []
    for i in final_image_path:
        indice = re.findall(r'\d+', i)
        indices.append(indice)
        
    final_indices = []
    for i in indices:
        for j in i:
            final_indices.append(int(j))
    
    fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(12, 6))
    for ax, img_path in zip(axes.flat, final_image_path):
        image = Image.open(img_path)
        ax.imshow(image)
        ax.axis('off')
        
    plt.show()
    print("This is the list with half actual and half dummy pictures. Which 5 pictures amongst these were in the original list?? Write their indices")
    
    answer_given = []
    score = 0
    
    while True:
        
        for i in range(5):
            a = int(input())
            answer_given.append(a-1)
        
        if len(set(answer_given))==len(answer_given):
            break
        else:
            print("DO NOT WRITE SAME OPTION MULTIPLE TIMES!!")
            
    for pos in answer_given:
        if(final_indices[pos])<=30:
            score = score + 1
    
    return score