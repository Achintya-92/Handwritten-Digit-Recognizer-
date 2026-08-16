# ✍️ Handwritten Digit Recognizer

A web-based handwritten digit recognition system that uses a **Convolutional Neural Network (CNN)** trained on the **MNIST dataset**.

Users can draw a digit directly on a web canvas, and the trained model predicts the digit through a **Flask REST API**.

---

## 🚀 Demo

Draw a digit on the canvas:

```text
        ┌──────────────────┐
        │                  │
        │        7         │
        │                  │
        └──────────────────┘
                 ↓
          Flask REST API
                 ↓
             CNN Model
                 ↓
          Predicted: 7
          Confidence: 91.7%
````

---

## ✨ Features

* 🖊️ Draw digits directly on a web canvas
* 🤖 CNN-based digit classification
* 🧠 Trained using the MNIST dataset
* 🔌 Flask REST API for model inference
* 📡 JavaScript `fetch()` API communication
* 🖼️ Base64 image transmission
* 🔍 Automatic image preprocessing
* 📏 Image resizing to `28 × 28`
* 📊 Prediction confidence
* 🔄 Custom handwritten dataset support
* 🌐 CORS-enabled frontend/backend communication

---

## 🛠️ Tech Stack

| Technology         | Purpose                    |
| ------------------ | -------------------------- |
| Python             | Backend & ML               |
| TensorFlow / Keras | CNN model                  |
| NumPy              | Numerical processing       |
| Pillow             | Image processing           |
| Flask              | REST API                   |
| Flask-CORS         | Cross-Origin requests      |
| HTML               | Web structure              |
| CSS                | Styling                    |
| JavaScript         | Canvas & API communication |

---

## 🧠 Model Architecture

The CNN uses the following architecture:

```text
Input
28 × 28 × 1
     │
     ▼
Conv2D (32 filters)
     │
     ▼
MaxPooling
     │
     ▼
Conv2D (64 filters)
     │
     ▼
Flatten
     │
     ▼
Dense (128)
     │
     ▼
Dense (10)
     │
     ▼
Softmax
     │
     ▼
Digit 0–9
```

---

## 📊 MNIST Performance

The initial model achieved approximately:

```text
MNIST Test Accuracy: 99.1%
```

Test set:

```text
10,000 images
```

Wrong predictions:

```text
90 images
```

The confusion matrix was also analyzed to understand which digits were commonly confused.

---

## 🔄 Prediction Pipeline

```text
User draws digit
       │
       ▼
HTML Canvas
       │
       ▼
canvas.toDataURL()
       │
       ▼
Base64 PNG
       │
       ▼
POST /api/predict
       │
       ▼
Flask Backend
       │
       ▼
Base64 Decode
       │
       ▼
Pillow Image
       │
       ▼
Grayscale
       │
       ▼
Crop Digit
       │
       ▼
Resize → 28 × 28
       │
       ▼
Normalize → 0–1
       │
       ▼
CNN Model
       │
       ▼
Prediction
       │
       ▼
Frontend
```

---

## 📡 API

### `POST /api/predict`

The frontend sends the canvas image as a Base64 encoded PNG.

### Request

```json
{
  "image": "data:image/png;base64,..."
}
```

### Response

```json
{
  "message": "Image Prediction successful.",
  "predicted_digit": 7,
  "confidence": 0.9171
}
```

---

## 📁 Project Structure

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
├── src/
│   └── ...
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
├── README.md
├── .gitignore
└── requirements.txt
```

---

## 🧪 Custom Handwritten Dataset

The project also supports adding personal handwritten images.

Images are organized according to their labels:

```text
data/my_digits/
│
├── 0/
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

For example:

```text
data/my_digits/9/
├── 9_01.png
├── 9_02.png
├── 9_03.png
└── ...
```

The folder name represents the digit label.

The plan is to combine these images with MNIST and retrain/fine-tune the CNN so that it performs better on real user handwriting.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd "Handwritten Digit Recognizer"
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Backend

```bash
python api/app.py
```

The Flask server will run at:

```text
http://127.0.0.1:5000
```

---

## 🌐 Run the Frontend

Open the `Web/index.html` using a local development server.

For example, VS Code Live Server:

```text
http://127.0.0.1:5500
```

The frontend communicates with:

```text
http://127.0.0.1:5000/api/predict
```

---

## 🔐 Git & Data

Personal handwritten images and local environment files are excluded using `.gitignore`.

Ignored files include:

```text
.venv/
data/
*.keras
.env
__pycache__/
```

---

## 📚 What I Learned

This project helped me understand the complete machine-learning application pipeline:

```text
Dataset
   ↓
Preprocessing
   ↓
CNN Training
   ↓
Evaluation
   ↓
Model Saving
   ↓
Flask API
   ↓
Frontend
   ↓
Real-time Prediction
```

It also helped me understand an important real-world ML problem:

> A model can achieve very high accuracy on a benchmark dataset like MNIST but still perform differently on images coming from a real user interface.

---

## 🔮 Future Improvements

* [ ] Add more personal handwriting samples
* [ ] Combine MNIST with custom handwritten data
* [ ] Fine-tune the CNN on personal handwriting
* [ ] Improve canvas image preprocessing
* [ ] Improve digit centering and scaling
* [ ] Add prediction visualization
* [ ] Improve UI/UX
* [ ] Deploy the application

---

## 👨‍💻 Author

**Lovejot Singh**

Built as a practical Machine Learning + Web Development project.

````






