# Face Detection and Recognition - README and Reference

## Overview
This project implements a face detection and recognition system using Haar Cascade and FaceNet. It uses a TensorFlow SavedModel for extracting embeddings and a Tkinter-based GUI for user interaction. Recognized faces can trigger actions such as opening a virtual door.

## Project Structure
```
Face Detection And Recognition/
|-- app.py                         # Main application script
|-- saved_model.pb                 # TensorFlow SavedModel file
|-- variables/                     # TensorFlow model variables
|   |-- variables.data-00000-of-00001
|   |-- variables.index
|-- embeddings/                    # Folder containing precomputed embeddings
|   |-- obama_embedding.npy
|   |-- george_bush_embedding.npy
|-- images/                        # Folder containing UI images
|   |-- door_opened.jpg
|   |-- door_closed.jpg
```

## Requirements
- Python 3.8 or higher
- TensorFlow 2.x
- NumPy
- OpenCV
- PIL (Pillow)
- Tkinter (included with most Python installations)

Install the required Python libraries:
```bash
pip install tensorflow numpy opencv-python pillow
```

## How to Run
1. **Prepare the Model**:
   - Ensure `saved_model.pb` and the `variables/` folder are correctly placed in the project directory.
   - Verify the structure of the SavedModel is intact.

2. **Load Known Embeddings**:
   - Place `.npy` files containing embeddings of known individuals in the `embeddings/` folder.
   - Ensure the paths in `app.py` correctly point to these files.

3. **Run the Application**:
   - Execute the `app.py` script:
     ```bash
     python app.py
     ```
   - This will open a GUI where you can upload images for recognition.

4. **Use the GUI**:
   - Click the **Upload Image** button to select an image.
   - The system will detect faces, compare embeddings, and display results on the GUI.

## Key Functions in `app.py`

### Preprocessing
```python
def preprocess_image(image):
    image = cv2.resize(image, (160, 160))
    image = (image - 127.5) / 128.0
    return np.expand_dims(image, axis=0)
```
Prepares images for input to the FaceNet model.

### Face Detection
```python
def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces
```
Detects faces in the input image using Haar Cascade.

### Embedding Extraction
```python
def get_embeddings(face_image):
    preprocessed_image = preprocess_image(face_image)
    embeddings = inference_fn(tf.constant(preprocessed_image, dtype=tf.float32))["Bottleneck_BatchNorm"].numpy()
    return embeddings
```
Extracts embeddings using the FaceNet model.

### Face Recognition
```python
def recognize_face(image):
    faces = detect_faces(image)
    if len(faces) == 0:
        return None, "No face detected!"

    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        embeddings = get_embeddings(face)

        threshold = 0.8
        for name, known_emb in known_embeddings.items():
            distance = euclidean_distance(embeddings, known_emb)
            if distance < threshold:
                return name, f"Match found: {name}"

    return None, "No match found!"
```
Matches detected faces with known embeddings.

## Debugging Tips
- **Model Not Loading**: Ensure `saved_model.pb` and `variables/` are correctly placed.
- **Embeddings Issue**: Check the contents of `.npy` files and validate paths.
- **Face Not Detected**: Ensure Haar Cascade XML is available and correctly loaded.
- **Recognition Threshold**: Adjust the threshold to fine-tune matching sensitivity.

## References
- Haar Cascade: [OpenCV Documentation](https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html)
- FaceNet: [Google Research Blog](https://research.google/pubs/pub45610/)
- TensorFlow SavedModel: [TensorFlow Documentation](https://www.tensorflow.org/guide/saved_model)
- GUI: [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

