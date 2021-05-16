from flask import Flask, url_for , request , render_template
import numpy as np 
from joblib import load
app = Flask(__name__)
model = load("basic_model.joblib")
@app.route('/')
@app.route('/home')
def index_page():
    return render_template('index.html')
@app.route('/predict' , methods=['POST'])
def predict():
    userform = request.form
    print(userform)
    anaemia= userform['anaemia']
    sex= userform['sex']
    platelets= userform['platelets']
    age= userform['age']
    diabetes= userform['diabetes']
    highbp= userform['highbp']
    smoking= userform['smoking']
    test=[[anaemia,sex,platelets,age,diabetes,highbp,smoking]]
    pred = model.predict(test)
    label=pred[0]
    msg=" "
    if label==0:
        msg="You are Healthy" 
    elif label==1:
        msg="You seem to be Unhealthy."
    
     
    return render_template('result.html',pred=msg,label=label)
if __name__== "__main__" :
    app.run(debug=True)
    