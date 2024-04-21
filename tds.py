import streamlit as st

title = st.title('Maximum of 3 numbers:')

number1 = st.number_input('Input 1st Number:') 
number2 = st.number_input('Input 2nd Number:') 
number3 = st.number_input('Input 3rd Number:')

st.write(max([number1,number2,number3]))
