import streamlit as st
import base64

st.set_page_config(
    page_title="NLP FUSION ENGINE",
    page_icon="nlp_icon.png",

)


main_bg = "blue-thistle-free-solidcolor-background.jpg"
main_bg_ext = "jpeg"

side_bg = "relax-free-solidcolor-background-green.jpg"
side_bg_ext = "jpeg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.write("# Welcome to NLP FUSION ENGINE!👋")

st.sidebar.success("Feel free to check out our features")

st.markdown(
    """
    The NLP Fusion Engine project is an integrated and advanced Natural Language Processing System that combines multiple NLP tasks seamlessly.
    This fusion engine aims to enhance language understanding and generation by incorporating NLP state of art into a cohesive and efficient platform. 
    The goal is to provide a versatile tool that leverages cutting-edge NLP techniques to address diverse linguistic challenges 
    ultimately improving communication and content creation across various domains.\n

    **👈 Select a feature from the sidebar** to explore what **NLP FUSION ENGINE** can do!

    ### NLP Fusion Engine Capabilities
    🆎 Language Translation  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
    📝 Text Summarization  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    📧 Email generation \n
    ✅ Grammar correction &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    📺 Story generation


    ### Want to know more?
    - Jump into our [github page](https://github.com/bhavitha202002/NLP_FUSION_ENGINE)
    - Check out our [models](https://github.com/bhavitha202002/NLP_FUSION_ENGINE/models)
    - Dive into [datasets](https://github.com/bhavitha202002/NLP_FUSION_ENGINE/datasets)
    - Take a look at [notebooks](https://github.com/bhavitha202002/NLP_FUSION_ENGINE/tree/main/notebooks)

"""
)