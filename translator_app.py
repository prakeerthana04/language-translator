import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile

# Mapping of languages to gTTS-supported language codes
gtts_lang_codes = {
    "english": "en",
    "hindi": "hi",
    "malayalam": "ml",
    "tamil": "ta",
    "kannada": "kn",
    "telugu": "te",
    "french": "fr",
    "german": "de",
    "spanish": "es",
    "italian": "it",
    "japanese": "ja",
    "chinese (simplified)": "zh-cn"
    # Add more as needed
}

st.set_page_config(page_title="Universal Translator 🌍", layout="centered")
st.title("🌐 Language Translator with Voice")

text_input = st.text_area("Enter text to translate:", height=100)

lang_list = GoogleTranslator().get_supported_languages()
source_lang = st.selectbox("Source language", lang_list, index=lang_list.index("english"))
target_lang = st.selectbox("Target language", lang_list, index=lang_list.index("malayalam"))

if st.button("Translate"):
    try:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text_input)
        st.success(f"Translation ({target_lang.title()}):")
        st.write(translated)

        # Use language code only if supported in gTTS
        lang_code = gtts_lang_codes.get(target_lang.lower())
        if lang_code:
            tts = gTTS(translated, lang=lang_code)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                tts.save(tmp.name)
                st.audio(tmp.name, format="audio/mp3")
        else:
            st.warning(f"Voice playback not available for '{target_lang.title()}'.")

    except Exception as e:
        st.error(f"Translation failed: {e}")
