import cv2
import matplotlib.pyplot as plt
import numpy as np

def load_grayscale_image(path):

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return img

def show_images(original, compressed):

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original')
    plt.imshow(original, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Compressed')
    plt.imshow(compressed, cmap='gray')
    plt.axis('off')
    plt.show()

def save_compressed_image(img, path):

    cv2.imwrite(path,img)