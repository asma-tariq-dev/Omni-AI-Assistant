import streamlit as st

from services.groq_service import ask_groq
from utils.prompts import get_prompt


# Page configuration
st.set_page_config(
    page_title="Omni AI Assistant",
    page_icon="🤖",
    layout="centered"
)


st.title("🤖 Omni AI Assistant")


# Sidebar
st.sidebar.title("Features")

feature = st.sidebar.selectbox(
    "Choose Feature",
    [
        "💬 Text Chat",
        "🎤 Voice Conversation"
    ]
)


# Select AI mode
mode = st.sidebar.selectbox(
    "AI Mode",
    [
        "General Assistant",
        "Coding Assistant",
        "Study Assistant"
    ]
)


# -------------------------------
# Chat History Memory
# -------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -------------------------------
# Text Chat
# -------------------------------

if feature == "💬 Text Chat":

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.write(message["content"])


    # User input
    q = st.chat_input("Ask anything...")


    if q:

        # Store user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": q
            }
        )


        # Display user message
        with st.chat_message("user"):
            st.write(q)


        # Generate AI response
        answer = ask_groq(q, mode)


        # Store AI response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


        # Display AI response
        with st.chat_message("assistant"):
            st.write(answer)



# -------------------------------
# Voice Feature
# -------------------------------

elif feature == "🎤 Voice Conversation":

    st.info("Voice feature code remains here.")
