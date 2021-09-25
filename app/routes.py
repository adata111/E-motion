from app import app
from flask import render_template, jsonify, request, flash, redirect, url_for
# from server.image_captioning import image2caption
from server.txt_to_emo import preprocess, generate_emo
import os
from werkzeug.utils import secure_filename


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

# @app.route('/res', methods=['GET'])
# def txt_to_emo():
#     text = image2caption('./server/img2.jpg')
#     print(text)
#     preds = preprocess(text)
#     response = generate_emo(preds)
#     return jsonify(result=response)

@app.route('/emotion', methods=['POST'])
def txt_to_emo():
    text = request.form
    print(text)
    prediction = preprocess(text)
    response = generate_emo(prediction)
    return render_template("index.html", emotion=str(response))