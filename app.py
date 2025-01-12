import streamlit as st
import numpy as np
import cv2
from PIL import Image
from deepface import DeepFace

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Door animation function
def draw_door(opened):
    from PIL import Image, ImageDraw
    img = Image.new("RGB", (500, 300), "white")
    draw = ImageDraw.Draw(img)

    # Door frame
    draw.rectangle([50, 50, 450, 250], outline="black", width=5)

    if opened:
        # Door open
        draw.rectangle([300, 50, 450, 250], fill="white")
        text = "Door Open"
    else:
        # Door closed
        draw.rectangle([50, 50, 450, 250], fill="brown")
        text = "Door Closed"

    draw.text((200, 270), text, fill="black")
    return img

st.title("Face Recognition Door System")

# Upload an image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Read image
    image = np.array(Image.open(uploaded_file))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Initialize predicted label variable
    predicted_label = "Unknown"

    for (x, y, w, h) in faces:
        # Crop and preprocess face
        face = image[y:y + h, x:x + w]
        face = cv2.resize(face, (299, 299))  # Resize for face recognition model
        face = np.expand_dims(face, axis=0)

        # Use DeepFace to recognize the face
        try:
            result = DeepFace.find(img_path=face, db_path='path_to_faces_db', model_name='VGG-Face')
            # If face is recognized, show label
            predicted_label = result['identity'][0].split('/')[-1]  # Extract name from db_path
        except Exception as e:
            predicted_label = "Unknown"
        
        # Draw face box and label
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(image, predicted_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Logic for opening or closing the door based on recognized person
    if predicted_label == "Barack Obama" or predicted_label == "George Bush":
        st.image(draw_door(opened=True))  # Open the door for Obama or Bush
    else:
        st.image(draw_door(opened=False))  # Close the door for everyone else (including LFW faces)

    # Display image with annotations
    st.image(image, caption="Processed Image", use_column_width=True)
