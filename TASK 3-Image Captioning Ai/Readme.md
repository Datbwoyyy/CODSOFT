# Image Captioning Project

This project implements an AI-based image captioning system that combines **Computer Vision (CV)** and **Natural Language Processing (NLP)** techniques to generate descriptive captions for images. It leverages **pre-trained ResNet50** for image feature extraction and a **Recurrent Neural Network (RNN)** for text generation. The system is designed to efficiently handle large datasets by streaming images from the **MS COCO dataset**.

---

## Dataset Information

- **Dataset Name**: MS COCO 2017
- **Source**: [Kaggle - MS COCO 2017 Dataset](https://www.kaggle.com/datasets/sabahesaraki/2017-2017)
- **License**: Creative Commons Attribution 4.0 License (CC BY 4.0)
- **Description**: The MS COCO dataset contains a variety of images with human-annotated captions, used for object detection, segmentation, and image captioning tasks.

---

## Project Features

- **Image feature extraction** using **ResNet50**.
- **Caption generation** using an **RNN-based or Transformer-based model**.
- **Online image streaming** to reduce computational load.
- **Proper attribution to all datasets and models used**.

---

## 📦 Requirements

- Python 3.7+
- TensorFlow
- NumPy
- Pandas
- PIL (Python Imaging Library)
- Requests

To install the dependencies, run:
```bash
pip install -r requirements.txt
```

---

##  How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/image-captioning.git
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the main script**:
   ```bash
   python image_captioning.py
   ```

---

##  References and Credits

1. **MS COCO Dataset**:
   - **Title**: MS COCO 2017 Dataset
   - **Source**: [Kaggle - MS COCO 2017 Dataset](https://www.kaggle.com/datasets/sabahesaraki/2017-2017)
   - **License**: Creative Commons Attribution 4.0 License (CC BY 4.0)
   - **Description**: A large-scale dataset for object detection, segmentation, and captioning.

2. **ResNet50 Pre-trained Model**:
   - **Source**: [Keras Applications](https://keras.io/api/applications/resnet/)
   - **Description**: A pre-trained Convolutional Neural Network model provided by TensorFlow's Keras library.

3. **TensorFlow Documentation**:
   - **Source**: [https://www.tensorflow.org](https://www.tensorflow.org)
   - **Description**: Official documentation for TensorFlow, an open-source machine learning framework.

4. **Kaggle**:
   - **Source**: [https://www.kaggle.com](https://www.kaggle.com)
   - **Description**: Platform for sharing datasets and machine learning models.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

##  Disclaimer

This project is for **educational purposes only**. The datasets, models, and libraries used are the property of their respective owners. Please ensure compliance with licensing agreements before commercial use.

