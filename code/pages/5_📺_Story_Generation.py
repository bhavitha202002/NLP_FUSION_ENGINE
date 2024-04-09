#import section
import streamlit as st
import requests

#page configuration
st.set_page_config(
    page_title="Story Generation",
    page_icon="📺",
)

#Heading
st.write('# <span style="color:darkblue"> Story Generation</span>', unsafe_allow_html=True)

#Taking genre input from user
genre = st.selectbox(
    f'**Please select genre for your story**',
    ('Science Fiction','Fantasy','Romance','Mystery','Horror'),
    index=None,
   placeholder="Select genre")

#Input title from user
title = st.text_input(f'**Please enter story title**', placeholder='title')

#Input number of characters from user
no_of_characters = st.number_input(f'**Enter number of main characters in story**',min_value=1, step=1)

#Input name and gender of characters
characters={}
for i in range(1,no_of_characters+1):
    name = st.text_input(f'**Enter name of character{i}**', placeholder='Select gender')
    gender = st.selectbox(f'**Select gender of character{i}**',('Male','Female','Other'),index=None,placeholder='Select gender')
    characters[name]=gender

#slider to take maxlength of story
max_length = st.slider(f"**Enter story size**", min_value=50, max_value=200, value=100, step=1)

#Generate button
result = st.button(f"**Generate Story**", type="primary")

if result : 
# Set your OpenAI API key
    with st.spinner(f'Please wait...generating story'):
        api_key = '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'

        # Provide input for story generation
        character_list = ', '.join([f"{name} ({gender})" for name, gender in characters.items()])

        prompt = f"""
        Genre: {genre}
        Title: {title}
        Main Characters: {character_list}

        """
        url = "https://api.openai.com/v1/engines/gpt-3.5-turbo-instruct/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        data = {
            "prompt": prompt,
            "max_tokens": max_length,
            "temperature": 0.7,
            "n": 1,
            "stop": None
        }

        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()

        # Extracting the generated story text from the response
        generated_story = response_data['choices'][0]['text'].strip() if 'choices' in response_data else ""

        
    st.success("Story generated Successfully")
    #Display output
    index = generated_story.rfind('.')
    final_result = generated_story[:index+1:]
    output = st.text_area(f"**Generated story**",final_result)
    
else:
    st.write('Please click **Generate story** button to generate the story')

 