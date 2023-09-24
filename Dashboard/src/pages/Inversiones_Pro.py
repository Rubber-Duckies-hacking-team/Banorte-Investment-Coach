import streamlit as st
from services.GettingBestChoices import GettingRiskyChoices, GettingNeutralChoices,GettingPopularChoices
from services.modelCharts import main

import re
st.title("Inversiones Pro")
st.sidebar.markdown("### Inversiones Pro")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    if re.search(r'\briesgo\b', prompt):
        response = GettingRiskyChoices()
    elif re.search(r'\bsegura\b', prompt):
        response = GettingNeutralChoices()
    elif re.search(r'\bpopular\b', prompt):
        response = GettingPopularChoices()
    elif re.search(r'\bempresa\b', prompt):
        response = "Estamos procesando tu solicitud, por favor espera un momento..."
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        empresa = re.search(r'\bempresa\b\s*(\w+)', prompt).group(1)
        try:
            response = main(empresa,st.session_state.messages)
        except:
            response= """Una disculpa, no tengo información sobre esa empresa para analizar y hacer una prediccion correcta"""
    else:
        response = """¡Hola! Parece que has planteado una pregunta interesante. Lamentablemente, mi conocimiento actual se limita a ciertos temas y no tengo información específica sobre ese tema en particular.
                        Sin embargo, estaré encantado de ayudarte con cualquier otra consulta que tengas o proporcionarte información sobre inversiones. ¿En qué más puedo asistirte hoy?"""

    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

