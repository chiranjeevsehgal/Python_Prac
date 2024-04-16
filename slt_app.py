import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import cv2 as cv
from matplotlib import pyplot as plt

from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from wordcloud import STOPWORDS

def display_home():
    st.header("EXAM!")
    # st.write("""
    # Exam
    # """)

def visualizaionfunc():
    if option == "3D Plot Visualization":
        st.subheader('3D Plot Visualization')

        
        data=pd.read_csv('WomensClothingE_CommerceReviews.csv')
        st.dataframe(data)

        st.subheader('Data Insights')
        product_preferences = data.groupby('Department Name')['Positive Feedback Count'].sum().reset_index()
        bar_fig = px.bar(product_preferences, x='Department Name', y='Positive Feedback Count', title='Distribution by Department')
        st.plotly_chart(bar_fig)

        
        st.subheader('3D Plot between Age, Rating and Positive Feedback Counts')
        fig = go.Figure(data=[go.Scatter3d(
            x=data['Age'],
            y=data['Rating'],
            z=data['Positive Feedback Count'],
            mode='markers',
            marker=dict(
            size=8,
            color=data['Positive Feedback Count'],
            colorscale='Viridis',
            opacity=0.8
            )
        )])

        fig.update_layout(scene=dict(
            xaxis_title='Age',
            yaxis_title='Rating',
        zaxis_title='Positive Feedback Count'
        ))

        st.plotly_chart(fig)

        
def imageprocessingfunc():
    if option == "Image Processing":
        st.subheader('Image Processing')
        st.sidebar.title('Dashboard Options')
        dashboard_selectbox = st.sidebar.selectbox(
        'Select Technique:',
        ('Original','Resize', 'Grayscale Conversion', 'Cropping', 'Rotation')
        )
        

        
        if dashboard_selectbox == 'Original':
            
            img = cv.imread('image1.jpg')
            print(img.shape)

            image_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            st.image(image_rgb, caption='Original Image')
            



        if dashboard_selectbox == 'Resize':
            
            img = cv.imread('image1.jpg')
            resized = cv.resize(img, (140, 198))

            image_resized = cv.cvtColor(resized, cv.COLOR_BGR2RGB)
            st.image(image_resized, caption='Resized Image')



        if dashboard_selectbox == 'Grayscale Conversion':
            
            img = cv.imread('image1.jpg')
            grayscaleimg= cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

            image_grayscale = cv.cvtColor(grayscaleimg, cv.COLOR_BGR2RGB)
            st.image(image_grayscale, caption='Grayscale Image')
            


        if dashboard_selectbox == 'Cropping':
            
            img = cv.imread('image1.jpg')
            crop = img[0:90, 0:90]
            
            image_crop = cv.cvtColor(crop, cv.COLOR_BGR2RGB)
            st.image(image_crop, caption='Cropped Image')
        
        
        if dashboard_selectbox == 'Rotation':
            
            img = cv.imread('image1.jpg')

            (height, width) = img.shape[:2]
            center = (width / 2, height / 2)

            angle = 45
            scale = 1.0
            matrix = cv.getRotationMatrix2D(center, angle, scale)
            rotate = cv.warpAffine(img, matrix, (width, height))


            image_rotate = cv.cvtColor(rotate, cv.COLOR_BGR2RGB)
            st.image(image_rotate, caption='Cropped Image')
            

def txtanalysisfunc():
    if option == "Text Analysis":
        st.subheader('Text Analysis')


        st.subheader('Original Dataset')
        data=pd.read_csv('WomensClothingE_CommerceReviews.csv')
        st.dataframe(data)

        

        def preprocess_text(content):

            tokenizer = RegexpTokenizer("[A-Za-z]+")
            words3 = tokenizer.tokenize(str(content))

            stop_words = set(STOPWORDS)
            filtering_list = []

            for word in words3:
                if word.casefold() not in stop_words:
                    filtering_list.append(word)

            stemmer = PorterStemmer()
            stemming_words = [stemmer.stem(word.lower()) for word in filtering_list]

            return stemming_words
        
        if st.button('Preprocess data'):
            data["Review"] = data["Review"].apply(preprocess_text)

            st.subheader('Preprocessed Dataset')
            st.dataframe(data)
        
        if st.button('Similarity Analysis'):

            data["Division Name"].value_counts()
            general = data[data["Division Name"]== "General"]
            general_petite = data[data["Division Name"]== "General Petite"]
            initmate = data[data["Division Name"]== "Initmates"]

            token1 = set(preprocess_text(general))
            token2 = set(preprocess_text(general_petite))
            token3 = set(preprocess_text(initmate))

            def jaccard_similarity(set1,set2):
                intersection1=len(set1.intersection(set2))
                # intersection2 = len(intersection1.intersection(set3))
                union1=len(set1.union(set2))
                # union2=len(union1.union(set3))
                return intersection1/union1

            similarity_score1 = jaccard_similarity(token1, token2)
            # similarity_score1 = jaccard_similarity(token1, token2,token3)
            # print(f"Jaccard similarity: {similarity_score1}")

            st.success(f"Jaccard Similariy is: {similarity_score1}")
                

            
            



def reset_page():
    st.session_state.page = "Home"  

if 'page' not in st.session_state:
    st.session_state.page = 'home'

st.title('Python Exam')

st.sidebar.markdown('---')


st.sidebar.title('Dashboard Options')

option = st.sidebar.radio("Choose an action:", ("Home","3D Plot Visualization","Image Processing", "Text Analysis"),index=0, on_change=reset_page)

st.sidebar.markdown('---')



if option == "Home":
    display_home()
elif option == "3D Plot Visualization":
    visualizaionfunc()
elif option == "Image Processing":
    imageprocessingfunc()
elif option == "Text Analysis":
    txtanalysisfunc()









