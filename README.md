# Secure Data Hiding in Image using Steganography

This project is a web-based application that allows users to securely encrypt text messages into images and later decrypt them using a password. It combines Python, Flask, and OpenCV for the backend, alongside HTML, CSS, and JavaScript for the frontend. The goal is to demonstrate how steganography (hiding data within images) can be used for secure text encryption and decryption.

**Features**
- **Encrypt Text into Image**:
  - Users can upload an image, input a secret text message, and set a password.
  - The text message is then encrypted and hidden within the image using the least significant bit (LSB) technique in the image's blue channel.
  - An encrypted image is generated and made available for download.

- **Decrypt Text from Image**:
  - Users can upload an encrypted image and enter the password used during encryption.
  - If the password is correct, the text embedded within the image is retrieved and displayed to the user.
  - If the password is incorrect, an error message is shown.

**Technologies Used**
- **Backend**:
  - Flask: A lightweight Python web framework used to handle HTTP requests and responses.
  - OpenCV: A computer vision library used to manipulate and encode/decode images.
  - Python: Core language for implementing encryption and decryption logic.

- Frontend:
  - HTML: Structure of the webpage.
  - CSS: Styling of the webpage, with a dark-themed, glassmorphism UI.
  - JavaScript: Handling frontend logic for image uploading, interaction with Flask API, and displaying results.
 
**Installation & Setup**
1. Clone the Repository
   - git clone https://github.com/yourusername/STEGANOGRAPHY-WEBSITE.git

2. Install Dependencies
   - pip install flask opencv-python

3. Run the Application
   - python app.py
   - The application will be accessible at `http://127.0.0.1:5000/`

**How It Works**
- Encryption
  1. Select an image from your device.
  2. Enter a secret message to encrypt.
  3. Enter a password for additional security.
  4. Click "Encrypt" to generate the encrypted image for download.

- Decryption
  1. Upload the encrypted image.
  2. Enter the password used during encryption.
  3. Click "Decrypt" to retrieve and display the decrypted message if the password is correct.

# **OUTPUT**
![Image](https://github.com/user-attachments/assets/11d3d978-86e7-4659-a803-3b104b616b6d)
