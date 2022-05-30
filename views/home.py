import streamlit as st
from PIL import Image


def load_view():

    st.markdown("""
    <div class="container"> 
        <div class="hero">
            <div class="hero-content">
                <div>
                    <h1>
                        “The Future begins with us” 
                    </h1> <br>
                    <p>
                        <b>SmartVisionAI</b> is  an Artificial Intelligence-based solution  we provide to help detect potentially dangerous or illegal objects in within different luggage
                        <br/>
                        With robust & fast algorithms at its core, <b>SmartVisionAI</b> detects prohibited items in real-time from X-ray Baggage Scanner 
                    </p>
                </div>
            </div>
        </div>
        <div class="why-section">
            <div>
                <h2>
                    Why SmartVisionAI ?
                </h2>
                <p>
                    The current approach with luggage verification depends on human observation thus a high error rate and slower processing
                </p> 
                <ul>
                    <li>
                        8 out of 10 tests Banned items made it through US airport security 
                    </li>
                    <li> 
                        0.28 percent of times flight delay is caused by security delays (baggage scan) in 2017
                    </li>
                </ul>
            </div>
            <div class="why-section-image">
                <img src="https://github.com/MohamedBoutaieb/SmartVisionAI/blob/main/assets/images/why.png?raw=true">
            </div>
        </div>
        <div class="industries-section">
            <h1>INDUSTRIES</h1>
            <div class="industries-grid">
                <div class="grid-item">
                    <img src="https://www.baggageai.com/assets/images/industry/airport.png">
                </div> 
                <div class="grid-item">
                    <img src="https://www.baggageai.com/assets/images/industry/malls-and-parcel.png">
                </div> 
                <div class="grid-item">
                    <img src="https://www.baggageai.com/assets/images/industry/metros-railways.png">
                </div> 
                <div class="grid-item">
                    <img src="https://www.baggageai.com/assets/images/industry/stadiums-events.png">
                </div> 
                <div class="grid-item">
                    <img src="https://www.baggageai.com/assets/images/industry/prison.png">
                </div> 
                <div class="grid-item">
                    <img src="https://www.baggageai.com/assets/images/industry/schools.png">
                </div> 
            </div>
        </div>
        <div class="who-section">
            <h1>CLIENTS</h1>
            <img src="https://github.com/MohamedBoutaieb/SmartVisionAI/blob/main/assets/images/whom.png?raw=true">
        </div>
    </div>
    """, unsafe_allow_html=True)
