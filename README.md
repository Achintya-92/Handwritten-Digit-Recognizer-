# Handwritten Digit Recognizer

A handwritten digit recognition project using a **CNN trained on the MNIST dataset**, with a web interface that allows users to draw digits on a canvas and get predictions through a Flask API.

## Project Overview

The project has three main parts:

1. **CNN Model**
   - TensorFlow / Keras
   - Trained on MNIST
   - Input: `28 × 28` grayscale image
   - Output: digit `0–9`

2. **Flask Backend**
   - Receives canvas images from the frontend
   - Decodes Base64 PNG images
   - Converts and preprocesses the image
   - Sends the image to the CNN
   - Returns predicted digit and confidence

3. **Web Frontend**
   - HTML/CSS/JavaScript
   - Provides a drawing canvas
   - Sends the canvas image to the Flask API
   - Displays the prediction

---

## Project Structure

```text
Handwritten Digit Recognizer/
│
├── api/
│   └── app.py
│
├── Web/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── data/
│   └── my_digits/
│       ├── 0/
│       ├── 1/
│       ├── 2/
│       ├── 3/
│       ├── 4/
│       ├── 5/
│       ├── 6/
│       ├── 7/
│       ├── 8/
│       └── 9/
│
├── mnist_cnn.keras
├── train.py
└── README.md
````

---

# Current Model

The current CNN is trained on MNIST.

Basic architecture:

```text
Input: 28 × 28 × 1
        ↓
Conv2D(32)
        ↓
MaxPooling
        ↓
Conv2D(64)
        ↓
Flatten
        ↓
Dense(128)
        ↓
Dense(10, Softmax)
```

The original model achieved approximately:

```text
MNIST Test Accuracy ≈ 99.1%
```

---

# Web Prediction Pipeline

The frontend creates a PNG image from the canvas.

```text
Canvas
   ↓
canvas.toDataURL()
   ↓
Base64 PNG
   ↓
POST /api/predict
   ↓
Flask
   ↓
Base64 Decode
   ↓
PIL Image
   ↓
Grayscale
   ↓
Crop handwritten digit
   ↓
Resize to 28 × 28
   ↓
Normalize 0–1
   ↓
CNN
   ↓
Prediction
```

Example API response:

```json
{
    "message": "Image Prediction successful.",
    "predicted_digit": 7,
    "confidence": 0.9171
}
```

---

# API

## POST `/api/predict`

The frontend sends:

```json
{
    "image": "data:image/png;base64,..."
}
```

The backend processes the image and returns:

```json
{
    "predicted_digit": 7,
    "confidence": 0.9171
}
```

---

# CORS

The frontend and backend run on different ports during development.

Frontend:

```text
http://127.0.0.1:5500
```

Backend:

```text
http://127.0.0.1:5000
```

Therefore, CORS is enabled in Flask.

---

# Custom Handwritten Dataset

The original MNIST model performs very well on MNIST, but handwritten digits created by a real user can have significantly different shapes.

For example, different handwritten versions of `9` can look like:

```text
    ○
     \
      \
```

or:

```text
    ___
   /   \
       |
       |
```

Some valid `9` images can therefore be confused with `8`, `4`, `5`, `7`, `3`, etc.

To improve performance on personal handwriting, a custom dataset will be added.

---

# Custom Dataset Structure

Each digit has its own folder.

```text
data/
└── my_digits/
    ├── 0/
    │   ├── 0_01.png
    │   ├── 0_02.png
    │   └── ...
    │
    ├── 1/
    ├── 2/
    ├── 3/
    ├── 4/
    ├── 5/
    ├── 6/
    ├── 7/
    ├── 8/
    └── 9/
```

The folder name is the label.

For example:

```text
my_digits/9/9_01.png
```

means:

```text
label = 9
```

---

# Custom Image Preprocessing

Custom images will be converted to the same format expected by the CNN:

```text
PNG
 ↓
Grayscale
 ↓
28 × 28
 ↓
Pixel values / 255
 ↓
Shape: (28, 28, 1)
```

The preprocessing must be consistent with the training and prediction pipeline.

---

# Retraining Plan

The next stage of the project is to combine:

```text
MNIST Training Data
        +
Custom Handwritten Images
        ↓
Combined Dataset
        ↓
Train CNN
        ↓
Validate
        ↓
Evaluate on untouched MNIST Test Set
```

The MNIST test set must remain separate.

This allows us to compare:

```text
Old Model
    vs
Retrained Model
```

---

# Important Evaluation Rule

Do not evaluate the model using images that were used during training.

We will maintain:

```text
Training data
    ↓
Used to train model

Validation data
    ↓
Used during training to monitor performance

Test data
    ↓
Never used for training
```

This helps determine whether the model actually generalizes.

---

# Planned Training Pipeline

The custom images will eventually be loaded using Python:

```python
x_custom, y_custom = load_custom_images(
    "data/my_digits"
)
```

MNIST will be loaded using:

```python
(x_train, y_train), (x_test, y_test) = \
    tf.keras.datasets.mnist.load_data()
```

Then the training datasets will be combined:

```python
x_combined = np.concatenate(
    [x_train, x_custom],
    axis=0
)

y_combined = np.concatenate(
    [y_train, y_custom],
    axis=0
)
```

The test set will remain untouched.

---

# Data Augmentation

The model may use augmentation to make it more robust to handwriting variations.

Possible augmentations:

```text
Rotation
Translation
Zoom
```

For example:

```python
data_augmentation = tf.keras.Sequential([
    layers.RandomRotation(0.05),
    layers.RandomTranslation(0.08, 0.08),
    layers.RandomZoom(0.08)
])
```

Augmentation will be used carefully so that the digit's identity is not changed.

---

# Model Saving

After retraining:

```python
model.save("mnist_cnn_custom.keras")
```

The Flask backend can then load:

```python
model = tf.keras.models.load_model(
    "mnist_cnn_custom.keras"
)
```

---

# Current Development Status

* [x] MNIST dataset loaded
* [x] CNN trained
* [x] MNIST evaluation completed
* [x] Flask backend created
* [x] `/api/predict` endpoint created
* [x] CORS issue resolved
* [x] Canvas image sent from JavaScript
* [x] Base64 image decoded in Flask
* [x] Image converted to grayscale
* [x] Image cropped
* [x] Image resized to `28 × 28`
* [x] CNN prediction working
* [x] Prediction and confidence returned to frontend
* [x] Wrong MNIST predictions analyzed
* [ ] Custom handwritten dataset creation
* [ ] Custom PNG loading
* [ ] MNIST + custom dataset combination
* [ ] Retraining
* [ ] Evaluation of retrained model
* [ ] Testing custom canvas handwriting
* [ ] Final frontend polishing

---

# Important Learning Goal

The purpose of this project is not only to build a working digit recognizer.

It is also to understand the complete machine-learning pipeline:

```text
Dataset
   ↓
Preprocessing
   ↓
Training
   ↓
Validation
   ↓
Testing
   ↓
Model Saving
   ↓
API
   ↓
Frontend
   ↓
Real-world Prediction
```

A major focus is understanding why a model can achieve very high MNIST accuracy but still perform poorly on handwritten digits drawn by a user.

---

# Future Improvements

Possible future improvements:

* Add more custom handwritten samples
* Balance custom samples across all digits
* Improve image centering
* Match canvas preprocessing with MNIST preprocessing
* Fine-tune the pretrained MNIST model on custom handwriting
* Analyze confusion matrix after retraining
* Add prediction confidence to UI
* Add loading state
* Add error handling
* Deploy frontend and backend

````

Save this as:

```text
README.md
````

**Current next step remains Step 1:** create `data/my_digits/0` through `data/my_digits/9` and put your handwritten images into the appropriate folders. When you return, we’ll continue from **Step 2**, not restart anything.
#   H a n d w r i t t e n - D i g i t - R e c o g n i z e r -  
 