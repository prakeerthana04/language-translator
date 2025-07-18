import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os
import time

# Initialize translator
translator = Translator()

# Map language codes to names
language_dict = {v.capitalize(): k for k, v in LANGUAGES.items()}
language_names = list(language_dict.keys())

# App UI setup
st.set_page_config(page_title="Language Translator", layout="wide")
st.markdown("<h1 style='text-align: center; color: #FEC260;'>🌐 Language Translator</h1>", unsafe_allow_html=True)

# Language selection
col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("From Language", language_names, index=language_names.index("English"))
with col2:
    dest_lang = st.selectbox("To Language", language_names, index=language_names.index("Spanish"))

# Input text area
input_text = st.text_area("Enter Text", height=200)

# Translate text
if st.button("Translate ➡"):
    if input_text.strip():
        try:
            translated = translator.translate(input_text, src=language_dict[src_lang], dest=language_dict[dest_lang])
            st.text_area("Translated Text", value=translated.text, height=200, key="output")
        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter some text to translate.")

# Text-to-speech
def speak_text(text, lang_code):
    try:
        tts = gTTS(text=text, lang=lang_code)
        filename = "temp_audio.mp3"
        tts.save(filename)
        st.audio(filename, format="audio/mp3")
        time.sleep(2)
        os.remove(filename)
    except Exception as e:
        st.error(f"Audio error: {e}")

# Pronounce Buttons
col3, col4 = st.columns(2)
with col3:
    if st.button("🔊 Pronounce Original"):
        speak_text(input_text, language_dict[src_lang])

with col4:
    if st.button("🔊 Pronounce Translated"):
        if "output" in st.session_state:
            speak_text(st.session_state.output, language_dict[dest_lang])

