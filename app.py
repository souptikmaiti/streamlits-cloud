import streamlit as st
import pandas as pd

# Add a title 
st.title("My First Streamlit App")

# Add a header
st.header("This is a header")

# Add a subheader
st.subheader("This is a subheader")

# Add a text
st.text("This is a text")

# Add a markdown
st.markdown("This is a markdown")

# Add a code
st.code("This is a code")

# Add a button
st.button("This is a button")

# Add a text input field
name = st.text_input("Enter your name:")
# Display a dynamic greeting if a name is entered
if name:
    st.write(f"Hello, {name}!")

data = pd.DataFrame(
    {
        "Name": ["John", "Jane", "Bob", "Mary"],
        "Age": [20, 30, 40, 50],
        "Salary": [1000, 2000, 3000, 4000],
    }
)
st.dataframe(data)