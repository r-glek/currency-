import streamlit as st

#Creating widgets for UI
st.title("Currency Converter")
st.text_input("Enter Amount:")
st.radio("Select Currency:", ["GDP to USD", "USD to GDP","GDP to JPY","JPY to GDP"])

col1, col2 = st.columns([2, 1])

with col1:
    st.text("Converted Amount: ")
    with col2:
        st.text("900")