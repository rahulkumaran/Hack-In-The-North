import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
pd.options.mode.chained_assignment = None
import seaborn as sns
from sklearn.externals import joblib

def predict_outcome():
	data_input = pd.read_csv("depression.csv")		#Reading the csv file using pandas
	data = data_input[['Time','Age','Gender','AcuteT']]	#The machine learning model will take the following as the inputs to predict
	data_input['Outcome'] = np.where(data_input['Outcome'] == 'Recurrence', 1, 0)	#This is just to clean the data to convert the words into numbers for the ML Algo

	expected_output = data_input[['Outcome']]		#The output that is expected is here
	input_train, input_test, expected_op_train, expected_op_test = train_test_split(data, expected_output, test_size=0.29, random_state = 10000)	#Dividing the avaiable dataset to train & test

	rf = RandomForestClassifier(n_estimators = 100)		#The ML Algorithm that we're using
	rf.fit(input_train, expected_op_train)			#Getting the best fit for the curve by using the fit function

	accuracy = rf.score(input_test, expected_op_test)
	print("accuracy is {}%".format(accuracy*100))

	joblib.dump(rf, "models/Outcome_Model", compress = 9)		#Stores the machine learning model by the name "Outcome_Model"
