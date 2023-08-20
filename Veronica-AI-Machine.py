from difflib import get_close_matches as find
from os import system
import speedtest
from phonenumbers import timezone,geocoder,carrier
import phonenumbers
import instaloader
from cProfile import run
from distutils.cmd import Command
from email import encoders, message
from email.mime import audio
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import operator
import tkinter
from typing import Dict
from email.mime.text import MIMEText
from http import server
import wolframalpha
from msilib.schema import MIME, Condition
from platform import machine
import os  
from re import M, X
from socket import close
from ssl import _create_default_https_context
from pytube import YouTube
import smtplib
from this import d
from time import sleep, strftime, time
from tkinter import N, PAGES, Y
from pyaudio import paASIO
import subprocess 
import pyttsx3
from bs4 import BeautifulSoup
import webbrowser
import cv2
from requests.api import head
from soupsieve import select
import wikipedia
import requests
import smtplib
import PyPDF2
import time
import os
import sys
# import operator
from requests import get
import datetime
import pyjokes
import pywhatkit
import speech_recognition as sr
import qrcode as qr
import pyautogui
from pyaudio import paASIO
from googletrans import Translator
from pywikihow import search_wikihow
from gtts import gTTS
import googletrans
import random
import keyboard
from  tkinter import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTime, QTimer, QDate, Qt 
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Veronica_GUI import Ui_MainWindow





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 192)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

program = []
progid = []
progdict = {}

cmd = 'powershell "gps |where mainwindowtitle |select Description'
cmd1 = 'powershell "gps |where mainwindowtitle |select id'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
proc1 = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE)
for line in proc.stdout:
    st = str(line.decode().rstrip())
    program.append(st)

for line in proc1.stdout:
    st = str(line.decode().rstrip())
    progid.append(st)

for i in range(0,len(progid)):
    progdict[program[i]]=progid[i]

def close(c):
    global program,progid
    q = find(c,program)
    if q==[]:
        speak("The app is not running")
    else:
        for key,value in progdict.items():
            if key == q[0]:
                speak(f"{key} is closing")
                system("taskkill /im  "+ str(value))

def wishme():
    hour = int(datetime.datetime.now().hour)
    now = datetime.datetime.now()
    
    if hour>=0 and hour<12:
        speak("Good morning Ayush!")
        # speak("its")
        # speak(now.strftime("%H:%M:%S"))
    elif hour>=12 and hour<18:
        speak("Good afternoon Ayush!")
        # speak("its")
        # speak(now.strftime("%H:%M:%S"))
    elif hour>=18 and hour<20:
        speak("Good evening Ayush!")
        # speak("its")
        # speak(now.strftime("%H:%M:%S"))
    else:
        speak("Good night")  

    speak("I am your Personal AI Assistant. how may I help you?")

def news():
        main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513'

        main_page= requests.get(main_url).json()
        articles = main_page["articles"]
        head = []
        day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "nineth", "tenth"]
        for ar in articles:
                head.append(ar["title"])
        for i in range(len(day)):
                speak(f"today's {day[i]} news is: {head[i]}")

def readpdf():
    book = open("Path", 'rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    python  = 'Path'
    speak(f"Total numbers of pages in this book {python} ")
    speak("Ayush please enter the page number i have to read")
    pg = int(input("Please enter the number: "))
    page = pdfreader.getPage(pg)
    text = page.extractText()
    speak(text)




def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)

        try:
                print("Understanding...")
                query = r.recognize_google(audio, language='en-in')
                print(f"You Said: {query}\n")
        except Exception as e:
                return "None"
        return query
def readpdf2():
    book2 = open("Path", 'rb')
    pdfreader = PyPDF2.PdfFileReader(book2)
    pages = pdfreader.numPages
    pdf = 'Verbs.pdf'
    speak(f"Total numbers of pages in this book {pdf} ")
    speak("Ayush please enter the page number i have to read")
    pg = int(input("Please enter the number: "))
    page = pdfreader.getPage(pg)
    text = page.extractText()
    speak(text)

def sendemail(to, content): # please enter the email id and password and where ask person email id write email id
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('your email address', 'your password')
        server.sendmail('your email id', to, content)
        server.close()



class MainThread(QThread):
        def __init__(self):
                super(MainThread, self).__init__()
        def run(self):
                self.TaskExecution()

                

        def takeCommand(self):
                r = sr.Recognizer()
                with sr.Microphone() as source:
                        print("Listening...")
                        r.pause_threshold = 1
                        audio = r.listen(source)

                try:
                        print("Understanding...")
                        query = r.recognize_google(audio, language='en-in')
                        print(f"You Said: {query}\n")
                except Exception as e:
                        return "None"
                return query


        def TaskExecution(self):
                wishme()
                while True:
                        self.query = self.takeCommand()
                        query = takeCommand()
                        def weather():
                                a = self.query.replace("weather", "")
                                a = self.query.replace("report", "")
                                search = "temprature in {a}"
                                url = f"https://www.google.com/search?q={search}"
                                r = requests.get(url)
                                data = BeautifulSoup(r.text,"html.parser")
                                temp = data.find("div",class_ = "BNeawe").text
                                speak(f"Current {search} is {temp}")
                
                        

                        def Meaning():
                                meanby = self.query.split("by", 1)
                                try:
                                        soup = BeautifulSoup(requests.get(f"https://www.google.com/search?q={meanby[1]}+means").text, "html.parser")
                                        word = soup.find("div", class_="v9i61e")                        
                                        words = ["noun", "exclamation"]
                                        word_list = word.text.split()
                                        speak(meanby[1] + " " + "means" + " " + ' '.join([i for i in word_list if i not in words]))
                                        print(meanby[1] + " " + "means" + " " + ' '.join([i for i in word_list if i not in words]))
                                except:
                                        soup = BeautifulSoup(requests.get(f"https://www.google.com/search?q={meanby[1]}+means").text, "html.parser")
                                        word = soup.find("div", class_="BNeawe s3v9rd AP7Wnd")
                                        words = ["noun", "exclamation"]
                                        word_list = word.text.split()
                                        speak(meanby[1] + " " + "means" + " " + ' '.join([i for i in word_list if i not in words]))
                                        print(meanby[1] + " " + "means" + " " + ' '.join([i for i in word_list if i not in words]))

                        # logic building for tasks
                        if 'open youtube' in self.query:
                                speak("opening youtube")
                                webbrowser.open("youtube.com")
                        elif 'open kali' in self.query:
                                speak("opening kali")
                                webbrowser.open("kali.org")
                        elif 'wikipedia' in self.query:
                                speak("Searching wikipedia")
                                self.query = self.query.replace("wikipedia", "")
                                results = wikipedia.summary(self.query, sentences=2)
                                speak("According to wikipedia")
                                speak(results)
                        elif 'open visual studio code' in self.query:
                                speak("opening code")
                                npath = "Path"
                                os.startfile(npath)
                        elif 'open command prompt' in self.query:
                                speak("opening command prompt")
                                os.system("start cmd")
                        elif 'play music' in self.query:
                                # import random
                                music_dir = "C:\\Users\\Asing\\Music"
                                songs = os.listdir(music_dir)
                                # rd = random.choice(songs)
                                for song in songs:
                                        if song.endswith('.mp3'):
                                                os.startfile(os.path.join(music_dir, song))
                        elif 'what is the time' in self.query:
                                now = datetime.datetime.now()
                                speak("Current time is: ")
                                speak(now.strftime("%H:%M:%S"))
                        elif 'ip address' in self.query:
                                ip = get('https://api.ipify.org').text
                                speak(f"Your ip address is {ip}")
                        elif 'open google' in self.query:
                                speak("Sir, what should I search on google")
                                self.cm = self.takeCommand()
                                webbrowser.open(f"{self.cm}")
                        elif 'open notepad' in self.query:
                                os.startfile("Path")
                        elif 'open snipping tool' in self.query:
                                speak("Opening Snipping tool")
                                spath = "Path"
                                os.startfile(spath)
                        elif 'open paint' in self.query:
                                speak("Opening paint")
                                ppath = "Path"
                                os.startfile(ppath)
                        elif 'open word' in self.query:
                                speak("Opening word")
                                wpath = "Path"
                                os.startfile(wpath)
                        elif 'open powerpoint' in self.query:
                                speak("opening powerpoint")
                                rpath = "Path"
                                os.startfile(rpath)
                        elif 'open edge' in self.query:
                                speak("Opening edge")
                                gpath = "Path"
                                os.startfile(gpath)
                        elif 'open chrome' in self.query:
                                speak("opening chrome")
                                opath = "path"
                                os.startfile(opath)
                        elif 'open excel' in self.query:
                                speak("Opening excel")
                                lpath = "path"
                                os.startfile(lpath)
                        elif 'open control panel' in self.query:
                                speak("Opening control panel")
                                qq = "path"
                                os.startfile(qq)
                        elif 'open my google' in self.query:
                                speak("Opening google")
                                webbrowser.open("google.com")
                        elif 'open outlook' in self.query:
                                speak("Opening outlook")
                                outlook = "Path"
                                os.startfile(outlook)
                        elif 'activate how to do mod' in self.query:
                                        
                                speak("How to mod is activated please tell me what you want to know")
                                self.how = self.takeCommand()
                                max_results = 1
                                how_to = search_wikihow(self.how, max_results)
                                assert len(how_to) ==1
                                how_to[0].print()
                                speak(how_to[0].summary)
                        elif 'joke' in self.query:
                                jokes = pyjokes.get_joke()
                                speak(jokes)
                                

                        elif 'close notepad' in self.query:
                                speak("okay Ayush, closing notepad")
                                os.system("taskkill /f /im notepad.exe")
                        elif 'close code' in self.query:
                                speak("Okay Ayush, closing code")
                                os.system("taskkill /f /im code.exe")
                        elif 'shut down' in self.query:
                                speak("Shutting down")
                                os.system("shutdown /s /t 5")
                        elif 'restart' in self.query:
                                speak("Restarting")
                                os.system("shutdown /r /t 5")
                        elif 'sleep' in self.query:
                                os.system("Rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                        elif 'switch the window' in self.query:
                                # import time
                                pyautogui.keyDown("alt")
                                pyautogui.press("tab")
                                time.sleep(5)
                                pyautogui.keyUp("alt")
                        elif 'take screenshot' in self.query or 'take a screenshot' in self.query:
                                # import time
                                speak("Ayush, please tell me the name for this screenshot file")
                                self.name = self.takeCommand()
                                speak("please Ayush hold screen for few seconds, i am taking screenshot")
                                time.sleep(3)
                                img = pyautogui.screenshot()
                                img.save(f"{self.name}.png")
                                speak("i am done Ayush, the screenshot is saved to our main folder. now i am ready for next command")
                        elif 'read my pdf book' in self.query:
                                readpdf()
                        elif 'where i am' in self.query or "what is my location" in self.query:
                                speak("Wait Ayush, let me check")
                                try:
                                        ipAdd = requests.get('https://api.ipify.org').text
                                        print(ipAdd)
                                        url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                                        geo_requests = requests.get(url)
                                        geo_data = geo_requests.json()
                                        city = geo_data['city']
                                        country = geo_data['country']
                                        speak(f"Ayush, i am not sure, but i think we are in {city} city of {country}")
                                except Exception as e:
                                        speak("Sorry Ayush, Due to network issue i am not able to find where we are")
                                        pass
                        elif 'hide my files' in self.query or 'hide this folder' in self.query or 'visible all them' in self.query:
                                speak("Ayush please tell me you want to hide tis folder or make it visible for everyone")
                                self.condition = self.takeCommand()
                                if 'hide' in self.condition:
                                        os.system("attrib +h /s /d")
                                        speak("Ayush, all the file in the folder are hidden now")
                                elif 'visible' in self.condition:
                                        os.system("attrib -h /s /d")
                                        speak("Ayush, all files are visible in this folder")
                                elif 'leave it' in self.condition:
                                        speak("Okay Ayush")
                                
                        elif 'send message to father' in self.query:
                                self.query = self.query.replace("send message to person", "")
                                self.query = self.query.replace("Veronica", "")
                                pywhatkit.sendwhatmsg("Enter the person number",f'{self.query}',16, 00 )
                                        
                        elif 'play song in youtube' in self.query:
                                pywhatkit.playonyt("Doctor strange believer")
                                
                        elif 'email to person' in self.query:
                                try:
                                        speak("Sir, What should I say")
                                        self.content = self.takeCommand()
                                        to = "person's email id"
                                        sendemail(to,self.content)
                                        speak("Email ha been send to been person")
                                except Exception as e:
                                        print(e)
                                        speak("Sorry Ayush I am not able to send email to person")
                        elif 'open camera' in self.query:
                                # import time
                                subprocess.run('start microsoft.windows.camera:', shell=True)
                                speak("Camera opened sucessfully")
                                speak("Wait 1 second")
                                time.sleep(1)
                                keyboard.press_and_release('space')
                                speak("image captured")
                                speak("wait for 0.5 second to turn video camera")
                                time.sleep(0.5)
                                keyboard.press_and_release('up arrow')
                                speak("camera turned to video capturing ")
                                keyboard.press_and_release('space')
                                time.sleep(10)
                                keyboard.press_and_release('space')
                                speak("Video capturing stopped now")
                                subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)
                                speak("Camera closed sucessfully")
                                        
                        elif 'tell me news' in self.query:
                                speak("Please wait Ayush, fetching the latest news")
                                news()
                        elif 'read my english book' in self.query:
                                readpdf2()
                        elif "temperature" in self.query:
                                search = "temprature in delhi"
                                url = f"https://www.google.com/search?q={search}"
                                r = requests.get(url)
                                data = BeautifulSoup(r.text,"html.parser")
                                temp = data.find("div",class_ = "BNeawe").text
                                speak(f"Current {search} is {temp}")
                        elif 'How much power left' in self.query or 'how much power we have' in self.query or 'battery' in self.query:
                                import psutil
                                battery = psutil.sensors_battery()
                                percentage = battery.percent
                                speak(f"Sir our system have {percentage} percent battery")
                                if percentage>=75:
                                        speak("Ayush we have enough battery to work")
                                elif percentage>=40 and percentage<=75:
                                        speak("Sir, we should connect our system to charging point to charge our battery")
                                elif percentage<=15 and percentage<=30:
                                        speak("Sir, we don't have enough power to work, please connect to charging")
                                elif percentage<=15:
                                        speak("Sir, we have very low power, please connect to charging the system will shutdown very soon")
                        elif 'internet speed' in self.query:
                                        
                                        st = speedtest.Speedtest()
                                        dl = st.download()
                                        up = st.upload()
                                        speak(f"Sir we have {dl} bit per second downloading speed and {up} bit per uploading speed ")
                        elif 'network speed' in self.query:
                                        
                                try:
                                        os.system('cmd /k "speedtest"')
                                except:
                                        speak("There is no Internet connection")
                        elif 'volume up' in self.query:
                                pyautogui.press("volumeup")
                        elif 'volume down' in self.query:
                                pyautogui.press("volumedown")
                        elif 'volume mute' in self.query or 'mute' in self.query:
                                pyautogui.press("volumemute")
                        elif 'instagram profile' in self.query or 'profile on instagram' in self.query:
                                # import time
                                speak("Sir please enter the user name correctly")
                                name = input("Enter Username here: ")
                                webbrowser.open("www.instagram.com/{name}")
                                speak("Sir here is the profile picture of this account")
                                time.sleep(5)
                                speak("Sir would you like to download profile picture of this account")
                                self.condition = self.takeCommand()
                                if 'yes' in self.condition:
                                        
                                        mod = instaloader.Instaloader()
                                        mod.download_profile(name, profile_pic_only=True)
                                        speak("I am done Ayush, profile picture is saved in our main folder. now i am ready for next command")
                                else:
                                        pass
                        elif 'hello veronica' in self.query:
                                speak("Hello Ayush")
                                speak("I am Veronica how may i help you")
                        elif 'play' in self.query:
                                song = self.query.replace('play', '')
                                speak('playing' + song)
                                pywhatkit.playonyt(song)
                        elif 'calculate' in self.query:
                                def WolfRamAlpha(query):
                                        apiKey = "VQRRYV-WJ8UL76UQL"
                                        requester = wolframalpha.Client(apiKey)
                                        requsted = requester.query(self.query)


                                        try:
                                                answer = next(requsted.results).text
                                                return answer
                                                
                                        except:
                                                speak("The value is not answerable")

                                def Calc(query):
                                        Term = str(query)
                                        Term = Term.replace("Veronica", "")
                                        Term = Term.replace("plus", "+")
                                        Term = Term.replace("multiply", "*")
                                        Term = Term.replace("minus", "-")
                                        Term = Term.replace("divide", "/")
                                        Term = Term.replace("percentage", "%")
                                query = query.replace("Calculate", "")
                                query = query.replace("Veronica", "")
                                Calc(query)
                                WolfRamAlpha(query)
                        elif 'turn on bluetooth' in self.query:
                                # import time
                                time.sleep(5)
                                print(pyautogui.position())
                                keyboard.press_and_release('windows+a')
                                time.sleep(2)
                                pyautogui.click(x=1679, y=513)
                        
                        elif 'youtube automation' in self.query:
                                speak("What your command")
                                self.comm = self.takeCommand()
                                if 'pause' in self.comm:
                                        keyboard.press('space bar')
                                elif 'restart' in self.comm:
                                        keyboard.press('0')
                                elif 'mute' in  self.comm:
                                        keyboard.press('m')
                                elif 'skip' in self.comm:
                                        keyboard.press('l')
                                elif 'back' in self.comm:
                                        keyboard.press('j')
                                elif 'full screen' in self.comm:
                                        keyboard.press('f')
                                elif 'film mode' in self.comm:
                                        keyboard.press('t')
                        
                        elif 'open new tab' in self.query:
                                keyboard.press_and_release('ctrl + t')
                        elif 'open new chrome' in self.query:
                                keyboard.press_and_release('ctrl + n') 
                        elif 'close tab' in self.query:
                                keyboard.press_and_release('ctrl + w')
                        elif 'history' in self.query:
                                keyboard.press_and_release('ctrl + h')
                        elif 'downloads' in self.query:
                                keyboard.press_and_release('ctrl + j')
                        elif 'left tab' in self.query:
                                keyboard.press_and_release('ctrl + 1')
                        elif 'next tab' in self.query:
                                keyboard.press_and_release('ctrl + 9')
                        elif 'repeat my words' in self.query:
                                speak("Speak Sir! ")
                                self.jj = self.takeCommand()
                                speak(f"You said: {self.jj}")
                        elif 'download video' in self.query:
                                link = "https://youtu.be/Z-bYToD629Y"
                                video = YouTube(link)
                                print("\n")
                                speak("Title: " + video.title)
                                speak("Thumbnail Image: " + video.thumbnail_url)
                                print("\n")
                                strams = video.streams.get_by_itag(22)
                                strams.download()
                                speak("Success")
                        
                                
                        elif 'track number' in self.query:
                                number = input("Enter the Number with +__: ")
                                phone=phonenumbers.parse(number)
                                timee=timezone.time_zones_for_number(phone)
                                car=carrier.name_for_number(phone,"en")
                                reg=geocoder.description_for_number(phone,"en")
                                speak(phone)
                                speak(timee)
                                speak(car)
                                speak(reg)
                        elif 'Youtube search' in self.query:
                                speak("Okay Ayush")
                                self.query = self.query.replace("Youtube", "")
                                self.query = self.query.replace("search", "")
                                self.query = self.query.replace("Veronica", "")
                                self.query = self.query.replace("youtube search", "")
                                web = 'https://www.youtube.com/watch?v=' + self.query
                                webbrowser.open(web)
                                speak("Done Ayush")
                        elif 'music' in self.query or 'video' in self.query:
                                speak("Tell me the name of song or video")
                                self.musicname = self.takeCommand()
                                pywhatkit.playonyt(self.musicname)
                        elif 'you need a break' in self.query or 'sleep' in self.query or 'quit' in self.query or 'exit' in self.query:
                                speak("Ok, Sir you can call me any time")
                                speak("Just say Wake up to run me")
                                break
                        elif 'pacman doodle' in self.query:
                                speak("Opening pac man doodle")
                                webbrowser.open("https://www.google.com/search?q=pacman+30th+anniversary&ct=pacman10-hp&oi=ddle") 
                        elif 'open calculator' in self.query:
                                speak("calculator mod is activated")
                                r = sr.Recognizer()
                                with sr.Microphone() as source:
                                        speak("Say what you want to calculate for example 3 plus 3")
                                        print("Listening...")
                                        audio = r.listen(source)
                                        my_string=r.recognize_google(audio)
                                        print(my_string)
                                        def getoperator(op):
                                                return{
                                                        '+': operator.add,
                                                        '-': operator.sub,
                                                        'X': operator.mul,
                                                        'divided':operator.__truediv__,
                                                }[op]
                                        def eval_binary_expr(op1,oper,op2):
                                                op1,op2=int(op1), int(op2)
                                                return getoperator(oper)(op1,op2)
                                        speak("Your result is")
                                        speak(eval_binary_expr(*(my_string.split())))
                        elif 'mean by' in self.query:
                                Meaning()
                                
                        elif 'snake game' in self.query:
                                speak("opening snake xenzia")
                                webbrowser.open("https://www.google.com/search?q=play%20snake&si=AC1wQDATZLWKCycW7QmrPUq4vpHcQ90G7N-gqkh6AR-Z77b7mG5QTbW8-jINz53OaxGvSg_rr6jQ&biw=1280&bih=609&dpr=1.5")
                                # elif 'change password' in self.query:
                                #         speak("What's the new password")
                                #         new_pw = input("Enter the new password\n")
                                #         new_password = open("pass.txt", "w")
                                #         new_password.write(new_pw)
                                #         new_password.close()
                                #         speak("Done Ayush")
                                #         speak(f"Your new password is{new_pw}")
                        elif 'weather' in self.query:
                                weather()
                        elif 'qr code' in self.query:
                                img = qr.make("Enter The Path wich you want to make it")
                                img.save("Nacho nacho fro RRR movie.png")
                        elif 'thank you' in self.query:
                                speak("Welcome Ayush its my work")
                        elif 'something for me' in self.query:
                                pywhatkit.playonyt("Doctor Strange Believer")
                        elif 'something your choice' in self.query:
                                speak("playing for my choice")
                                pywhatkit.playonyt("Nacho Nacho Song RRR")
                        elif 'tic tac' in self.query:
                                webbrowser.open("https://www.google.com/search?q=tic+tac+toe&oq=tic+tac+&aqs=chrome.0.0i433i512j69i57j0i512l7j0i131i433i512.8452j0j15&sourceid=chrome&ie=UTF-8")
                        elif 'close' in self.query:
                                self.query = self.query.replace("close", "")
                                close(self.query)
                                
                                
                        elif 'start digital clock' in self.query:
                                speak("Opening Digital Clock")
                                os.startfile("C:\\Users\\Asing\\Desktop\\Graphical Animation\\dt.py")
                        elif 'type' in self.query:
                                self.query = self.query.replace("type", "")
                                self.query = self.query.replace("Veronica", "")
                                pyautogui.typewrite(f"{self.query}")

                        elif 'send message' in self.query:
                                speak("Sir what should i say?")
                                msz= self.takeCommand()
                                from twilio.rest import Client
                                account_sid = "AC9b2d6a687b06fdc0cad9a673a866s3ce"
                                auth_token = "71bd663c53e678f48df48a1fea740b02"
                                client = Client(account_sid, auth_token)
                                message = client.messages \
                                        .create(
                                                body=msz,
                                                from_='+14145017135',
                                                to=''
                                        )
                                print(message.sid)
                        elif 'alarm' in self.query:
                                speak("Sir please tell me the time to set alarm. for example, set alarm 5:30 am")
                                self.tt= self.takeCommand()
                                self.tt = self.tt.replace("set alarm ", "")
                                self.tt = self.tt.replace(".", "")
                                self.tt  = self.tt.upper()
                                import MyAlarm
                                MyAlarm.alarm(self.tt)

                                
                
                        
                                
                                           
                                
                        

startexecution = MainThread()

class Main(QMainWindow):
        def __init__(self):
                super().__init__()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)
                self.ui.pushButton.clicked.connect(self.startask)
                self.ui.pushButton_2.clicked.connect(self.close)
        def startask(self):
                self.ui.movie = QtGui.QMovie("QT.gif")
                self.ui.label.setMovie(self.ui.movie)
                self.ui.movie.start()
                self.ui.movie = QtGui.QMovie("Jarvis_Loading_Screen.gif")
                self.ui.label_2.setMovie(self.ui.movie)
                self.ui.movie.start()
                Timer = QTimer(self)
                Timer.timeout.connect(self.showtime)
                Timer.start(1000)
                startexecution.start()
        
        def showtime(self):
                time = QTime.currentTime()
                now = QDate.currentDate()
                label_time = time.toString('hh:mm:ss')
                label_date = now.toString(Qt.ISODate)
                self.ui.textBrowser.setText(label_date)
                self.ui.textBrowser_2.setText(label_time)
        def exit(self):
                pass
app = QApplication(sys.argv)
Veronica = Main()
Veronica.show()
exit(app.exec_())

             