# codsoft_task1_streamlit_calc.py

import streamlit as st

# 🎯 Page settings
st.set_page_config(page_title="CodSoft Calculator", page_icon="🧮")

st.title("🧮 CodSoft Task 1 - Streamlit Calculator")
st.markdown("A simple calculator built with **Python + Streamlit** by [Pragadeesh](https://pragadeeshfolio.netlify.app) 💡")

# 📥 Inputs
num1 = st.text_input("Enter First Number")
num2 = st.text_input("Enter Second Number")
operation = st.radio("Choose Operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# 🚀 Button to calculate
if st.button("Calculate"):
    try:
        a = float(num1)
        b = float(num2)

        if operation == "Addition":
            result = a + b
        elif operation == "Subtraction":
            result = a - b
        elif operation == "Multiplication":
            result = a * b
        elif operation == "Division":
            if b == 0:
                st.error("❌ Cannot divide by zero.")
                result = None
            else:
                result = a / b
        else:
            st.warning("❌ Invalid operation.")
            result = None

        if result is not None:
            st.success(f"✅ Result of {operation} = {result}")

    except ValueError:
        st.error("❌ Please enter valid numbers.")

