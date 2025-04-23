# code >>>>>>>>>>>>
from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import os
import tensorflow as tf

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Load the trained model
model = tf.keras.models.load_model("waste_classification_model.h5")
IMG_SIZE = (150, 150)  
def preprocess_image(image_path):
    img = Image.open(image_path).convert("RGB")
    img = img.resize(IMG_SIZE)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    image_path = None
    if request.method == "POST":
        file = request.files["image"]
        if file:
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(image_path)

            processed_img = preprocess_image(image_path)
            pred = model.predict(processed_img)[0]
            prediction = "Organic Waste" if pred[0] < 0.5 else "Plastic Waste"

    return render_template("index.html", prediction=prediction, image_path=image_path)

if __name__ == "__main__":
    app.run(debug=True)
