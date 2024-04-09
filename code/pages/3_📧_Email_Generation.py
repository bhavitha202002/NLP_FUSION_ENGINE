#import section
import streamlit as st
import requests

#page configuration
st.set_page_config(
    page_title="Email Generation",
    page_icon="📧",
)

#Heading
st.write('# <span style="color:darkblue"> Email Generation </span>', unsafe_allow_html=True)

# Set your GPT-3 API key here
api_key = "your_api_key"

#Generate email function
def generate_email(prompt,max_length):
    url = "https://api.openai.com/v1/engines/gpt-3.5-turbo-instruct/completions"
    #https://api.openai.com/v1/completions
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

    #Hit api
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    # Extracting the generated email text from the response
    generated_email = response_data['choices'][0]['text'].strip() if 'choices' in response_data else ""

    return generated_email

# Take input prompt from user
user_prompt = st.text_area(f"**Enter a prompt to generate email**")

#Taking length of email from user
max_length = st.slider(f'**Enter the length of email you want**', 0, 200, 100)

#Generate button
result = st.button("Generate", type="primary")

if result:
    with st.spinner(f'please wait...generating email '):
        #call function
        generated_email = generate_email("write an email to "+user_prompt,max_length)
    st.success("Email generated Successfully")

    #Display output
    index = generated_email.rfind('.')
    final_result = generated_email[:index+1:]
    regards = "\n\nBest Regards\n[Your Name]."
    final_result += regards 

    output = st.text_area(f"**Generated Email**",final_result)
    
else:
    st.write("Please **Generate** button to get output")


