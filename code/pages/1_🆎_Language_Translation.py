import streamlit as st
import subprocess
import sys

# Import google translator
import googletrans
from googletrans import Translator



# Configuring page
st.set_page_config(
    page_title="Language Translation",
    page_icon="🆎",
)


#Heading
st.write('# <span style="color:darkblue"> Language Translator</span>', unsafe_allow_html=True)

#Extracting the supported Languages
language=googletrans.LANGUAGES
all_languages=list(language.values())

#Input for source Language
src_language = st.selectbox(
    f'**Please select source language**',
    all_languages,
    index=None,
   placeholder="Select source language")

#Input for source text 
source_text = st.text_area(f"**Enter source language text**")

#Input for target language
target_lang = st.selectbox(
    f'**Please select target language**',
    all_languages,
    index=None,
   placeholder="Select target language")

#Translate button
result = st.button("Translate", type="primary")
if result : 
    with st.spinner(f'Please Wait...translating your text into {target_lang}'):
        # Translating from source text to target text
        t1 = Translator()
        trans_text=t1.translate(source_text,src=src_language,dest=target_lang)
        trans_text=trans_text.text
    st.success("Text Generated Successfully")
    output = st.text_area(f'**Translation**',trans_text)
else:
    st.write('Please click **Translate** button to translate')
