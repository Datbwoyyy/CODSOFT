import streamlit as st
from PIL import Image
import numpy as np
import face_recognition
import cv2

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

    # Convert the image to RGB (face_recognition needs RGB format)
    image_rgb = image_array[:, :, ::-1]  # Convert BGR to RGB

    # Find all face locations in the image
    face_locations = face_recognition.face_locations(image_rgb)

    # Find face encodings for the faces in the image
    face_encodings = face_recognition.face_encodings(image_rgb, face_locations)

    # Initialize predicted label
    predicted_label = "Unknown"

    # Load images of known people from GitHub (raw URLs)
    obama_image = face_recognition.load_image_file("https://raw.githubusercontent.com/Datbwoyyy/CODSOFT/main/path_to_faces_db/President_Barack_Obama.jpg")
    bush_image = face_recognition.load_image_file("https://raw.githubusercontent.com/Datbwoyyy/CODSOFT/main/path_to_faces_db/George-W-Bush.jpeg")

    # Encode the faces
    obama_encoding = face_recognition.face_encodings(obama_image)[0]
    bush_encoding = face_recognition.face_encodings(bush_image)[0]
    
    # List of known face encodings
    known_face_encodings = [obama_encoding, bush_encoding]
    known_face_names = ["Barack Obama", "George Bush"]

    # Loop through each face found in the image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the detected face encoding to the known encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        # If a match is found, assign the predicted label
        if True in matches:
            first_match_index = matches.index(True)
            predicted_label = known_face_names[first_match_index]

        # Draw face box and label
        cv2.rectangle(image_array, (left, top), (right, bottom), (255, 0, 0), 2)
        cv2.putText(image_array, predicted_label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Door animation based on face recognition
    if predicted_label in ["Barack Obama", "George Bush"]:
        st.image(draw_door(opened=True))
    else:
        st.image(draw_door(opened=False))

    # Display the processed image with face detection box and label
    st.image(image_array, caption="Processed Image", use_column_width=True)
