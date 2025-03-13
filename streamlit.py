# Import libraries
import streamlit as st
import pandas as pd
from databaseinput import insertdata


# head of the website
st.title('Python mysql sample project')
st.write('This is a python streamlit and mysql project. This project is supposed to accept input with streamlit and store the input in the mysql database. The project is just a sample project and nothing serious.')

# set input questions
with st.form('form input'):
    firstname = st.text_input('First Name', placeholder='your name goes here...')
    middlename = st.text_input('Middle Name', placeholder='your name goes here...')
    lastname = st.text_input('Last Name', placeholder='your name goes here...')
    age = st.slider('Age', min_value=18, max_value=70)
    country = st.selectbox('Country', ['Nigeria', 'India','Korea', 'Ghana', 'France', 'Ireland'])
    phone = st.text_input('Phone number', max_chars=11)
    if len(phone) < 11:
        st.error('phone number not correct')
    
    dob = st.date_input('Date of birth')# needs correction
    course = st.text_input('Course')
    life = st.text_area('what do you think about life?')
    submit = st.form_submit_button('Submit now')
    
    
    #form submit
    if submit: 
        insertdata(first_name =firstname, middle_name =middlename, last_name =lastname, age = age, country = country, phone = phone, about_life =life, Date_of_birth = dob, course = course)
        st.success('Thank youuuu')
        st.balloons()
    else:
        st.warning('fill the above fields')
        
# input values dataframe
st.write('This is the information you submitted above')         
table = pd.DataFrame({
    'first name': [firstname],
    'middle name': [middlename],
    'last name': [lastname],
    'age': [age],
    'country': [country],
    'phone': [phone],
    'about life': [life],
    'Date of birth': [dob],
    'course': [course]})

# show dataframe
st.write(table.transpose())
   