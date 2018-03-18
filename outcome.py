import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
pd.options.mode.chained_assignment = None
import json
from sklearn.externals import joblib
import statsmodels.formula.api as smf
import sklearn.metrics as sm
from math import ceil
from sklearn import linear_model 



def predict_outcome():
			'''
	This function is basically used to identify and predict
	whether or not a person might go into depression again.
	It analyses it by looking at the age, gender,
	time in depression before coming to meet doctor and also
	the time for which the person stays in evaluation or the time
	before which the person goes into depression again

	Everything here is in Integers or Float64.
			'''
	data_input = pd.read_csv("depression.csv")		#Reading the csv file using pandas
	data = data_input[['Time','Age','Gender','AcuteT']]	#The machine learning model will take the following as the inputs to predict
	

	expected_output = data_input[['Outcome']]		#The output that is expected is here
	input_train, input_test, expected_op_train, expected_op_test = train_test_split(data, expected_output, test_size=0.29, random_state = 10000)	#Dividing the avaiable dataset to train & test

	rf = RandomForestClassifier(n_estimators = 100)		#The ML Algorithm that we're using
	rf.fit(input_train, expected_op_train)			#Getting the best fit for the curve by using the fit function

	accuracy = rf.score(input_test, expected_op_test)


	joblib.dump(rf, "models/Outcome_Model", compress = 9)
	rf = joblib.load("models/Outcome_Model")		#Stores the machine learning model by the name "Outcome_Model"

	time = 32.6 
	age = 48
	gender = 2
	acutet = 284
	outcome = rf.predict([[time,age,gender,acutet]])
	#print(outcome, accuracy*100)
	return outcome



def predict_treatment():
			'''
	This function is basically used to identify and predict
	what kind of treatment is to be given to a patient.
	It analyses it by looking at the age, gender, recurrence outcome,
	time in depression before coming to meet doctor and also
	the time for which the person stays in evaluation or the time
	before which the person goes into depression again

	Everything here is in Integers or Float64.
			'''

	data_input = pd.read_csv("depression.csv")		#Reading the csv file using pandas
	data_input['Treat'].replace('Lithium', 3, inplace = True)
	data_input['Treat'].replace('Imipramine', 2, inplace = True)
	data_input['Treat'].replace('Placebo', 1, inplace = True)
	data_input['Outcome'] = np.where(data_input['Outcome'] == 'Recurrence', 1, 0)	#This is just to clean the data to convert the words into numbers for the ML Algo

	data = data_input[['Outcome','Time','AcuteT','Age','Gender']]
	expected_output = data_input[['Treat']]

	lm = linear_model.LinearRegression()		#Calling the regression algorithm and creating object
	model = lm.fit( data , expected_output)		#Getting the best fit for the curve by using the fit function

	predictions = lm.predict(data[['Outcome','Time','AcuteT','Age','Gender']])

	'''time = 32.6 
	age = 48
	gender = 2
	acutet = 284
	outcome = predict_outcome()'''
	treat = ceil(lm.predict([[1, 32.6, 284, 48, 2]]))	#Taking ceil because the regression algorithm here predicts low values and the ceil function makes predictions more accurate
	
	#print("MSE:", sm.mean_squared_error(predictions, data_input['Treat'].values))	#Calculates how good the fit is. Finds the error between the predicted values and actual ones.
	joblib.dump(model, "models/Treatment_Model", compress = 9)	#Stores the machine learning model by the name "Treatment_Model"
	
	#print(treat)
