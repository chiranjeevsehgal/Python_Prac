import streamlit as st
# from PIL import Image



def display_home():
    st.header("Welcome!")
    st.write("""
    Exam
    """)

def item1func():
    if option == "Item1":
        st.subheader('Item1')

        
def item2func():
    if option == "Item2":
        st.subheader('Item2')

        

def reset_page():
    st.session_state.page = "Home"  

if 'page' not in st.session_state:
    st.session_state.page = 'home'

st.title('Python Exam')

st.sidebar.markdown('---')


st.sidebar.title('Dashboard Options')

option = st.sidebar.radio("Choose an action:", ("Home","Item1", "Item2"),index=0, on_change=reset_page)

st.sidebar.markdown('---')



if option == "Home":
    display_home()
elif option == "Item1":
    item1func()
elif option == "Item2":
    item2func()
