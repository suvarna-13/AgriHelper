from flask import Flask,render_template,request
import pickle
import numpy as np
import sklearn


model = pickle.load(open('rf_pipeline.pkl','rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    Temperature = (request.form.get('Temperature'))
    Humidity = (request.form.get('Humidity'))
    Moisture = (request.form.get('Moisture'))
    SoilType = (request.form.get('soil_type'))
    CropType = (request.form.get('crop_type'))
    Nitrogen = (request.form.get('Nitrogen'))
    Potassium = (request.form.get('Potassium'))
    Phosphorous = (request.form.get('Phosphorous'))

    # prediction
    result = model.predict(np.array([[Temperature,Humidity,Moisture,SoilType,CropType,Nitrogen,Potassium,Phosphorous]]))
    if result[0] == 0:
        result = 'Fertilizer name: 10-26-26'
    elif result[0] == 1:
        result = 'Fertilizer name: 14-35-14'
    elif result[0] == 2:
        result = 'Fertilizer name: 17-17-17'
    elif result[0] == 3:
        result = 'Fertilizer name: 20-20'
    elif result[0] == 4:
        result = 'Fertilizer name: 28-28'
    elif result[0] == 5:
        result = 'Fertilizer name: DAP'
    else:
        result = 'Fertilizer name: UREA '




    return render_template('index.html',result=str(result))


if __name__ == '__main__':
    app.run(port=5001,debug=True)

