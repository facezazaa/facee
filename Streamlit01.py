import streamlit as st

st.title("การทดสอบสร้างเว็บด้วยPython")
st.image("data.jpeg")
st.header("การนำเสนอข้อมูลกราฟด้วย Python") 

col1,col2,col3 = st.columns(3)
with col1:
    st.header("Versicolor")
    st.image("./image/color.jpg")
with col2:
    st.header("Verginica")
    st.image("./image/ver.jpg")
with col3:
    st.header("Setosa")
     st.image("./image/set.jpg")

