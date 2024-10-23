import streamlit as st
import joblib

model = joblib.load("regression.joblib")

size = st.number_input("Taille de la maison (m²)", min_value=0)
nb_rooms = st.number_input("Nombre de chambres", min_value=0)
garden = st.radio("La maison a-t-elle un jardin?", [0, 1], format_func=lambda x: "Oui" if x == 1 else "Non")

input_data = [[size, nb_rooms, garden]]

if st.button("Faire une prédiction"):
    prediction = model.predict(input_data)
    
    st.write(f"Le prix estimé de la maison est : {prediction[0]:.2f} €")