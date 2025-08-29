import numpy as np
from flask import Flask,request, jsonify,render_template,redirect,url_for
import pickle


app=Flask(__name__)
model=pickle.load(open('crop_recommendation_model.pkl','rb'))

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/predict',methods=["POST"])
def predict():
    float_features=[float(x) for x in request.form.values()]
    features=[np.array(float_features)]
    Prediction=model.predict(features)
    return render_template("index.html",prediction_text='Recommended Crop is:{}'.format(Prediction))

if __name__=='__main__':
    app.run(debug=True)