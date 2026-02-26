import streamlit as st
st.title("Brand new app")
st.header("Esta es mi pagina de presentación")
from PIL import Image
image= Image.open("dim.jpeg")
st.image(image,caption="Deportivo Independiente Medellin")
texto=st.text_input("Ingresa texto","Texto inicial")
st.write("El texto que has escrito es:",texto)
if st.button("Presiona el botón"):
  st.write("Has presionado")

