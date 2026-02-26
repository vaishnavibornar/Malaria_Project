from flask import Flask, render_template, request, jsonify
import numpy as np
import os
from datetime import datetime
from PIL import Image
import tensorflow as tf

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

CLASS_NAMES = ["Parasitized", "Uninfected"]

# ================= MODEL LOADING =================
MODEL_PATH = "malaria_model.h5"

print("Loading model...")
model = tf.keras.models.load_model(MODEL_PATH)
print("✅ Model Loaded Successfully")

# ================= PREPROCESS =================
def prepare_image(image_file):
    img = Image.open(image_file).convert("RGB")

    input_shape = model.input_shape
    img_size = (input_shape[1], input_shape[2])

    img = img.resize(img_size)
    img_array = np.array(img, dtype="float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    return img_array

# ================= HOME =================
@app.route("/")
def home():
    return render_template("index.html")

# ================= PREDICT =================
@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return jsonify({"success": False})

    file = request.files["file"]

    img_array = prepare_image(file)

    prediction = model.predict(img_array, verbose=0)
    prob = float(prediction[0][0])

    if prob > 0.5:
        pred_class = 1
        confidence = prob * 100
    else:
        pred_class = 0
        confidence = (1 - prob) * 100

    result = CLASS_NAMES[pred_class]

    return jsonify({
        "success": True,
        "prediction": result,
        "confidence": round(confidence, 2),
        "parasitized_probability": round((1-prob)*100,2),
        "uninfected_probability": round(prob*100,2),
        "timestamp": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    })

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)