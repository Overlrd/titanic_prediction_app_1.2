import streamlit as st
from utils import columns, process
import pandas as pd
import numpy as np
import requests
import json 

st.title('Check if Survive :ship:')

#passengerid =st.text_input('Input Passenger Id', '1234')
passengerclass= st.select_slider('Choose Passenger Class',np.array([1, 2,3]).astype(int) )
#name = st.text_input('Passenger Name', 'John Doe')
gender = st.select_slider('Select Passenger Gender', ['male','female'])
sibsp = st.slider('Passenger Siblings', 0,10)
parch = st.slider('Parents or Childrens', 0,2)
embarked = st.selectbox('Choose Embarkation Point', ['S','C','Q'])
cabin = st.text_input('Enter Cabin', 'CS2')
age = st.selectbox('Passenger Age Group',['Unknown','Child(5-12)', 'Teenager(12-18)',	'Student(18-24)','Young Adult(24-35)', 'Adult(35-60)','Senior(>60)'])

if gender == 'female':
	title = st.selectbox('Choose Passengers Title', ["Miss", "Mrs", "Royal", "Other"])
else:
	title = st.selectbox('Choose Passengers Title', ["Mr", "Master", "Royal", "Other"])

fare = st.selectbox('Fare Amount', [1,2,3,4])



def request_pred(x):
	data_dict = x.to_dict('records')
	data_dic = {}

	for i in data_dict:
		data_dic =  dict(i)
	payload = json.dumps(data_dic ,  indent = 4)
	url = 'https://titanic-prediction-api-0.herokuapp.com/'
	resp = requests.post(url, payload)
	resp = resp.json()
	return resp




def predict():
	row = np.array([ passengerclass,gender,  sibsp , parch ,embarked, cabin, age , title ,fare])
	x = pd.DataFrame([row], columns=columns)

	x = process(x)

	prediction = request_pred(x)
	if prediction['result'] == 1:
		st.success('Passenger  Survived :thumbsup:')	
	elif prediction['result'] == 0:
		st.error('Passenger Did Not Survived :thumbsdown:')
	else:
			st.error('error :thumbsdown:')



st.button('Predict', on_click=predict)

