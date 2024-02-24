  <h3 align="center">Water Cleanliness Prediction ML Web App</h3>

  <p align="center">
    Empowering communities with data-driven decisions for safer, cleaner water sources!
    <a href="https://github.com/admin-sauce/Water-Cleanliness-Prediction-ML-Web-App"></a>
    <br/>
    <br/>
    <a href="https://github.com/admin-sauce/Water-Cleanliness-Prediction-ML-Web-App/issues">Report Bug</a>
    .
    <a href="https://github.com/admin-sauce/Water-Cleanliness-Prediction-ML-Web-App/issues">Request Feature</a>
  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/admin-sauce/Water-Cleanliness-Prediction-ML-Web-App?color=dark-green) ![Issues](https://img.shields.io/github/issues/admin-sauce/Water-Cleanliness-Prediction-ML-Web-App) ![License](https://img.shields.io/github/license/admin-sauce/Water-Cleanliness-Prediction-ML-Web-App) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Explanation Video](#explanation-video)
* [License](#license)
* [Authors](#authors)

## About The Project

![pic-1](https://github.com/admin-sauce/Water-Cleanliness-Prediction-ML-Web-App/assets/127975274/511ece6b-46b6-491e-8352-9a86277581fe)
![pic-2](https://github.com/admin-sauce/Water-Cleanliness-Prediction-ML-Web-App/assets/127975274/15723b5a-af2c-431a-af54-4742756da35a)
![pic-3](https://github.com/admin-sauce/Water-Cleanliness-Prediction-ML-Web-App/assets/127975274/3a2896a3-273c-4668-9d2e-e08a3c39237d)

The Water Potability Prediction project is a web application designed to assist in evaluating the drinkability of water resources based on various scientific parameters. Users input data on 23 specific factors related to water quality, including pH levels, chlorine content, and manganese concentration. Leveraging machine learning techniques, the application employs the DecisionTreeClassifier algorithm to classify water as potable or non-potable with an accuracy score of 87%.

## Built With

* Frontend: Flask, HTML, CSS
* Machine Learning: scikit-learn (for the DecisionTreeClassifier algorithm)
* Data Serialization: Pickle
* Scientific Computing: NumPy

## Getting Started

To start the project, clone the repository, install dependencies using pip install -r requirements.txt, then run the Flask app with python app.py. Access the app in your browser at http://localhost:5000, input the 23 water quality parameters, and click 'Predict' to classify water potability

### Prerequisites

* Flask
* Numpy
* Scikit Learn

### Installation

**Setting Up Your Project Locally**

To get a local copy up and running, follow these simple steps:

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/admin-sauce/Water-Cleanliness-Prediction-ML-Web-App.git
   ```

2. **Navigate to the Project Directory:**
   ```sh
   cd Water-Cleanliness-Prediction-ML-Web-App
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Flask App:**
   ```sh
   python app.py
   ```

5. **Access the Web Application:**
   Open your web browser and go to `http://localhost:5000` or `http://127.0.0.1:5000` to access the application

6. **Input Parameters:**
   Enter values for the 23 scientific parameters related to water quality

7. **Predict Water Potability:**
   Click the 'Predict' button to classify the water as drinkable or not based on the input parameters

8. **View Results:**
   The application will display a message indicating the drinkability of the water

## Explanation Video

https://youtu.be/pQSLLXEFiBE

## License

Distributed under the GNU General Public License v3.0 License. See [LICENSE](https://github.com/admin-sauce/Water-Cleanliness-Prediction-ML-Web-App/blob/master/LICENSE) for more information.

## Authors

[Abishek ](https://github.com/MLAbishek) </br>
[Rishon Jos Anton](https://github.com/RishonAnton) </br>
[Thomas Albert Iwin](https://github.com/admin-sauce)

