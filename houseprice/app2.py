from flask import Flask, render_template, request
import pandas as pd
import pickle


app = Flask(__name__)

#Load Models


model_names = ["LinearRegression", "RobustRegression", "RidgeRegression", "LassoRegression", "ElasticNet",
               "PolynomialRegression", "SGDRegressor", "ANN", "RandomForest", "SVM", "LGBM", "XGBoost", "KNN"]


models = {name : pickle.load(open(f'{name}.pkl')) for name in model_names}

#Load Evaluation results


results_df = pd.read_csv("model_evalueation_result")


@app.route("/")


def index():
    return render_template("index.html", model_names = model_names)


@app.route("/predict", methods = ["POST"])
def predict():
    model_name = request.form["model"]
    input_data = {
        "Avg. Area Income": float(request.form["Avg. Area Income"]),
        "Avg. Area House Age" : float(request.form["Avg. Area House Age"]),
        "Avg. Area Number of Rooms" : float(request.form["Avg. Area No. of Rooms"])
        
    }