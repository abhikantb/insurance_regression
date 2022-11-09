import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
import config

#created basic flask app and name is starting point of app where it will run
app=Flask(__name__)

#load the pickle model
insurance_model=pickle.load(open('artifacts/insurance_regression.pkl','rb'))
                

#homepage or localhost url including slash / 
# when you click on url after deployment the first page appears will be home page
#go to main directory or upper hirarchy of website/localhost address
@app.route('/')
def home():
    return render_template('templates/insurance_home.html')


@app.route('/predict',methods=['POST'])
def predict_api():
    age = int(request.form.get('age'))
    sex = int(request.form.get('sex'))
    bmi = int(request.form.get('bmi'))
    quantity = int(request.form.get('quantity'))
    smoker = int(request.form.get('smoker'))
  
    print(age,sex,bmi,quantity,quantity,smoker)
    
    data = np.array([[age,sex,bmi,quantity,quantity,smoker]])
    charges =  insurance_model.predict(data)
    return render_template('insurance_home.html',charges_result=charges)

if __name__ == "__main__":
    app.run(debug=True, host=config.host_name,port=config.port_number)
