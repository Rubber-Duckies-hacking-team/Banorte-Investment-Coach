import streamlit as st
from services.educationModel import educationModel
from services.financeEduModel import financeEduModel
from services.InvestmentFunds import get_fondo
import re

st.title("Inversiones")
st.sidebar.markdown("### Inversiones")
st.sidebar.markdown(
    """
    <img src="https://play-lh.googleusercontent.com/jFyE2IbJDS3tqTeuOoew-IfI84Uh1ZcXSr_sg0bIYuv_wkSjpFjpX70C8yezYwk3Tq4=w480-h960" style="width:60px;"/>
    """,
    unsafe_allow_html=True,
)
st.sidebar.markdown("### Inversiones")
st.sidebar.markdown("- En este chat nuestro coach de inversiones te ayudará a resolver tus dudas sobre educación financiera. Escribe **\"ed:\"** y después tu pregunta para que nuestro coach te responda sobre educación financiera.")
st.sidebar.markdown("Ejemplos:")
st.sidebar.markdown("""> ed: ¿Qué es una acción?
                    \n> ed: ¿Cómo puedo invertir mi dinero?""")
st.sidebar.markdown("- También puedes recibir recomendaciones sobre inversiones. Solo escribe **\"recomienda\"** y nosotros te vamos a orientar sobre las mejores opciones para ti.")
# Initialize chat history
if "messages1" not in st.session_state:
    st.session_state.messages1 = []

# Display chat messages from history on app rerun
for message in st.session_state.messages1:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Keywords to trigger the education model
education_keywords = {
    "Que es": True,
    "acciones": True,
    "invertir": True,
    "explicame": True,
    "explicar": True,
    "explica": True,
    "dime": True,
    "como": True,
    "ahorrar": True,
    "ahorro": True,
    "inversion": True,
    "inversiones": True,
    "stocks": True,
    "finanzas": True,
    "financiero": True,
    "sistema financiero": True,
    "retiro": True,
    "fondo de retiro": True,
    "banorte": True,
    "dinero": True,
    "crédito": True,
    "préstamo": True,
    "intereses": True,
    "diversificación": True,
    "planificación financiera": True,
    "presupuesto": True,
    "impuestos": True,
    "inflación": True,
    "dividendos": True,
    "acciones preferentes": True,
    "portafolio de inversión": True,
    "rentabilidad": True,
    "análisis financiero": True,
    "estrategia de inversión": True,
    "saber": True,
    "conocer": True,
    "aprender": True,
    "entender": True,
    "comprender": True,
}

# Regular expression to trigger the get_fondo() function
fondo_regex = r"\b(recomienda|recomiendame)\b"
response = ""

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages1.append({"role": "user", "content": prompt})

    # Check if the prompt matches the regular expression
    if re.search(fondo_regex, prompt, re.IGNORECASE):
        dinero = st.text_input('Ingresa el monto:', type='default')
        
        tiempo = st.text_input('Ingresa el tiempo:', type='default')
        
        if dinero and tiempo:
            response = get_fondo(int(dinero),int(tiempo))
        else:
            response = "Por favor ingresa un monto y un tiempo para poder recomendarte un fondo de inversión"
        
    # Check if any of the education keywords are present in the prompt
    elif any(keyword in prompt for keyword in education_keywords):
        response = financeEduModel(prompt)
    else:
        response = f"Echo: {prompt}"

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages1.append({"role": "assistant", "content": response})

    # Procesar modelo dependiendo del prompt antes de la respuesta
    # Verifica si alguna de las palabras clave está presente en el prompt
