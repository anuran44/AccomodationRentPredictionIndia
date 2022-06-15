from multiplepage import MultiApp
import streamlit as st
import hyderabad
import kolkata
import mumbai
import bangalore
import ahmedabad
import pune
import delhi
import chennai
import home

app = MultiApp()
app.add_app("Home",home.app)
app.add_app("Mumbai",mumbai.app)
app.add_app("Kolkata",kolkata.app)
app.add_app("Bangalore",bangalore.app)
app.add_app("Ahmedabad",ahmedabad.app)
app.add_app("Pune",pune.app)
app.add_app("Delhi",delhi.app)
app.add_app("Chennai",chennai.app)
app.add_app("Hyderabad",hyderabad.app)

app.run()