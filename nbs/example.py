# AUTOGENERATED! DO NOT EDIT! File to edit: app_streamlit.ipynb.

# %% auto 0
__all__ = []

# %% app_streamlit.ipynb 1
from datetime import datetime

import streamlit as st

from streamlit_jupyter import StreamlitPatcher, tqdm

# %% app_streamlit.ipynb 3
st.title("Example")

# %% app_streamlit.ipynb 4
st.markdown(
    """

This is a test page demonstrating the use of `streamlit_jupyter`.

If you're seeing this in jupyter, then it's working!

"""
)

# %% app_streamlit.ipynb 5
name = st.text_input("What's your name?", "John")

# %% app_streamlit.ipynb 6
st.markdown(f"## Hello {name}!\n## The date is TODAY")

# %% app_streamlit.ipynb 7
from nbdev_tutorial.core_2 import say_hola

st.markdown(f"## Desde Module core_2 {say_hola(name)}!\n## The date is TODAY")
