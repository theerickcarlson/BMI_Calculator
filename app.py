import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

# Title
st.title("⚖️ BMI Calculator")

# Description
st.markdown("""
This app calculates your **Body Mass Index (BMI)**  
Enter your **weight (kg)** and **height (meters)** below.
""")

# Input Fields
weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height (meters):", min_value=0.0, format="%.2f")

# Button
if st.button("Calculate BMI"):

    if height > 0:
        bmi = weight / (height * height)

        st.success(f"Your BMI is: **{bmi:.2f}**")

        # BMI Categories
        if bmi < 18.5:
            st.info("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("Category: Overweight")
        else:
            st.error("Category: Obese")

    else:
        st.error("Please enter a valid height.")
