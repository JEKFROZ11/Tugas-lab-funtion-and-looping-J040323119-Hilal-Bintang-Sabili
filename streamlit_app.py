# streamlit_calculator.py

import streamlit as st
from math_operations import *

st.title("Simple Calculator")

x = st.number_input("Enter the first number:")
y = st.number_input("Enter the second number:")

operation = st.selectbox("Select an operation",
                         ("Add", "Subtract", "Multiply", "Divide"))

result = None

if st.button("Calculate"):
    if operation == "Add":
        result = add(x, y)
    elif operation == "Subtract":
        result = subtract(x, y)
    elif operation == "Multiply":
        result = multiply(x, y)
    elif operation == "Divide":
        try:
            result = divide(x, y)
        except ZeroDivisionError:
            st.error("Division by zero is not allowed.")

if result is not None:
    st.success(f"Result: {result}")
