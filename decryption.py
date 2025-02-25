import cv2
import os

def decode_text_from_image(image):
    img = cv2.imread(image)
    h, w, _ = img.shape
    text = ""
    
    for i in range(h):
        for j in range(w):
            char = chr(img[i, j, 0])
            if text.endswith("##END##"):
                return text.replace("##END##", "")
            text += char
    
    return text
