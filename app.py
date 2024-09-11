import streamlit as st # type: ignore
from googletrans import Translator, LANGUAGES # type: ignore

# Initialize translator
translator = Translator()

# Custom CSS for animated background, central alignment, and more styling
st.markdown("""
    <style>
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(45deg, #84fab0, #8fd3f4, #9fb8ad, #1fc8db);
        background-size: 400% 400%;
        animation: gradientBG 20s ease infinite;
        color: #ffffff;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        padding: 0;
    }

    .main-container {
        text-align: center;
        max-width: 600px;
        margin: 0 auto;
    }

    .header {
        color: #f8f9fa;
        font-family: 'Arial Black', sans-serif;
        font-size: 40px;
        letter-spacing: 2px;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px #000000;
    }

    .subheader {
        color: #e0e0e0;
        font-family: 'Verdana', sans-serif;
        font-size: 20px;
        margin-bottom: 25px;
        text-shadow: 1px 1px 3px #000000;
    }

    .footer {
        text-align: center;
        margin-top: 50px;
        color: #f1f1f1;
        font-size: 14px;
    }

    .input-box, .button {
        margin-bottom: 15px;
        width: 100%;
    }

    .result-box {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        color: #000;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease-in-out;
    }

    .result-box:hover {
        transform: scale(1.05);
    }

    .button {
        background-color: #007bff;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 18px;
        cursor: pointer;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s ease;
    }

    .button:hover {
        background-color: #0056b3;
    }

    </style>
    """, unsafe_allow_html=True)

# Main container for centering the content
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Application Title
st.markdown('<h1 class="header">🌍 Language Translator</h1>', unsafe_allow_html=True)
#st.markdown('<h3 class="subheader">Translate words or sentences easily into multiple languages</h3>', unsafe_allow_html=True)

# User input for word/sentence
word = st.text_input("Enter a word or sentence to translate:", key="input", help="Type the text you want to translate here.")
search = st.text_input("Search for a language:", key="search", help="Type the language you want to translate to.")

# Filter the languages based on the search term
language_options = [language for language in LANGUAGES.values() if search.lower() in language.lower()]

if not language_options:
    st.write("No languages match your search.")
else:
    # Selectbox to choose the target language
    target_language = st.selectbox("Select the target language:", language_options, key="select_language")

# Translate button and display results
if word:
    # Detect the input language
    detected_language = translator.detect(word).lang
    detected_language_name = LANGUAGES[detected_language].capitalize()

    st.markdown(f"Detected Language: {detected_language_name}")

    # Add a button to trigger the translation
    if st.button("Translate", key='translate_button'):
        # Get the code of the selected language
        target_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]
        translated = translator.translate(word, dest=target_language_code)

        # Display detected language and translated text
        st.markdown(f'<div class="result-box">Input Language: {detected_language_name}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-box">Translated Text in {target_language}: {translated.text}</div>', unsafe_allow_html=True)

# Close the main container
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Developed with ❤️ using Googletrans & Streamlit</div>', unsafe_allow_html=True)
