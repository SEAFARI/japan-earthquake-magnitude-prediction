import streamlit as st
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd
import pickle

## loading the trained model
model = tf.keras.models.load_model('model.keras')

## load the encoders and scaler
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)
    
with open('ohe.pkl', 'rb') as file:
    ohe = pickle.load(file)
    
## streamlit app
st.title("Japan Earthquake Magnitude Prediction")

## user input
latitude = st.number_input('Latitude')
longitude = st.number_input('longitude')
depth = st.number_input('Depth')
nst = st.number_input('NST')
gap = st.number_input('Gap')
rms = st.number_input('RMS')
depthError = st.number_input('DepthError')
magNst = st.number_input('magNst')
year = st.number_input('Year')
month = st.number_input('Month')
day = st.number_input('Day')
hour = st.number_input('Hour')
minute = st.number_input('Minute')
second = st.number_input('Second')
magType = st.selectbox('magType',['mb', 'mww', 'mwr', 'mwb', 'mwc', 'ms', 'm'])

df = pd.DataFrame({
    'latitude': [latitude],
    'longitude': [longitude],
    'depth': [depth],
    'nst': [nst],
    'gap': [gap],
    'rms':[rms],
    'depthError':[depthError],
    'magNst':[magNst],
    'year':[year],
    'month':[month],
    'day':[day],
    'hour':[hour],
    'minute':[minute],
    'second':[second],
    'magType':[magType]
})


## OHE 
df_ohe = ohe.transform(df[['magType']])
df_ohe = pd.DataFrame(df_ohe, columns=ohe.get_feature_names_out())
df = pd.concat([df,df_ohe],axis=1)

df.drop(columns='magType',inplace=True)



## scaling the data
df = scaler.transform(df)

## Prediction of magnitude
if st.button("Predict"):
    prediction = model.predict(df)
    st.write("The magnitude of the earthquake is: ", prediction[0][0])