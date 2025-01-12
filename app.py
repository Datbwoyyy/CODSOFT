import streamlit as st
from PIL import Image
import cv2
import numpy as np
from deepface import DeepFace
from io import BytesIO

# Door animation
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
    # Read the uploaded image
    image = Image.open(uploaded_file)
    image_array = np.array(image)
    
    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)

    # Load Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Initialize predicted label
    predicted_label = "Unknown"

    for (x, y, w, h) in faces:
        # Crop the face from the image
        face = image_array[y:y + h, x:x + w]
        
        # Use DeepFace to find the closest match
        result = DeepFace.find(img_path=face, db_path='path_to_faces_db', model_name='VGG-Face')

        if len(result) > 0:
            # If the model finds a match, determine the label
            predicted_label = result[0]['identity'][0].split("/")[-1]  # Getting the name from the result file path

        # Draw face box and label
        cv2.rectangle(image_array, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(image_array, predicted_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Door animation based on face recognition
    if predicted_label in ["Barack Obama", "George Bush"]:
        st.image(draw_door(opened=True))
    else:
        st.image(draw_door(opened=False))

    # Display the processed image with face detection box and label
    st.image(image_array, caption="Processed Image", use_column_width=True)
