import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Teresia Mrema Buza, Ph.D.')

st.info('Self-Trained Developer, Data Scientist and Multi-Omics Bioinformatics Scientist')

icon_size = 20

# st_button('youtube', 'https://youtube.com/dataprofessor', 'Data Professor YouTube channel', icon_size)
# st_button('youtube', 'https://youtube.com/codingprofessor', 'Coding Professor YouTube channel', icon_size)
# st_button('medium', 'https://data-professor.medium.com/', 'Read my Blogs', icon_size)
# st_button('twitter', 'https://twitter.com/thedataprof/', 'Follow me on Twitter', icon_size)
st_button('cdi', 'https://https://complexdatainsights.com/', 'Visit my CDI website', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/teresia-buza-11b77a1b/', 'Follow me on LinkedIn', icon_size)
# st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
# st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)
