import cv2
import numpy as np
import hashlib
from datetime import datetime
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import tkinter as tk
from tkinter import filedialog, messagebox
import os


# Blockchain Class (remains the same as previous script)
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash, transaction=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
            'transaction': transaction
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_learning(self, check_data):
        hash_value = hashlib.sha256(check_data.tobytes()).hexdigest()
        return hash_value

    @staticmethod
    def hash_block(block):
        encoded_block = str(block).encode()
        return hashlib.sha256(encoded_block).hexdigest()


# Preprocessing Function
def preprocess_image(image_path):
    # Read image
    image = cv2.imread(image_path)

    # Check if image is loaded
    if image is None:
        raise ValueError(f"Unable to read image from {image_path}")

    # Resize and normalize
    image = cv2.resize(image, (256, 256))
    image = image / 255.0
    return np.expand_dims(image, axis=0)


# Create Check Detection Model
def create_check_detection_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(2, activation='softmax')  # Binary classification
    ])

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    return model


# Fake Check Detection Function
def detect_fake_check(model, image):
    prediction = model.predict(image)
    return np.argmax(prediction, axis=1)[0]  # 0: legitimate, 1: fake


# Image Upload and Detection GUI
class CheckDetectionApp:
    def __init__(self, master):
        self.master = master
        master.title("Check Detection System")
        master.geometry("500x400")

        # Blockchain and Model Initialization
        self.blockchain = Blockchain()
        self.fake_check_model = create_check_detection_model()

        # Upload Button
        self.upload_button = tk.Button(master, text="Upload Check Image", command=self.upload_image)
        self.upload_button.pack(pady=20)

        # Result Label
        self.result_label = tk.Label(master, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

        # Image Display Label
        self.image_label = tk.Label(master)
        self.image_label.pack(pady=10)

    def upload_image(self):
        # Open file dialog to select image
        file_path = filedialog.askopenfilename(
            title="Select Check Image",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif"),
                ("All files", "*.*")
            ]
        )

        if not file_path:
            return

        try:
            # Preprocess the image
            processed_image = preprocess_image(file_path)

            # Detect fake check
            classification = detect_fake_check(self.fake_check_model, processed_image)
            is_legitimate = (classification == 0)

            # Create blockchain entry
            check_hash = self.blockchain.proof_of_learning(processed_image)
            previous_block = self.blockchain.get_previous_block()
            self.blockchain.create_block(
                proof=check_hash,
                previous_hash=self.blockchain.hash_block(previous_block),
                transaction={
                    "check_hash": check_hash,
                    "legitimacy": is_legitimate
                }
            )

            # Display result
            label = "Legitimate" if is_legitimate else "Fake"
            color = "green" if is_legitimate else "red"
            self.result_label.config(text=f"Check Classification: {label}", fg=color)

            # Display uploaded image
            self.display_image(file_path)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_image(self, file_path):
        # Read and resize image for display
        img = cv2.imread(file_path)
        img = cv2.resize(img, (300, 300))

        # Convert color for tkinter
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Convert to PhotoImage
        from PIL import Image, ImageTk
        photo = ImageTk.PhotoImage(Image.fromarray(img))

        # Update image label
        self.image_label.config(image=photo)
        self.image_label.image = photo  # Keep a reference


def main():
    # Create main window
    root = tk.Tk()

    # Initialize and run the app
    app = CheckDetectionApp(root)

    # Start GUI event loop
    root.mainloop()


# Run the application
if __name__ == "__main__":
    main()