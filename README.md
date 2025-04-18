# Waste Classification Using CNN Model

This project is a **waste classification system** that utilizes a **Convolutional Neural Network (CNN)** to classify images into **Organic Waste** or **Plastic Waste** categories. It features a **Tkinter GUI** that allows users to upload an image, receive a prediction, and reset the interface for multiple classifications.

---

## 📌 Features
- 📷 **Image Upload**: Users can upload an image for classification.
- 🧠 **CNN-Based Prediction**: Uses a trained CNN model (`waste_classification_model.h5`) for classification.
- 🏷️ **Classifies Waste**: Determines whether the waste is **Organic** or **Plastic**.
- 🔄 **Reset Functionality**: Allows users to reset and classify multiple images without restarting the application.
- 🖼️ **GUI Interface**: Built with **Tkinter** for a user-friendly experience.

---

## 🛠️ Installation

### **1️⃣ Prerequisites**
Ensure you have **Python 3.7+** installed along with the required dependencies.

### **2️⃣ Install Dependencies**
Run the following command to install necessary Python libraries:

```bash
pip install tensorflow pillow numpy tkinter
```

---

## 🚀 Usage

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/Waste Classification Using CNN.git
cd Waste Classification Using CNN
```

### **2️⃣ Place Your Model**
Ensure that your trained **CNN model** (`waste_classification_model.h5`) is inside the project folder.

### **3️⃣ Run the Application**
Execute the following command to start the GUI:

```bash
python app.py
```

### **4️⃣ Upload & Classify**
- Click the **"Upload Image"** button.
- Select an image (**JPG, PNG, JPEG**).
- The application will display the image and predict whether it is **Organic Waste** or **Plastic Waste**.
- Click **"Reset"** to upload another image.

---

## 📸 GUI Preview
![image](https://github.com/user-attachments/assets/8fc8b807-8559-490c-9ec5-1a4b95060138)

---

## 🔬 How It Works
1. The image is **preprocessed**: resized to **150x150 pixels** and normalized.
2. The preprocessed image is **fed into the CNN model** for prediction.
3. The model returns a probability score to classify the image as:
   - **Organic Waste** (if the probability is < 0.5).
   - **Plastic Waste** (if the probability is ≥ 0.5).
4. The result is displayed in the **Tkinter GUI**.

---

## 🛠️ Technologies Used
- **Python**
- **TensorFlow/Keras** (for CNN model)
- **Tkinter** (for GUI)
- **Pillow (PIL)** (for image processing)
- **NumPy** (for array operations)

---

## 📌 Future Improvements
- 🏷️ Improve classification by adding more waste categories.
- 🔍 Enhance model accuracy with more training data.
- 📱 Create a **mobile version** of the app.
- ☁️ Deploy the model on **Flask/FastAPI** for web-based classification.

---


## 🤝 Contributing
Contributions are welcome! If you find any issues or want to add new features:
1. **Fork** this repository.
2. **Create a branch** (`feature-name`).
3. **Commit your changes** (`git commit -m "Added feature X"`).
4. **Push to your branch** and **create a pull request**.

---

## 📞 Contact
👤 **Chetan Singh Chouhan**  
📧 chouhanchetan066@gmail.com  

---

⭐ **If you like this project, please give it a star!** ⭐

