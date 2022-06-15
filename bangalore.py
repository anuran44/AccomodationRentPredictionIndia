from unittest import result
import streamlit as st
import json
import bangaloreutils
import math
with open("BangaloreColumns.json",'r') as f:
     __data_columns = json.load(f)['data_columns']
     __locations1 = __data_columns[3:254]
     __seller1 = __data_columns[254:257]
     __nature1 = __data_columns[257:259]
     __typeofstay1 = __data_columns[259:265]
     __furniture1 = __data_columns[265:268]
def app():
    
        st.title("Metropolitan Rents :-")
        html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Bangalore Accomodation Rent Prediction App </h2>
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
             result = math.ceil(bangaloreutils.starting(seller,bedroom,a,nature,location,area,furniture,bathroom))
             st.success('The Rent is %s {}'.format(result)%u'\u20B9')

if __name__ == '__main__':
      app()
