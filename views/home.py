import streamlit as st
from PIL import Image

def load_view():
    image = Image.open('./assets/images/why.png')
   
    st.markdown("""
    <div class="container"> 
    <div class='cut-text' style = "position:center;">SmartVisionAI</div>
    <h1>  “The Future begins with us” </h1> <br>
    <p>SmartVisionAI is  an Artificial Intelligence-based solution  we provide to help detect potentially dangerous or illegal objects in within different luggage
     With robust & fast algorithms at its core, SmartVisionAI detects prohibited items in real-time from X-ray Baggage Scanner 
    </p>
    <h2> Why SmartVisionAI ? </h2>
    <br>
    <p>
    The current approach with luggage verification depends on human observation thus a high error rate and slower processing
    <ul>
    <li>
    8 out of 10 tests Banned items made it through US airport security 
    </li>
    <li> 
    0.28 percent of times flight delay is caused by security delays (baggage scan) in 2017
    </li>
    </ul> """
    ,unsafe_allow_html=True)
    st.image(image)
    st.markdown("""</p>
    </div>
    """,unsafe_allow_html=True)