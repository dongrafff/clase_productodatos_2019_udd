from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
from pathlib import Path



# Import fast.ai Library
from fastai import *
from fastai.vision import *

# Flask utils hace posible la aplicacion web
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename


# Define a flask app
app = Flask(__name__)

# aca se carga el modelo
path = Path("models")
learn = load_learner(path)



# le paso una imagen la carga en memoria y predice que es
def model_predict(img_path):
    """
       model_predict will return the preprocessed image
    """
   
    img = open_image(img_path)
    pred_class,pred_idx,outputs = learn.predict(img)
    return str(pred_class)
    



# esto es lo qeu hace, al entrar anda al index.html y muestra esto, el como se ve la pagina web esta declado aca
# este index.html se puede modificar a su gusto
@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path)
        return preds
    return None


if __name__ == '__main__':
    
    app.run()


