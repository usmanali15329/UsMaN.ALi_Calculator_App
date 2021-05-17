import streamlit as st
import math
st.title("Lahore Garrison University")

#a = 5

#Addition application
#st.info("Please enter the number between 0 and 9")
a = st.number_input("Please enter the number between 0 and 9")
b = st.number_input("Please enter another number between 0 and 9")
c = a + b
st.title("Addtion")
st.text("The result after addition is")
st.write(c)



st.title("Subtraction")

#Subtraction application
#st.info("Please enter the number between 0 and 9")
d = a - b

st.text("The result after Subtraction is")
st.write(d)



st.title("Multiplication")

#Multiplication application
#st.info("Please enter the number between 0 and 9")
d = a * b


st.text("The result after Multiplication is")
st.write(d)





st.title("Division")

#Division application
#st.info("Please enter the number between 0 and 9")
d = a / b


st.text("The result after Division is")
st.write(d)


st.title("Modulus")

#Modulus application
#st.info("Please enter the number between 0 and 9")
d = a % b


st.text("The result after Division is")
st.write(d)


st.title("Exponension")

#Division application
#st.info("Please enter the number between 0 and 9")
d = a ** b


st.text("The result of exponention is is")
st.write(d)



st.title("Factorial")

#Division application
#st.info("Please enter the number between 0 and 9")
x = st.number_input("Please enter any number")


st.text("The result of Factorial is")
st.write(math.factorial(x))

