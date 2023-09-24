import streamlit as st
from services.educationModel import educationModel
from services.financeEduModel import financeEduModel
st.title("Inversiones")
st.sidebar.markdown("### Inversiones")
# Initialize chat history
if "messages1" not in st.session_state:
    st.session_state.messages1 = []

# Display chat messages from history on app rerun
for message in st.session_state.messages1:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages1.append({"role": "user", "content": prompt})

    response=""
    #Procesar modelo dependiendo del prompt antes de la respuesta
    # Verifica si alguna de las palabras clave está presente en el prompt
    if "ed:" in prompt:
        response = financeEduModel(prompt)
    else:
        response = """¡Hola! Parece que has planteado una pregunta interesante. Lamentablemente, mi conocimiento actual se limita a ciertos temas y no tengo información específica sobre ese tema en particular.
                        Sin embargo, estaré encantado de ayudarte con cualquier otra consulta que tengas o proporcionarte información sobre educación financiera y inversiones con Banorte. ¿En qué más puedo asistirte hoy?"""

        
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages1.append({"role": "assistant", "content": response})