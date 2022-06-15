from unittest import result
import streamlit as st
import json
import kolkatautils
import math
with open("KolkataColumns.json",'r') as f:
     __data_columns = json.load(f)['data_columns']
     __locations1 = __data_columns[3:116]
     __seller1 = __data_columns[116:119]
     __nature1 = __data_columns[119:121]
     __typeofstay1 = __data_columns[121:126]
     __furniture1 = __data_columns[126:129]
def app():
    
        st.title("Metropolitan Rents :-")
        html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Kolkata Accomodation Rent Prediction App </h2>
        </div>
         """
        st.markdown(html_temp,unsafe_allow_html=True)
        seller = st.selectbox('Select Seller Type',(__seller1))
        bedroom = st.text_input("No. Of Bedrooms","Type Here")
        a = st.selectbox('Accomodation Type',(__nature1))
        nature = st.selectbox('Type Of Stay',(__typeofstay1))
        location = st.selectbox('Location',(__locations1))
        area = st.text_input("Area","Type Here")
        furniture = st.selectbox('Furnished Type',(__furniture1))
        bathroom = st.text_input("No. Of Bathrooms","Type Here")
        result = ""
        if st.button("Predict"):
             result = math.ceil(kolkatautils.starting(seller,bedroom,a,nature,location,area,furniture,bathroom))
             st.success('The Rent is %s {}'.format(result)%u'\u20B9')

if __name__ == '__main__':
      app()
