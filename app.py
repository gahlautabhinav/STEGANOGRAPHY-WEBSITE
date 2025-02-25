from flask import Flask, request, jsonify, send_file, render_template
import os
from encryption import encode_text_in_image
from decryption import decode_text_from_image

app = Flask(__name__, static_folder="static", template_folder="templates")  # Set up static & template folders
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")  # Serves the HTML page

@app.route("/encrypt", methods=["POST"])
def encrypt():
    if "image" not in request.files or "text" not in request.form:
        return jsonify({"error": "Missing image or text"}), 400
    
    image = request.files["image"]
    text = request.form["text"]
    password = request.form.get("password", "")

    image_path = os.path.join(UPLOAD_FOLDER, "input.png")
    image.save(image_path)
    encrypted_image = encode_text_in_image(image_path, text + password)

    return send_file(encrypted_image, as_attachment=True)

@app.route("/decrypt", methods=["POST"])
def decrypt():
    if "image" not in request.files or "password" not in request.form:
        return jsonify({"error": "Missing image or password"}), 400

    image = request.files["image"]
    password = request.form["password"]

    image_path = os.path.join(UPLOAD_FOLDER, "encrypted_input.png")
    image.save(image_path)
    decrypted_text = decode_text_from_image(image_path)

    if decrypted_text.endswith(password):
        return jsonify({"message": decrypted_text.replace(password, "")})
    else:
        return jsonify({"error": "Incorrect password"}), 403

if __name__ == "__main__":
    app.run(debug=True)
