# Welcome to TMB Streamlit `links page`

<img src="streamlit-links-page.png" width="350">


> A Streamlit app that you can build for free to store all your personal links that is similar in functionality to that of [Linktr.ee](https://linktr.ee/).

<img src="23F54497-245E-413F-99C7-F3E295E4EA13.png" width="350">

## Python code
```python
import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Teresia Mrema-Buza')

st.info('Interest in Data Science, Machine Learning, Multi-Omics Bioinformatics and Data Visualization')

icon_size = 20

st_button('linkedin', 'https://www.linkedin.com/in/teresia-buza-11b77a1b/', 'Follow me on LinkedIn', icon_size)

```

