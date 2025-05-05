import streamlit as st

# Heading
st.markdown(f"<span style='color: blue; font-size: 80px; font-weight: bold;'>BMI Calculator</span>", unsafe_allow_html=True)

height = st.slider("Enter your Height (in cm): ", 100, 250, 175)
weight = st.slider("Enter your Weight (in kg): ", 40, 200, 70)

bmi = weight / ((height/100 )** 2)

# st.write(f"Your BMI is {bmi:.2f}")
st.markdown(f"<span style='color: blue; font-size: 20px; font-weight: bold;'>Your BMI is {bmi:.2f}</span>", unsafe_allow_html=True)


st.markdown(f"<span style='color: blue; font-size: 40px; font-weight: bold;'>BMI Categories</span>", unsafe_allow_html=True)
st.write("- Underweight: BMI less than 18.5.")
st.write("- Normal weight: BMI between 18.5 to 24.9.")
st.write("- Overweight: BMI between 25.0 to 29.9.")
st.write("- Obesity: BMI 30 or greater.")