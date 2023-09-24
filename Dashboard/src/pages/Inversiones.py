import streamlit as st
from services.educationModel import educationModel
from services.financeEduModel import financeEduModel
st.title("Inversiones")
st.sidebar.markdown("### Inversiones")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages1 = []

# Display chat messages from history on app rerun
for message in st.session_state.messages1:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Keywords to trigger the education model
education_keywords = {
    "Que es": True, "acciones": True, "invertir": True,
    "explicame": True, "explicar": True, "explica": True,
    "dime": True, "como": True, "ahorrar": True,
    "ahorro": True, "inversion": True, "inversiones": True,
    "stocks": True, "finanzas": True,
    "financiero": True, "sistema financiero": True, "retiro": True,
    "fondo de retiro": True, "banorte": True, "dinero": True,
    "crédito": True, "préstamo": True, "intereses": True,
    "diversificación": True, "planificación financiera": True, "presupuesto": True,
    "impuestos": True, "inflación": True, "dividendos": True, 
    "acciones preferentes": True, "portafolio de inversión": True,
    "rentabilidad": True, "análisis financiero": True, "estrategia de inversión": True,
    "saber": True, "conocer": True, "aprender": True,
    "entender": True, "comprender": True
}
# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages1.append({"role": "user", "content": prompt})

    response=""
    #Procesar modelo dependiendo del prompt antes de la respuesta
    # Verifica si alguna de las palabras clave está presente en el prompt
    if any(keyword in prompt for keyword in education_keywords):
        response = financeEduModel(prompt)
    else:
        response = f"Echo: {prompt}"
        
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages1.append({"role": "assistant", "content": response})