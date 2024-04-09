#Import section
import streamlit as st

#configuring page
st.set_page_config(
    page_title="Text Summarization",
    page_icon="📝",
)

#Heading
st.write('# <span style="color:darkblue"> Text Summarization</span>', unsafe_allow_html=True)

#Input the text to be summarized
input_text = st.text_area(f"**Enter text to be summarized**")

#Taking input for summary length
max_length = st.slider(f'**Enter the length of summary you want**', 0, 200, 100)

#Summarize button
result = st.button("Summarize", type="primary")
if result : 
    # Display a progress bar for loading the model and tokenizer
    progress_bar = st.progress(1,text="Importing libraries...1%")
    from transformers import pipeline, BartTokenizer, BartForConditionalGeneration
    progress_bar.progress(5,text="Loading Tokenizer...5%")

    # Local directory where the model and tokenizer are saved
    local_model_path = 'C:/Users/B.Bhavitha/OneDrive/Desktop/NLP FUSION ENGINE/Text_Summarization_model'

    # Load tokenizer and model from the local directory
    
    tokenizer = BartTokenizer.from_pretrained(local_model_path)
    
    # Loading Model
    progress_bar.progress(20,text="Loading Model.... 20%")  # Update progress bar
    model = BartForConditionalGeneration.from_pretrained(local_model_path)
    
    # Use pipeline for summarization]
    progress_bar.progress(50,text = "Loading pipeline... 50%")  # Update progress bar
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, device=-1)

    # Summarizing
    progress_bar.progress(65,text = "Summarizing ... 65%")  # Update progress bar
    summary = summarizer(input_text, max_length=max_length, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)

    #Generation
    progress_bar.progress(85,text = "Generating outpt.... 85%")  # Update progress bar
    summarized_text = summary[0]['summary_text']

    progress_bar.progress(100,text = "Completed..100%")  # Update progress bar
    st.success("Text Summarized Successfully")

    #Displaying output
    output = st.text_area(f"**Summarized Text**",summarized_text)

else:
    st.write('Please click **Summarize** button to summarize')


