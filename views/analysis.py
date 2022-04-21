import streamlit as st
from PIL import Image
import torch
import gdown

  
def load_view():
    downloaded = False  
    st.title('SmartVisionAI detects prohibited items in real-time from X-ray Baggage Scanner')
    st.subheader("""
        SmartVisionAI is an Artificial Intelligence-based solution which ensures accuracy and efficiency in threat-detection at security checkpoints. With robust & fast algorithms at its core
        """)
    file = st.file_uploader('Upload Image', type = ['jpg','png','jpeg'])
    if file!= None:    
        
        img1 = Image.open(file)
        st.image(img1, caption = "Uploaded Image")

        st.text("confidence threshold is the minimum score that the model will consider the prediction to be a true prediction (otherwise it will ignore this prediction entirely)")
        confThreshold =st.slider('Confidence', 0, 100, 50)

        st.text("IoU threshold is the minimum overlap between ground truth and prediction boxes for the prediction to be considered a true positive.")
        nmsThreshold= st.slider('IoU Threshold', 0, 100, 20)

        if st.button("Download Model"):

            if not downloaded : 
                download_bar = st.progress(0)
                url = "https://drive.google.com/file/d/1-3lfM37xcm4CNwJmHbs9n8PBeO20h22W/view?usp=sharing"
                download_bar.progress(20)
                gdown.download(url=url, quiet=False, fuzzy=True)
                download_bar.progress(100)
                downloaded = True
        
        if st.button('Predict'):
            object_detection_image(img1, confThreshold, nmsThreshold)