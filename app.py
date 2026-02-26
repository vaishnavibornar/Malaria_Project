from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

model = tf.keras.models.load_model("malaria_model.keras")

classes = ['Parasitized','Uninfected']

def predict_img(img_path):
    img = image.load_img(img_path, target_size=(224,224))
    img = image.img_to_array(img)/255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)
    return classes[int(pred[0][0] > 0.5)]

@app.route("/", methods=["GET","POST"])
def home():
    result = None
    if request.method == "POST":
        file = request.files["file"]
        path = "static/" + file.filename
        file.save(path)
        result = predict_img(path)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)