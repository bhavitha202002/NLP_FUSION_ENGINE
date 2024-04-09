#Import section
import streamlit as st

#Configuring page
st.set_page_config(
    page_title="Grammar Correction",
    page_icon="✅",
)

#Heading
st.write('# <span style="color:darkblue"> Grammar Correction</span>', unsafe_allow_html=True)

# Input incorrect text from user
user_input = st.text_area(f"**Enter a sentence with potential grammar issues:**")

#Summarize button
result = st.button("Fix Grammar", type="primary")

#Generating output
if result :
    #Display a progress bar for loading the model and tokenizer
    progress_bar = st.progress(1,text="Importing libraries... 1%")
    from transformers import T5ForConditionalGeneration, T5Tokenizer
    progress_bar.progress(5,text="Loading Tokenizer...5%")

    # Load the saved model from the local path
    local_model_path = "C:/Users/B.Bhavitha/OneDrive/Desktop/NLP FUSION ENGINE/Grammar_correction_model"

    #Load tokenizer and model from the local directory
    tokenizer = T5Tokenizer.from_pretrained(local_model_path)

    #Loading Model
    progress_bar.progress(20,text="Loading Model...20%") # Update progress bar
    model = T5ForConditionalGeneration.from_pretrained(local_model_path)
    
    #Configuring parameters
    progress_bar.progress(50,text="Configuring parameters...50%")
    args = {"num_beams": 5, "min_length": 1}

    #Encoding inputs
    progress_bar.progress(70,text="Encoding inputs...70%")
    input_ids = tokenizer.encode(f"grammar: {user_input}", return_tensors="pt")

    #Generating output
    progress_bar.progress(80,text="Generating outputs...80%")
    output = model.generate(input_ids, **args)

    #Decoding outputs
    progress_bar.progress(90,text="Decoding output...90%")
    corrected_text = tokenizer.decode(output[0], skip_special_tokens=True)

    #Displaying outputs
    progress_bar.progress(100,text="Completed...100%")
    st.success("Sentence Corrected Successfully")
    corrected_grammar = st.text_area("Corrected sentence",corrected_text)

else:
    st.write('Please click **Fix Grammar** button to receive a grammatically improved version')

