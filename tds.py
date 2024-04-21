import streamlit as st

def maximum(a, b, c): 
 
    if (a >= b) and (a >= c): 
        largest = a 
 
    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c 
         
    return largest 
 
 
a = int(input("First number"))
b = int(input("Second number"))
c = int(input("Third number"))
print(maximum(a, b, c)) 
