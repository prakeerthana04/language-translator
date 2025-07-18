import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile

st.set_page_config(page_title="Universal Translator 🌍", layout="centered")
st.title("🌐 Language Translator with Voice")

text_input = st.text_area("Enter text to translate:", height=100)

# ✅ Corrected line to avoid TypeError
lang_list = GoogleTranslator().get_supported_languages()

source_lang = st.selectbox("Source language", lang_list, index=lang_list.index("english"))
target_lang = st.selectbox("Target language", lang_list, index=lang_list.index("hindi"))

if st.button("Translate"):
    try:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text_input)
        st.success(f"Translation ({target_lang.title()}):")
        st.write(translated)

        # ✅ Get language code for gTTS
        tts = gTTS(translated, lang=GoogleTranslator().get_language_code(target_lang))

        # ✅ Play audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tts.save(tmp.name)
            st.audio(tmp.name, format="audio/mp3")

    except Exception as e:
        st.error(f"Translation failed: {e}")
