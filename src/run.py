import json

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st
from PIL import Image
import os

import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from db.models import Message


# Login
login_option = st.sidebar.radio('Login/Singup', ('Login', 'Singup'))
if login_option == 'Login':
    with st.sidebar.form("login"):
        st.write("Login Here.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Login")
        if submitted:
            pass
else:
    with st.sidebar.form("signup"):
        st.write("Singup Here.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Singup")
        if submitted:
            pass

# Banner
banner = Image.open('./data/banner.webp', )
st.image(banner)
st.title(':zap: Pytopia Dashboard')

# Questions
with st.expander('Q / A'):
    query = st.text_input('Search:')

    # select top 10 from messages
    for msg in Message.objects.all().order_by('-date'):
        if not msg.text or msg.text[-1] not in '؟?':
            continue

        if query and query not in msg.text:
            continue

        col1, col2 = st.columns([1, 4])
        col1.write(f'**{msg.user.username}**')
        col2.write(msg.text.replace(query, f'**{query}**'))

    col1, col2 = st.columns(2)
    col1.button('< Previous')
    col2.button('Next >')
