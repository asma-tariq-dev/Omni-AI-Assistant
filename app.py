import streamlit as st
from audio_recorder_streamlit import audio_recorder
from services.groq_service import ask_groq
from services.image_service import generate_image
from services.voice_service import speech_to_text, text_to_speech

st.set_page_config(page_title="Omni AI Assistant", page_icon="🤖")
st.title("🤖 Omni AI Assistant")

mode = st.sidebar.selectbox("Assistant Mode", ["General Assistant", "Coding Expert"])
feature = st.sidebar.radio("Feature", ["💬 Text Chat", "🎤 Voice Conversation", "🖼️ Image Generator"])

if feature == "💬 Text Chat":
    q = st.chat_input("Ask anything...")
    if q:
        st.write("🤖 AI:", ask_groq(q, mode))

elif feature == "🎤 Voice Conversation":
    audio = audio_recorder(text="Click and speak")
    if audio:
        with open("input.wav", "wb") as f:
            f.write(audio)
        q = speech_to_text("input.wav")
        st.write("👤 You:", q)
        ans = ask_groq(q, mode)
        st.write("🤖 AI:", ans)
        st.audio(text_to_speech(ans))

else:
    prompt = st.text_input("Enter image prompt")
    if st.button("Generate"):
        st.image(generate_image(prompt))
