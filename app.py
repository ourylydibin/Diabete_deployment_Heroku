from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
from flask_cors import CORS, cross_origin
app = Flask(__name__)
model = joblib.load(open('rand_model.pickle', 'rb'))
CORS(app)
@app.route('/')
@cross_origin()
def hello_world():
    return render_template("home.html")

@app.route("/banknote", methods=["GET", "POST"])
def predict():
    feature = [np.array([float(x) for x in request.form.values()])]
    #re.columns = ["variance", "skewness", "curtosis", "entropy"]
    prediction = model.predict(feature)
    if prediction==1:
        result = 1
    else:
        result = 0
    return render_template("result.html", result=result)
if __name__=="__main__":
    app.run(debug=True)