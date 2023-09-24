import streamlit as st
import random
import time

st.title("Inversiones Pro")
st.sidebar.markdown("### Inversiones Pro")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages2 = []

# Display chat messages from history on app rerun for the second session
for message in st.session_state.messages2:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# Accept user input for the second session
if prompt2 := st.chat_input("What is up for Session 2?"):
    # Add user message to chat history for the second session
    st.session_state.messages2.append({"role": "user", "content": prompt2})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt2)


    # Display assistant response in chat message container for the second session
    with st.chat_message("assistant"):
        """
            Procesar prompt antes de la respuesta
        """
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = "Assistant response for Session 2."  # Customize as needed
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history for the second session
    st.session_state.messages2.append({"role": "assistant", "content": full_response})