import streamlit as st
import spacy_streamlit
from PIL import Image
import os
import spacy  # Import the spacy library

# Download the model if not already present
import spacy.cli
spacy.cli.download("en_core_web_sm", "-d", "--user")

@st.cache_data
def load_image(img):
    im = Image.open(img)
    return im

# Layout Templates
title_temp ="""
    <div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
    <h4 style="color:white;text-align:center;">SpaCy Streamlit</h1>
    </div>
    """

def main():
    st.title("SpaCy Streamlit  APP")
    # st.markdown(title_temp,unsafe_allow_html=True)
    our_image = Image.open(os.path.join('SpaCy_logo.svg.png'))
    st.image(our_image)

    menu = ['Home','NER']
    choice = st.sidebar.selectbox('Menu', menu)

    # Load the SpaCy model using the full name
    nlp = spacy.load("en_core_web_sm")

    if choice == 'Home':
        st.subheader('Home')
        raw_docx = st.text_area('Your Docs','Enter Text')
        docx = nlp(raw_docx)
        if st.button("Tokenize"):
            spacy_streamlit.visualize_tokens(docx, attrs=["text", "pos_", "dep_", "ent_type_"])

    elif choice == 'NER':
        st.subheader('Named Entity Recognizer')
        raw_docx = st.text_area('Your Text','Enter Text')
        docx = nlp(raw_docx)
        spacy_streamlit.visualize_ner(docx, labels=nlp.get_pipe("ner").labels)

if __name__ == '__main__':
    main()

