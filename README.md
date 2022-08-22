# Welcome to TMB Streamlit `links page`

<img src="streamlit-links-page.png" width="350">


> A Streamlit app that you can build for free to store all your personal links that is similar in functionality to that of [Linktr.ee](https://linktr.ee/).

<img src="23F54497-245E-413F-99C7-F3E295E4EA13.png" width="350">

# Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chanin.streamlitapp.com/)

# How to Setup

Getting your own Streamlit `links page` up and running is really easy, just follow the following 3 steps:

**Step 1**. [Click here](https://github.com/dataprofessor/links/generate) to generate a copy of this repository. Next, name your new repository to anything you'd like except for `your username`.github.io

**Step 2**. Customize the contents of the newly generated `links page` by editing the `streamlit_app.py` file:

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


**Step 3**. Deploy to [Streamlit Cloud](https://streamlit.io/cloud). Log-in and click on the **New app** button. Choose the newly generated repo from Steps 1-2. Finally click on the **Deploy!** button. 

After a few moments your new `links page` should be accessible at `https://share.streamlit.io/{your-username}/{newly-created-repo}`

In an upcoming release of Streamlit Cloud, you will be able to customize the URL address to `https://{custom-name--here}.streamlitapp.com/` such as the one that I've created at https://chanin.streamlitapp.com/
