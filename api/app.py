import tensorflow as tf
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import io
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
app = Flask(__name__)

CORS(app)

model = tf.keras.models.load_model("mnist_cnn.keras")


@app.route("/api/predict", methods=["POST", "OPTIONS"])
def predict():

    if request.method == "OPTIONS":
        return "", 200

    data = request.get_json()

    # Base64 string
    image_data = data["image"]

    # "data:image/png;base64,"
    image_data = image_data.split(",")[1]

    # Base64 → bytes
    image_bytes = base64.b64decode(image_data)

    # bytes → PIL Image
    image = Image.open(io.BytesIO(image_bytes))

    image = image.convert("L")

    image_array = np.array(image)

# White pixels search
    coords = np.argwhere(image_array > 20)

    if coords.size == 0:
     return jsonify({"error": "No digit detected"}), 400

    y_min, x_min = coords.min(axis=0)
    y_max, x_max = coords.max(axis=0)

    # padding
    padding = 20

    y_min = max(0, y_min - padding)
    y_max = min(image_array.shape[0], y_max + padding)

    x_min = max(0, x_min - padding)
    x_max = min(image_array.shape[1], x_max + padding)

# Crop
    image = image.crop((x_min, y_min, x_max + 1, y_max + 1))

# Resize only once
    image = image.resize((28, 28))


    image.save("received_image.png")

    image_array = np.array(image)

    print("Processed shape:", image_array.shape)
    print("Min:", image_array.min())
    print("Max:", image_array.max())

    image_array = image_array.astype("float32") / 255.0
    image_array = image_array.reshape(1, 28, 28, 1)

    prediction = model.predict(image_array)

    predicted_digit = int(np.argmax(prediction))

    confidence = round(float(np.max(prediction)),3)
    print( predicted_digit)
    return jsonify({
        "message": "Image Prediction successfull.",
        "predicted_digit": predicted_digit,
        "confidence": confidence
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)