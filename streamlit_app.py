import streamlit as st
import requests

st.title("Buscador de Datos Deportivos")

league = st.text_input("Liga (ej: premier-league)")
season = st.text_input("Temporada (ej: 2024)")

if st.button("Buscar datos"):
    if league and season:
        url = f"https://www.scorebat.com/video-api/v3/feed/?league={league}&season={season}"
        
        try:
            data = requests.get(url).json()
            st.json(data)
        except Exception as e:
            st.error("Error al obtener datos.")
            st.write(e)
    else:
        st.warning("Completa todos los campos.")
