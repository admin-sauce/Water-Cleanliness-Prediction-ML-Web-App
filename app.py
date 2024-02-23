from flask import Flask, render_template, request
import pickle
import numpy as np
from werkzeug.exceptions import BadRequestKeyError

app = Flask(__name__)

month_dict = {
    "April": 0,
    "August": 1,
    "December": 2,
    "February": 3,
    "January": 4,
    "July": 5,
    "June": 6,
    "March": 7,
    "May": 8,
    "November": 9,
    "October": 10,
    "September": 11
}

color_of_water = {
    "Colorless": 0,
    "Faint Yellow": 1,
    "Light Yellow": 2,
    "Near Colorless": 3,
    "Yellow": 4
}

water_body = {
    "Aquifer": 0,
    "Ground": 1,
    "Lake": 2,
    "Reservoir": 3,
    "River": 4,
    "Spring": 5,
    "Stream": 6,
    "Well": 7
}

def predict(dataset):
    with open("model.pickle", "rb") as f:
        classifier = pickle.load(f)
    ans = classifier.predict(dataset)
    if ans == 1:
        return "drinkable water"
    else:
        return "not drinkable"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def get_prediction():
    try:
        ph = float(request.form['ph'])
        iron = float(request.form['iron'])
        nitrate = float(request.form['nitrate'])
        chloride = float(request.form['chloride'])
        lead = float(request.form['lead'])
        zinc = float(request.form['zinc'])
        turbidity = float(request.form['turbidity'])
        color = request.form['color']
        color = color_of_water.get(color)
        fluoride = float(request.form['fluoride'])
        copper = float(request.form['copper'])
        odor = float(request.form['odor'])
        sulphate = float(request.form['sulphate'])
        conductivity = float(request.form['conductivity'])
        chlorine = float(request.form['chlorine'])
        manganese = float(request.form['manganese'])
        total_dissolved_solids = float(request.form['total_dissolved_solids'])
        source = request.form['source']
        source = water_body.get(source)
        water_temperature = float(request.form['water_temperature'])
        air_temperature = float(request.form['air_temperature'])
        month = request.form['month']
        month = month_dict.get(month)
        date = int(request.form['date'])
        time_of_the_day = int(request.form['time_of_the_day'])

    except BadRequestKeyError as e:
        print("Bad request. Missing form data:", e)
        return "Bad request. Please check your form data.", 400
    except Exception as e:
        print("An error occurred:", e)
        return "Internal server error.", 500
    
    question = [
        ph, 
        iron,
        nitrate,
        chloride, 
        lead, 
        zinc, 
        color, 
        turbidity,
        fluoride, 
        copper, 
        odor, 
        sulphate, 
        conductivity, 
        chlorine,
        manganese, 
        total_dissolved_solids, 
        source, water_temperature,
        air_temperature, 
        month, 
        date, 
        time_of_the_day
    ]
    question = np.array(question).reshape(1, -1)

    prediction = predict(question)
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
