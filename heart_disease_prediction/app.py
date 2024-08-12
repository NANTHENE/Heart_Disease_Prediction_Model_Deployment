# Importing essential libraries
from flask import Flask, render_template, request
import requests
import numpy as np

app = Flask(__name__)
API_KEY = "<API-Key>"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + "<Access_Token>"}

@app.route('/')
def home():
	return render_template('main.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':

        age = int(request.form['age'])
        sex = request.form.get('sex')
        cp = request.form.get('cp')
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = request.form.get('fbs')
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = request.form.get('exang')
        oldpeak = float(request.form['oldpeak'])
        slope = request.form.get('slope')
        ca = int(request.form['ca'])
        thal = request.form.get('thal')
        
        data = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        data_list=data.tolist()
        
        payload_scoring = {"input_data": [{"fields": ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal'], "values": [data_list]}]}
        response_scoring = requests.post("https://private.eu-de.ml.cloud.ibm.com/ml/v4/deployments/<Deployment_ID>/predictions?version=2021-05-01", json=payload_scoring, headers=header)
        if response_scoring.status_code == 200:
            output = response_scoring.json()['prediction']
            return render_template('result.html', prediction=output)
        else:
            return render_template('result.html', prediction="error")

if __name__ == '__main__':
	app.run(debug=True)
import requests

