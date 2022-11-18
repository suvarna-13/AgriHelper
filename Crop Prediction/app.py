from flask import Flask,render_template,request
import pickle
import numpy as np
import sklearn

model = pickle.load(open('xgb_pipeline.pkl','rb'))

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    Temperature = (request.form.get('Temperature'))
    Humidity = (request.form.get('Humidity'))
    Rainfall = (request.form.get('Rainfall'))
    Ph = (request.form.get('Ph'))
    Nitrogen = (request.form.get('Nitrogen'))
    Potassium = (request.form.get('Potassium'))
    Phosphorous = (request.form.get('Phosphorous'))

    # prediction
    result = model.predict(np.array([[Nitrogen,Potassium,Phosphorous,Temperature,Humidity,Ph,Rainfall]]))
    if result[0] == 0:
        result = 'Crop Name: Apple'
    elif result[0] == 1:
        result = 'Crop Name: Banana'
    elif result[0] == 2:
        result = 'Crop Name: Blackgram'
    elif result[0] == 3:
        result = 'Crop Name: Chickpea'
    elif result[0] == 4:
        result = 'Crop Name: Coconut'
    elif result[0] == 5:
        result = 'Crop Name: Coffee'
    elif result[0] == 6:
        result = 'Crop Name: Cotton'
    elif result[0] == 7:
        result = 'Crop Name: Grapes'
    elif result[0] == 8:
        result = 'Crop Name: Jute'
    elif result[0] == 9:
        result = 'Crop Name: Kidneybeans'
    elif result[0] == 10:
        result = 'Crop Name: Lentil'
    elif result[0] == 11:
        result = 'Crop Name: Maize'
    elif result[0] == 12:
        result = 'Crop Name: Mango'
    elif result[0] == 13:
        result = 'Crop Name: Mothbeans'
    elif result[0] == 14:
        result = 'Crop Name: Mungbean'
    elif result[0] == 15:
        result = 'Crop Name: Musk Melon'
    elif result[0] == 16:
        result = 'Crop Name: Orange'
    elif result[0] == 17:
        result = 'Crop Name: Papaya'
    elif result[0] == 18:
        result = 'Crop Name: Pigeonpeas'
    elif result[0] == 19:
        result = 'Crop Name: Pomegranate'
    elif result[0] == 20:
        result = 'Crop Name: rice'
    else:
        result = 'Crop Name: watermelon'




    return render_template('index.html',result=str(result))


if __name__ == '__main__':
    app.run(debug=True)