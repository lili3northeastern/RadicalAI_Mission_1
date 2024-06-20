import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

st.title("Gemini Explorer")

# Collect user's name
user_name = st.text_input("Please enter your name:", placeholder="Type your name here...")

# Initialize chat history if not already
if "messages" not in st.session_state:
    st.session_state.messages = []

# Only set initial messages if user name is inputted and it's a new session
if user_name and "initialized" not in st.session_state:
    welcome_message = f"Welcome to Gemini Explorer, {user_name}! How can I assist you with your flight information today?"
    initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive."

    # Append messages only once
    if not st.session_state.messages:
        st.session_state.messages.append({"role": "model", "content": welcome_message})
        st.session_state.messages.append({"role": "model", "content": initial_prompt})

    # Display messages
    for message in st.session_state.messages:
        with st.container():
            st.markdown(message["content"])
    
    # Mark the session as initialized
    st.session_state.initialized = True

# Optional: Clear button to reset session (for testing and demo purposes)
if st.button('Clear Session'):
    st.session_state.clear()

# Handling user queries
query = st.text_input("Ask me anything:")
if query:
    # Simulate response (replace with actual function call if available)
    response = f"Here is a response to your query, {user_name}."
    with st.container():
        st.markdown(f"You asked: {query}")
        st.markdown(f"ReX responds: {response}")
