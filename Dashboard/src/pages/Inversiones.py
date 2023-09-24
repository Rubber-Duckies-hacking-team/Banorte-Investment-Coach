import streamlit as st
from services.educationModel import educationModel
from services.financeEduModel import financeEduModel
from services.InvestmentFunds import get_fondo
import re

st.title("Inversiones")
st.sidebar.markdown("### Inversiones")
# Initialize chat history
if "messages1" not in st.session_state:
    st.session_state.messages1 = []

# Display chat messages from history on app rerun
for message in st.session_state.messages1:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# Regular expression to trigger the get_fondo() function
fondo_regex = r"\b(recomienda|recomiendame|in:)\b"
response = ""

money, time=0,0
# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages1.append({"role": "user", "content": prompt})

    # Check if the prompt matches the regular expression
    # if "in:" in prompt:
    #     col1, col2 = st.columns(2)
    #     if "visibility" not in st.session_state:
    #         st.session_state.visibility = "visible"
        
    #     # Set the disabled attribute based on visibility
    #     disabled = not (st.session_state.visibility == "visible")
        
    #     with col1:
    #         money = st.text_input(
    #             "Ingresa la cantidad de inversion deseas hacer",
    #             label_visibility=st.session_state.visibility,
    #             disabled=disabled
    #         )

    #     with col2:
    #         time = st.text_input(
    #             "Ingresa el plazo en el que deseas hacer la inversion",
    #             label_visibility=st.session_state.visibility,
    #             disabled=disabled
    #         )

    #     if st.button("Calcular"):
    #         try:
    #             _money = float(money)
    #             _time = float(time)
    #             response = get_fondo(_money, _time)
    #         except ValueError:
    #             st.error("Por favor, ingresa valores válidos para la cantidad y el plazo.")

    # Check if any of the education keywords are present in the prompt

    try:
        response = educationModel(prompt)
    except:
        response= "Una disculpa, hubo un error al procesar tu solicitud. Intenta de nuevo"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages1.append({"role": "assistant", "content": response})

    # Procesar modelo dependiendo del prompt antes de la respuesta
    # Verifica si alguna de las palabras clave está presente en el prompt
