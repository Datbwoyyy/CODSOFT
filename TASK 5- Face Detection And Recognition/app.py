import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import tensorflow as tf
import os

# Suppress TensorFlow warnings
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# Load Haar Cascade model for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load FaceNet model
model_path = r"C:\Users\HP\Desktop\Codsoft\TASK 5- Face Detection And Recognition"
model = tf.saved_model.load(model_path)  # Ensure this path points to the correct folder
inference_fn = model.signatures["serving_default"]

# Load known embeddings (update paths as needed)
obama_embeddings = np.load(r"C:\Users\HP\Desktop\Codsoft\TASK 5- Face Detection And Recognition\embeddings\obama_embedding.npy", allow_pickle=True)
george_bush_embeddings = np.load(r"C:\Users\HP\Desktop\Codsoft\TASK 5- Face Detection And Recognition\embeddings\george_bush_embedding.npy", allow_pickle=True)

known_embeddings = {
    "Barack Obama": obama_embeddings,
    "George Bush": george_bush_embeddings,
}

# Functions for face recognition
def preprocess_image(image):
    image = cv2.resize(image, (160, 160))
    image = (image - 127.5) / 128.0
    return np.expand_dims(image, axis=0)

def euclidean_distance(emb1, emb2):
    return np.linalg.norm(emb1 - emb2)

def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

def get_embeddings(face_image):
    preprocessed_image = preprocess_image(face_image)
    embeddings = inference_fn(tf.constant(preprocessed_image, dtype=tf.float32))["Bottleneck_BatchNorm"].numpy()
    return embeddings

def recognize_face(image):
    faces = detect_faces(image)
    if len(faces) == 0:
        return None, "No face detected!"

    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        embeddings = get_embeddings(face)

        threshold = 12
        for name, known_emb in known_embeddings.items():
            distance = euclidean_distance(embeddings, known_emb)
            if distance < threshold:
                return name, f"Match found: {name}"

    return None, "No match found!"

# Tkinter GUI
def upload_and_recognize():
    global panel, door_label

    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if not file_path:
        return

    image = cv2.imread(file_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(image_rgb)
    img_tk = ImageTk.PhotoImage(image_pil)
    
    panel.config(image=img_tk)
    panel.image = img_tk

    name, result = recognize_face(image)
    result_label.config(text=result)

    if name:
        door_label.config(image=door_open_img)
        door_label.image = door_open_img
    else:
        door_label.config(image=door_closed_img)
        door_label.image = door_closed_img

# Main Tkinter Window
root = tk.Tk()
root.title("Face Recognition - Door Opener")

upload_button = tk.Button(root, text="Upload Image", command=upload_and_recognize)
upload_button.pack()

panel = tk.Label(root)
panel.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack()

# Load door images
door_open_img = ImageTk.PhotoImage(Image.open("images/door_opened.jpg").resize((200, 400)))
door_closed_img = ImageTk.PhotoImage(Image.open("images/door_closed.jpg").resize((200, 400)))

door_label = tk.Label(root, image=door_closed_img)
door_label.pack()

# Start Tkinter loop
root.mainloop()
