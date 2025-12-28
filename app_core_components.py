import streamlit as st
import pandas as pd

st.title("Core Components & Layout")

st.markdown("This is **bold text**, this is *italic text*, and here is a [link](https://streamlit.io).")

# Text input
name = st.text_input("Enter your name:")

# Number input with range
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)

# Checkbox
subscribe = st.checkbox("Subscribe to newsletter")

# Button
if st.button("Submit"):
    st.write(f"Name: {name}, Age: {age}, Subscribe: {subscribe}")

color = st.selectbox("Choose a color:", ["Red", "Green", "Blue"])
st.write(f"You selected: {color}")

# Split the page into two columns
col1, col2 = st.columns(2)

with col1:
    st.write("Column 1: Slider Example")
    slider_value = st.slider("Select a value", 0, 100, 50)
    st.write(f"Slider value: {slider_value}")

with col2:
    st.write("Column 2: Radio Button Example")
    choice = st.radio("Pick one:", ["Option A", "Option B", "Option C"])
    st.write(f"You chose: {choice}")

# Create a sample DataFrame
data = pd.DataFrame({"Fruit": ["Apple", "Banana", "Orange"],"Quantity": [10, 20, 15]})

# Display as a static table
st.table(data)