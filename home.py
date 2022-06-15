import streamlit as st
from PIL import Image
image = Image.open('Property.jpg')
def app():
    st.title('HomePage')
    
    st.image(image)
    
    st.title('Welcome User to Our Rent Prediction System Interface')

    st.write('Select City Name From Navigation Menu To Get Started')