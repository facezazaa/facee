import streamlit as st

st.title("การทดสอบสร้างเว็บด้วยPython")
st.image("data.jpeg")
st.header("การนำเสนอข้อมูลกราฟด้วย Python") 

col1,col2,col3 = st.columns(3)
with col1:
    st.header("Versicolor")
    st.image("https://en.m.wikipedia.org/wiki/File:Symphyotrichum_%C3%97_versicolor.jpg")
with col2:
    st.header("Verginica")
    st.image("https://commons.wikimedia.org/wiki/File:Fire_Pink_Silene_virginica_Flower_2391px.jpg")
with col3:
    st.header("Setosa")
     st.image("https://commons.wikimedia.org/wiki/File:Wild_iris_flower_iris_setosa.jpg")

