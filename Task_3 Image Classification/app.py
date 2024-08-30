from flask import Flask, render_template, request, redirect, url_for
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

app = Flask(__name__)
model = load_model('model/cnn_model.h5')

# CIFAR-10 class names
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        img_file = request.files['image']
        img_path = 'static/uploads/' + img_file.filename
        img_file.save(img_path)

        # Predict the class of the uploaded image
        class_idx = predict_image(img_path)
        class_name = class_names[class_idx]

        return render_template('result.html', img_path=img_path, class_name=class_name)
    return render_template('index.html')

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(32, 32))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0) / 255.0
    predictions = model.predict(img)
    class_idx = np.argmax(predictions)
    return class_idx

if __name__ == '__main__':
    app.run(debug=True)
