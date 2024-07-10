# NLP_app_with_Spacy_Streamlit
This Streamlit application, named "SpaCy Streamlit Application," coordinates the 'en_core_web_sm' model from SpaCy for normal language handling undertakings inside an easy to use interface. After sending off, it presents a title flag styled with a foundation tone ('#464e5f') and shows the SpaCy logo picture ('SpaCy_logo.svg.png').

Clients explore through the application utilizing a sidebar menu offering two fundamental segments: 'Home' and 'NER' (Named Substance Recognizer). In the 'Home' segment, clients input text into a text region marked 'Your Docs' and the SpaCy model tokenizes this contribution after tapping the "Tokenize" button. The tokenization results are then imagined utilizing 'spacy_streamlit', featuring text, grammatical form labels, reliance relations, and substance types.

In the 'NER' segment, marked 'Named Substance Recognizer', clients input text into another text region marked 'Your Text' for named element acknowledgment. The application processes the information utilizing SpaCy's 'ner' pipeline and imagines perceived named elements, including their sorts.

The application proficiently oversees execution by storing picture information ('load_image' capability) and possibly handled text information ('@st.cache_data'). It guarantees a consistent client experience by downloading the SpaCy model ('en_core_web_sm') while possibly not currently introduced.

In general, "SpaCy Streamlit Application" gives an intelligent stage to investigating SpaCy's capacities in tokenization and named element acknowledgment through a direct and outwardly engaging connection point.
