import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model("waste_classification_model.h5")  # Update with your model name

# Define the image size expected by the model
IMG_SIZE = (150, 150)  # Update this if your model requires a different size

def preprocess_image(img_path):
    """ Preprocess the image to match model input shape. """
    img = Image.open(img_path).convert("RGB")
    img = img.resize(IMG_SIZE)  # Resize to model's input size
    img_array = np.array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

def classify_image():
    """ Classify the uploaded image and display result. """
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    
    if file_path:
        # Display image
        img = Image.open(file_path)
        img = img.resize((250, 250))  # Resize for display
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk

        # Preprocess and predict
        processed_img = preprocess_image(file_path)
        prediction = model.predict(processed_img)[0]

        # Assuming binary classification: 0 - Organic, 1 - Plastic
        class_name = "Organic Waste" if prediction[0] < 0.5 else "Plastic Waste"
        result_label.config(text=f"Prediction: {class_name}", fg="green", font=("Arial", 14, "bold"))

def reset():
    """ Reset the UI to allow new image uploads without restarting. """
    image_label.config(image="")  # Clear displayed image
    result_label.config(text="")  # Clear prediction result

# Create GUI window
root = tk.Tk()
root.title("Waste Classification")

# UI Components
upload_btn = tk.Button(root, text="Upload Image", command=classify_image, font=("Arial", 12), bg="blue", fg="white")
upload_btn.pack(pady=10)

reset_btn = tk.Button(root, text="Reset", command=reset, font=("Arial", 12), bg="red", fg="white")
reset_btn.pack(pady=5)

image_label = tk.Label(root)
image_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
