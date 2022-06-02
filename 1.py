# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 14:08:15 2022

@author: MSI
"""

import csv
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.title("Game Searching")
image=Image.open("game.jpeg")
st.image(image, caption=None, use_column_width=False,width=None)

def amazing():
        video_file=open('amazing.mp4','rb')
        video_bytes=video_file.read()
        st.video(video_bytes)
        st.stop()

def sort():
    st.session_state.result.sort(key=lambda x:x[18],reverse=True)
      
def byname():
    if st.session_state.name=='dasima':
        amazing()
    list1=[]
    for row in st.session_state.result:
        if st.session_state.name in row[1]:
            list1.append(row)
    st.session_state.result=list1

def bydate():
    list1=[]
    for row in st.session_state.result:
        if st.session_state.date<=row[2]:
            list1.append(row)
    st.session_state.result=list1

def byenglish0():
    list1=[]
    for row in st.session_state.result:
        if '0'==row[3]:
            list1.append(row)
    st.session_state.result=list1
    
def byenglish1():
    list1=[]
    for row in st.session_state.result:
        if '1'==row[3]:
            list1.append(row)
    st.session_state.result=list1
    

def bydeveloper():
    list1=[]
    for row in st.session_state.result:
        if st.session_state.developer==row[4]:
            list1.append(row)
    st.session_state.result=list1
            
def bypublisher():
    list1=[]
    for row in st.session_state.result:
        if st.session_state.publisher==row[5]:
            list1.append(row)
    st.session_state.result=list1

def byplatforms():
    if 'pf' not in st.session_state:
        st.session_state.pf=st.session_state.platforms[0]
    for i in range(1,len(st.session_state.platforms)):
        st.session_state.pf+=';'
        st.session_state.pf+=st.session_state.platforms[i]
    list1=[]
    for row in st.session_state.result:
        if st.session_state.pf in row[6]:
            list1.append(row)
    st.session_state.result=list1

def byage18():
    list1=[]
    for row in st.session_state.result:
        if '18'==row[7]:
            list1.append(row)
    st.session_state.result=list1
    
def byage0():
    list1=[]
    for row in st.session_state.result:
        if '0'==row[7]:
            list1.append(row)
    st.session_state.result=list1

def bycategory():
    if 'ca' not in st.session_state:
        st.session_state.ca=st.session_state.category[0][0]
    for i in range(1,len(st.session_state.category)):
        st.session_state.ca+=';'
        st.session_state.ca+=st.session_state.category[i][0]
    list1=[]
    for row in st.session_state.result:
        if st.session_state.ca in row[8]:
            list1.append(row)
    st.session_state.result=list1

def bygenres():
    if 'ge' not in st.session_state:
        st.session_state.ge=st.session_state.genres[0][0]
    for i in range(1,len(st.session_state.genres)):
        st.session_state.ge+=';'
        st.session_state.ge+=st.session_state.genres[i][0]
    list1=[]
    for row in st.session_state.result:
        if st.session_state.ge in row[9]:
            list1.append(row)
    st.session_state.result=list1

def bytags():
    if 'ta' not in st.session_state:
        st.session_state.ta=st.session_state.tags[0][0]
    for i in range(1,len(st.session_state.tags)):
        st.session_state.ta+=';'
        st.session_state.ta+=st.session_state.tags[i][0]
    list1=[]
    for row in st.session_state.result:
        if st.session_state.ta in row[10]:
            list1.append(row)
    st.session_state.result=list1

def byach():
    list1=[]
    for row in st.session_state.result:
        if row[0]=='appid':
            continue
        if int(row[11])>=int(st.session_state.slider):
            list1.append(row)
    st.session_state.result=list1

def byprice():
    list1=[]
    for row in st.session_state.result:
        if row[0]=='appid':
            continue
        if float(row[17])<=float(st.session_state.price):
            list1.append(row)
    st.session_state.result=list1

if 'photo' not in st.session_state:
    with open("steam_media_data.csv",encoding='utf8') as photo:
        photo_csv=csv.reader(photo)
        photo=list(photo_csv)
        st.session_state.photo=photo

if 'result' not in st.session_state:
    with open('steam.csv',encoding='utf8') as steam:
        steam_csv=csv.reader(steam)
        result=list(steam_csv)
        st.session_state.result=result
        # row[0]  = game_id
        # row[1]  = name
        # row[2]  = release_date
        # row[3]  = english_support   (if game support english, this value is 1)
        # row[4]  = developer
        # row[5]  = publisher
        # row[6]  = platforms         (Windows or Linux or MacOS)
        # row[7]  = required_age      (All age or 18+)
        # row[8]  = categories
        # row[9]  = genres
        # row[10] = steam_tags        (Tags in steam)
        # row[11] = achievements      (Number of game achievements)
        # row[12] = positive_ratings  (Number of people rate positive in steam)
        # row[13] = negative_ratings  (Numebr of people rate negative in steam)
        # row[14] = average_playtime
        # row[15] = median_playtime
        # row[16] = owners
        # row[17] = price (USD)
        for row in  st.session_state.result:
            if row[0]=='appid':
                continue
            row.append(int(row[12])-int(row[13])) # row[18] = positive_ratings - negative_ratings
            row[16]=row[16][:row[16].index('-')] # Cut text after '-' in owners
            row[16]=int(row[16]) # Change str to int in owners
            row[14]=int(row[14]) # Change str to int in average_playtime
        

st.write("Total Game:",len(st.session_state.result)) 
number=""
option=st.selectbox(
    'Searching by ...',
    ('name','release date','English Support','developer','publisher',
     'platforms','required age','category','genres','steam_tags',
     'achievements','price'))
number=option

if st.button('Next'):
    if number=='name':
        name=st.text_input('Name',on_change=byname,key='name')
    if number=='release date':
        date=st.text_input('Release date(xxxx-xx-xx)',on_change=bydate,key='date')
    if number=='English Support':
        english1=st.checkbox('Support English',on_change=byenglish1)
        english0=st.checkbox('No English',on_change=byenglish0)
    if number=='developer':
        developer=st.text_input('Developer',on_change=bydeveloper,key='developer')
    if number=='publisher':
        publisher=st.text_input('Publisher',on_change=bypublisher,key='publisher')
    if number=='platforms':
        with st.form(key='platforms'):
            multiselect=st.multiselect(
                'Platforms:',
                ['windows','mac','linux'],key='platforms')
            st.form_submit_button('Next',on_click=byplatforms)
    if number=='required age':
        adult=st.checkbox('18+',on_change=byage18)
        allage=st.checkbox('All age',on_change=byage0)
        
    if number=='category':
        list_category=st.session_state.result
        list_category1={}
        for row in list_category:
            if ';' in row[8]:
                for i in row[8].split(';'):
                    if i in list_category1.keys():
                        list_category1[i]+=1
                    else:
                        list_category1[i]=1
            else:
                if row[8] in list_category1.keys():
                    list_category1[row[8]]+=1
                else:
                    list_category1[row[8]]=1
        list_category1=sorted(list_category1.items(),key=lambda x:x[1],reverse=True)
        with st.form(key='category'):
            multiselect_category=st.multiselect(
                'Category:',
                [i for i in list_category1],key='category')
            st.form_submit_button('Next',on_click=bycategory)

    if number=='genres':
        list_genres=st.session_state.result
        list_genres1={}
        for row in list_genres:
            if ';' in row[9]:
                for i in row[9].split(';'):
                    if i in list_genres1.keys():
                        list_genres1[i]+=1
                    else:
                        list_genres1[i]=1
            else:
                if row[9] in list_genres1.keys():
                    list_genres1[row[9]]+=1
                else:
                    list_genres1[row[9]]=1
        list_genres1=sorted(list_genres1.items(),key=lambda x:x[1],reverse=True)
        with st.form(key='genres'):
             multiselect_genres=st.multiselect(
                 'Genres:',
                 [i for i in list_genres1],key='genres')
             st.form_submit_button('Next',on_click=bygenres)
             
    if number == 'steam_tags':
        list_tags=st.session_state.result
        list_tags1={}
        for row in list_tags:
            if ';' in row[10]:
                for i in row[10].split(';'):
                    if i in list_tags1.keys():
                        list_tags1[i]+=1
                    else:
                        list_tags1[i]=1
            else:
                if row[10] in list_tags1.keys():
                    list_tags1[row[10]]+=1
                else:
                    list_tags1[row[10]]=1
        list_tags1=sorted(list_tags1.items(),key=lambda x:x[1],reverse=True)
        with st.form(key='tags'):
              multiselect_tags=st.multiselect(
                  'Steam_tags:',
                  [i for i in list_tags1],key='tags')
              st.form_submit_button('Next',on_click=bytags)
        
    if number=='achievements':
        with st.form(key='slider'):
              achievements=st.slider("Achievements:",0,1000,100,key='slider')
              st.form_submit_button('Next',on_click=byach)
        
    if number=='price':
        with st.form(key='price'):
              price=st.slider("Price(USD):",0.0,100.0,0.0,key='price')
              st.form_submit_button('Next',on_click=byprice)
              
   
with st.form(key='resultnum'):
      price=st.slider("Result:",0,len(st.session_state.result),0,key='resultnum')
      st.form_submit_button('Next',on_click=sort)
      
    
        

if st.button('Result(all information)'):  
    no=1
    for row in st.session_state.result:
        st.write("No."+str(no)+":")
        for row1 in st.session_state.photo:
            if row1[0]==row[0]:
                response=requests.get(row1[1])
                img=Image.open(BytesIO(response.content))
                st.image(img,caption=row[1])
        st.write("Release_date: "+row[2])
        if row[3]=='1':
            st.write("Support English!")
        if row[3]=='0':
            st.write("No English!")
        st.write("Developer: "+row[4])
        st.write("Publisher: "+row[5])
        st.write("Platforms: "+row[6])
        if row[7]=='18':
            st.write("Required age: 18+")
        if row[7]!='18':
            st.write("Required age: all")
        st.write("Category: "+row[8])
        st.write("Genres: "+row[9])
        st.write("Steam_tags: "+row[10])
        st.write("Achievements: "+row[11])
        st.write("Positive_ratings: "+row[12])
        st.write("Negative_ratings: "+row[13])
        st.write("Average playtime: ",row[14])
        st.write("Owners: ",row[16])
        st.write("Price(USD): "+row[17])
        no=no+1
        if st.session_state.resultnum==no-1:
            break
        
if st.button('Result(only name)'):
    no=1
    for row in st.session_state.result:
        st.write("No."+str(no)+":")
        for row1 in st.session_state.photo:
            if row1[0]==row[0]:
                response=requests.get(row1[1])
                img=Image.open(BytesIO(response.content))
                st.image(img,caption=row[1])
        no=no+1
        if st.session_state.resultnum==no-1:
            break