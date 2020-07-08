import numpy as np
import pandas as pd
import pickle

with open("cardekho_random_foreset_regression_model.pkl", 'rb') as f:
	model = pickle.load(f)

def predict(data_array):
	#'Year', 'Present_Price', 'Kms_Driven', 'Owner', 'Fuel_Type_Diesel','Fuel_Type_Petrol', 'Seller_Type_Individual', 'Transmission_Manual'
	return model.predict([data_array])[0]
	 	

