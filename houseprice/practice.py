import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, SGDRegressor, HuberRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsRegressor
import lightgbm as lgb
import xgboost as xgb
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle 
import os

path = os.path.join(os.getcwd(), "houseprice")
data = pd.read_csv(r"C:\Users\vineet\Desktop\house_price_project\USA_Housing.csv")

#Preprocessing

X = data.drop(["Price", "Address"], axis = 1)
y = data["Price"]


#Split data

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size= 0.2, random_state= 0)


#Define models

models = {
    "LinearRegression" : LinearRegression(),
    "RobustRegression" : HuberRegressor(),
    "RidgeRegression" : Ridge(),
    "LassoRegression" : Lasso(),
    "ElasticNet" : ElasticNet(),
    "PolynomialRegression" : Pipeline([
        ("poly", PolynomialFeatures(degree = 2)),
        ("linear", LinearRegression())
    ]),
    "SGDRegressor" : SGDRegressor(),
    "ANN" : MLPRegressor(),
    "RandomForest" : RandomForestRegressor(),
    "SVM" : SVR(),
    "LGBM" : lgb.LGBMRegressor(),
    "XGBoost" : xgb.XGBRegressor(),
    "KNN" : KNeighborsRegressor()
    }

results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    results.append({
     "Model" : name,
     "MAE" : mae,
     "MSE" : mse,
     "R2" : r2   
    })
    
    
    
    file_path = os.path.join(path, f"{name}.pkl")
    with open(file_path, "wb") as f:  # Writing in binary mode
        pickle.dump(model, f)


results_df = pd.DataFrame(results)
results_df.to_csv(r"C:\Users\vineet\Desktop\TimeSeries\houseprice\model_evaluation_results.csv", index = False)


print("Models trained and saved to pickle file. Evalutation results stored in model_evaluation_results.csv")