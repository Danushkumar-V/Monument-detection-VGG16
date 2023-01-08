import numpy as np
import pandas as pd
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import tensorflow as tf
import cv2
from PIL import Image, ImageOps
import output1 as po



@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('D:\DK\Dev\monuments-detection\my_model3.hdf5')
    return model
model = load_model()


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def image_preprocessing(image_data, model):
    size = (224, 224)   
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    image = np.asarray(image)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_reshape = img[np.newaxis,...]
    prediction = model.predict(img_reshape)
    return prediction


lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_8autcbbt.json")

class_names = ['Ajanta Caves', 'Charar-E- Sharif', 'Chhota_Imambara', 'Ellora Caves', 'Fatehpur Sikri', 'Gateway of India', "Humayun's Tomb", 'India gate pics', 'Khajuraho', 'Sun Temple Konark', 'alai_darwaza', 'alai_minar', 'basilica_of_bom_jesus', 'charminar', 'golden temple', 'hawa mahal pics', 'iron_pillar', 'jamali_kamali_tomb', 'lotus_temple', 'mysore_palace', 'qutub_minar', 'tajmahal', 'tanjavur temple', 'victoria memorial']

st.markdown('''
# Monuments detector **app**
This **Monuments detector** created using `Python` + `Streamlit` + `Pre-trained VGG16 architecture` !
''')

st_lottie(
        lottie_hello,
        speed=1,
        reverse=True,
        loop=True,
        quality="low", # medium ; high# canvas
        height=400,
        width=400,
        key=None,
    )

choice = st.selectbox('Select the input mode :', options=['Upload from device','Take photo'], index = 0)

if choice == "Take photo":
    img_file_buffer = st.camera_input("Take a picture")
    if img_file_buffer is None:
        st.text("Please take a photo!")
    else:
        image = Image.open(img_file_buffer)
        predictions = image_preprocessing(image, model)
        score = tf.nn.softmax(predictions[0])
        po.printoutput(score)

        max = 0.0
        max_index = 0
        for i in range(0, len(score)):
            if(score[i] > max):    
                max = score[i]
                max_index = i
        if max>0.1:
            st.markdown('''
            # Audio description :
            '''
            )
            monument_name = class_names[max_index]
            audio_file = open('audio/'+monument_name+'.mp3','rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/ogg')
        

elif choice == "Upload from device":
    st.header("Upload your Image here!")
    given_file = st.file_uploader("Upload the jpg or png which should be predicted")
    if given_file is None:
        st.text("Please upload an image file")
    else:
        image = Image.open(given_file)
        st.image(image, use_column_width=True)
        predictions = image_preprocessing(image, model)
        score = tf.nn.softmax(predictions[0])
        po.printoutput(score)
        
        max = 0.0
        max_index = 0
        for i in range(0, len(score)):
            if(score[i] > max):    
                max = score[i]
                max_index = i
        if max>0.1:
            st.markdown('''
            # Audio description :
            '''
            )
            monument_name = class_names[max_index]
            audio_file = open('audio2/'+monument_name+'.mp3','rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/ogg')
        


# img_file_buffer = st.camera_input("Take a picture")








