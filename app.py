from sklearn.decomposition import PCA
import numpy as np
import tensorflow as tf
import cv2
from PIL import Image
import requests
from io import BytesIO
from scipy.spatial.distance import euclidean

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Download Obama and Bush embeddings from GitHub
obama_url = "https://raw.githubusercontent.com/Datbwoyyy/CODSOFT/main/obama_embedding.npy"
bush_url = "https://raw.githubusercontent.com/Datbwoyyy/CODSOFT/main/bush_embedding.npy"

# Function to load embeddings from a URL
def load_embedding(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad responses
    return np.load(BytesIO(response.content))

# Load Obama and Bush embeddings
obama_embedding = load_embedding(obama_url)
bush_embedding = load_embedding(bush_url)

# Function to resize embeddings to a target size
def resize_embedding(embedding, target_size=2048):
    # Apply PCA to reduce the dimensionality to the target size
    pca = PCA(n_components=target_size)
    embedding_resized = pca.fit_transform(embedding.reshape(1, -1)).flatten()
    return embedding_resized

# Function to calculate the Euclidean distance between two embeddings
def compare_embeddings(embedding1, embedding2):
    embedding1_resized = resize_embedding(embedding1)
    embedding2_resized = resize_embedding(embedding2)
    return euclidean(embedding1_resized, embedding2_resized)

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path='face_recognition_model.tflite')
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Class labels (this could also be dynamically fetched from the model)
class_names = ['Barack Obama', 'George Bush', 'Other']

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
        face = cv2.resize(face, (299, 299))  # Inception V3 input size
        face = np.expand_dims(face, axis=0).astype(np.float32) / 255.0

        # Set the input tensor
        interpreter.set_tensor(input_details[0]['index'], face)

        # Run inference
        interpreter.invoke()

        # Get model output
        predictions = interpreter.get_tensor(output_details[0]['index'])

        # Compare embeddings for prediction
        predicted_embedding = predictions[0]  # Assuming predictions are embeddings

        # Calculate Euclidean distance to Obama and Bush embeddings
        obama_distance = compare_embeddings(predicted_embedding, obama_embedding)
        bush_distance = compare_embeddings(predicted_embedding, bush_embedding)

        # Determine if it's Obama or Bush
        if obama_distance < bush_distance:
            predicted_label = "Barack Obama"
        elif bush_distance < obama_distance:
            predicted_label = "George Bush"
        else:
            predicted_label = "Unknown"

        # Draw face box and label
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(image, predicted_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Door animation
    if predicted_label in ["Barack Obama", "George Bush"]:
        st.image(draw_door(opened=True))
    else:
        st.image(draw_door(opened=False))

    # Display image with annotations
    st.image(image, caption="Processed Image", use_column_width=True)
