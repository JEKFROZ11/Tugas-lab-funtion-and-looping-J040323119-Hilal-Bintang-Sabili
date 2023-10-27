# streamlit_calculator.py

import streamlit as st


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y


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
