import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
import config

#created basic flask app and name is starting point of app where it will run
app=Flask(__name__,template_folder='templates')

#load the pickle model
insurance_model=pickle.load(open(config.model_path,'rb'))
                

#homepage or localhost url including slash / 
# when you click on url after deployment the first page appears will be home page
#go to main directory or upper hirarchy of website/localhost address
@app.route('/')
def home():
    return render_template('insurance_home.html')


@app.route('/predict',methods=['POST'])
def predict_api():
    age = int(request.form.get('age'))
    sex = request.form.get('sex')
    bmi = int(request.form.get('bmi'))
    children = int(request.form.get('children'))
    smoker = request.form.get('smoker')
    region= request.form.get('region')

    print(age,sex,bmi,children,smoker,region)
    
    input_data=pd.DataFrame(data=[[age,sex,bmi,children,smoker,region]],columns=['age','sex','bmi','children','smoker','region'])
    print(input_data)
    charges =  insurance_model.predict(input_data)
  
    return render_template('insurance_home.html',charges_result='Insurance charges are {}'.format(float(charges)))

if __name__ == "__main__":
    app.run(debug=True)

    
   # app.run(debug=True, host=config.host_name,port=config.port_number)
