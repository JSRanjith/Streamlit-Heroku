# -*- coding: utf-8 -*-
"""App.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y25uraeodQImDVYNUxbun6a4hUvgL6jj
"""

import streamlit as st

st.title("SUBTRACTION OF 2 NUMBERS")
st.header("User Input Values")
a = st.number_input('Number-1')
b = st.number_input('Number-2')
st.write(a, ' - ', b , '= ',a - b)

