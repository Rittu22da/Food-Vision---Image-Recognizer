from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import tensorflow_datasets as tfds

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load trained model
model = tf.keras.models.load_model("model/food_vision_model.h5")

# Class names (Food101 example – change if needed)
# class_names = [
#     "apple_pie","burger","pizza","sushi","ice_cream",
#     # add all your classes here
# ]
class_names = tfds.builder("food101").info.features["label"].names
print("Loaded class names:", len(class_names))


def preprocess_image(img_path):
    img = Image.open(img_path).convert("RGB")
    img = img.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            img = preprocess_image(filepath)
            prediction = model.predict(img)

            pred_index = int(np.argmax(prediction[0]))
            pred_class = class_names[pred_index]
            confidence = float(prediction[0][pred_index]) * 100

            return render_template(
                "result.html",
                image_path=filepath,
                prediction=pred_class,
                confidence=round(confidence, 2)
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
