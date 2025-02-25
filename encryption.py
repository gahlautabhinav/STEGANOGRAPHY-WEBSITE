import cv2
import os

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def encode_text_in_image(image_path, text):
    img = cv2.imread(image_path)
    h, w, _ = img.shape
    text += "##END##"  # End marker for retrieval

    index = 0
    for i in range(h):
        for j in range(w):
            if index < len(text):
                img[i, j, 0] = ord(text[index])  # Store character ASCII in the blue channel
                index += 1
            else:
                break

    encoded_img_path = os.path.join(UPLOAD_FOLDER, "encrypted.png")
    cv2.imwrite(encoded_img_path, img)
    return encoded_img_path
