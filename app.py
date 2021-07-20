import streamlit as st

# Text/title
st.title("Streamlit Basics")



# header/subheader

st.header("This is header")

st.subheader("This is subheader")


# text
st.text("hello world!!")

# markdown
st.markdown('### This is markdown')


# eror/colorful text
st.success("Successful")

st.info("Information!")

st.warning("This is a warning!!")

st.error("This is an error")

st.exception("NameError('name there not defined')")

# get help info about python

st.help(range)

# writing text

st.write("Text with write")

st.write(range(10))


# image
st.text('Testing  image')
from PIL import Image
img = Image.open('Suyash.jpeg')
st.image(img,caption = "Learning Curve is essential for growth!!")


# video syntax
#video_file = open("example.mp4","rb").read()
#st.video(video_file)

# widget
# check box
if st.checkbox("Show/hide"):
    st.text('Showing or hiding widget')

# radio
status = st.radio("what is your status",("Active","Inactive"))

if status == 'Active':
    st.success("you are active")
else:
    st.warning("Inactve, Activate")
    
# selection box

occupation = st.selectbox("your occupation",["Programmer","Data scientist","Student","Professor","Doctor"]) 

st.write("You selected this option",occupation) 


# multi select 
location = st.multiselect("Where do you work?",("India","London","England","New York","China"))
st.write("you selected",len(location),"locations")
    
# slider

level = st.slider("What is your level",1,5)


# buttons
st.button("simple button")

if st.button("About"):
    st.text("Stream lit is cool!!")
    
    
# text input

firstname = st.text_input("Enter your first name", "Enter here..")

if st.button("Submit"):
    result = firstname.title()
    st.success(result)
    
# text area

msg = st.text_area("Enter your message", "Enter here..")

if st.button("submit"):
    result = msg.title()
    st.success(result)


# data input
import datetime
today = st.date_input("Today is ",datetime.datetime.now())

# time
the_time = st.time_input("This is ",datetime.time())


#displaying json

st.text("display json")
st.json({'name':"acchu", "gender":"Male","hobby":"painting"})


# displaying raw code
st.text("display raw code")
st.code("import numpy as np")

# display with raw code 
with st.echo():
    # this will also display the comment
    import pandas as pd
    df= pd.DataFrame()

# progress bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p+1)
    
    
# spinner
with st.spinner("Waiting...."):
    time.sleep(2)
st.success("finished")


# balloons
st.balloons()

# sidebars
st.sidebar.header("About")
st.sidebar.text("this is streamlit basic ")


# function
@st.cache
def run_fxn():
    return range(100)

st.write(run_fxn())


# plot
st.pyplot()

# dataframe
st.dataframe(df) 

# tables
st.table(df)
