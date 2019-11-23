from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
import random

def send_data_thingspeak(code):
    fieldid='2'
    writekey='TRV2A3148OPDX7D8'
    code=str(code)
    baseURL = 'http://api.thingspeak.com/update?api_key='+writekey+'&field'+fieldid+'='
    f = urlopen(baseURL+code)	
    print("Sending",code,"to thingspeak")
    f.read()
    f.close()

def read_data_thingspeak(field):
    channelid='918879'
    fieldid=str(field)
    URL='https://api.thingspeak.com/channels/'+channelid+'/fields/'+fieldid+'.json?api_key='
    readkey='Z5PEGCWA99S6A146' #'CU4W1P240P0XK0QP'
    HEADER='&results=1'
    NEW_URL=URL+readkey+HEADER
    print("Contacting URL : ",NEW_URL)
    get_data=get(NEW_URL).json()
    # print(get_data)
    # channel_id=get_data['channel']['id']
    fields=get_data['feeds']
    # print(fields)
    # t=[]
    for x in fields:
        return int(x['field'+fieldid])
# sleep(5)

def speak(word):
    engine.say(word)
    engine.runAndWait()

# takey query : it takes audio as input from user and convert it to string..

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")

# creating a function
def enter_function(event):
    btn.invoke()

def repeatL():
    while True:
        takeQuery()

def ask_from_bot():
    answers=['Yes i have turned on the light','okk i\'ll do it for u']
    errors=["Sorry, I didn't get your request."]
    q_wordList = ['know','say','tell','inform','status']
    positive_answers=[]
    negative_answers=[]
    query = textF.get().split()
    if 'livingroom' in query or ('living' in query and 'room' in query) or 'hall' in query:
        if any(word in query for word in q_wordList):
            if 'light' in query or 'lights' in query:
                if 'on' in query:
                    #read status and give message
                    int stat = read_data_thingspeak(1)
                    if stat==1:
                        answer_from_bot='Yes, the living room light is on.'
                    else:
                        answer_from_bot='No, the living room light is off.'
                elif 'off' in query or 'out' in query:
                    #read status and give message
                    int stat = read_data_thingspeak(1)
                    if stat==1:
                        answer_from_bot='No, the living room light is on.'
                    else:
                        answer_from_bot='Yes, the living room light is off.'
                else:
                    #error message
                    answer_from_bot=random.choice(errors)
            elif 'fan' in query:
                if 'on' in query:
                    #read status and give message
                    int stat = read_data_thingspeak(4)
                    if stat==1:
                        answer_from_bot='Yes, the living room fan is on.'
                    else:
                        answer_from_bot='No, the living room fan is off.'
                elif 'off' in query:
                    #read status and give message
                    int stat = read_data_thingspeak(4)
                    if stat==1:
                        answer_from_bot='No, the living room fan is on.'
                    else:
                        answer_from_bot='Yes, the living room fan is off.'
                else:
                    #error message
                    answer_from_bot=random.choice(errors)
        elif 'light' in query or 'lights' in query:
            if 'is' in query or 'are' in query:
                if (query.index('is')<query.index('light') and query.index('is')<query.index('on')) or (query.index('are')<query.index('lights') and query.index('are')<query.index('on')):
                    #read status and give message
                    int stat = read_data_thingspeak(1)
                    if stat==1:
                        answer_from_bot='Yes, the living room light is on.'
                    else:
                        answer_from_bot='No, the living room light is off.'
                elif (query.index('is')<query.index('light') and query.index('is')<query.index('off')) or (query.index('are')<query.index('lights') and query.index('are')<query.index('off')):
                    #read status and give message
                    int stat = read_data_thingspeak(1)
                    if stat==1:
                        answer_from_bot='No, the living room light is on.'
                    else:
                        answer_from_bot='Yes, the living room light is off.'
                elif (query.index('is')<query.index('light') and query.index('is')<query.index('out')) or (query.index('are')<query.index('lights') and query.index('are')<query.index('out')):
                    #read status and give message
                    int stat = read_data_thingspeak(1)
                    if stat==1:
                        answer_from_bot='No, the living room light is on.'
                    else:
                        answer_from_bot='Yes, the living room light is off.'
                else:
                    #error message
                    answer_from_bot=random.choice(errors)
            elif 'on' in query:
                #send code and give message
                send_data_thingspeak(101)
                #handle error in sending to cloud
                answer_from_bot=random.choice(answers)
            elif 'off' in query or 'out' in query:
                #send code and give message
                send_data_thingspeak(106)
                #handle error in sending to cloud
                answer_from_bot=random.choice(answers)
            else:
                #error message
                answer_from_bot=random.choice(errors)
        elif 'fan' in query:
            if 'is' in query or 'are' in query:
                if query.index('is')<query.index('fan') and query.index('is')<query.index('on'):
                    #read status and give message
                    int stat = read_data_thingspeak(4)
                    if stat==1:
                        answer_from_bot='Yes, the living room fan is on.'
                    else:
                        answer_from_bot='No, the living room fan is off.'
                elif query.index('is')<query.index('fan') and query.index('is')<query.index('off'):
                    #read status and give message
                    int stat = read_data_thingspeak(4)
                    if stat==1:
                        answer_from_bot='No, the living room fan is on.'
                    else:
                        answer_from_bot='Yes, the living room fan is off.'
                else:
                    #error message
                    answer_from_bot=random.choice(errors)
            elif 'on' in query:
                #send code and give message
                send_data_thingspeak(104)
                #handle error in sending to cloud
                answer_from_bot=random.choice(answers)
            elif 'off' in query:
                #send code and give message
                send_data_thingspeak(109)
                #handle error in sending to cloud
                answer_from_bot=random.choice(answers)
            else:
                #error message
                answer_from_bot=random.choice(errors)
        else:
            #error message
            answer_from_bot=random.choice(errors)
        
    elif 'diningroom' in query or ('dining' in query and ('room' in query or 'hall' in query)) or 'kitchen' in query:
        if any(word in query for word in q_wordList):
            if 'light' in query or 'lights' in query:
                if 'on' in query:
                    #read status and give message
                elif 'off' in query or 'out' in query:
                    #read status and give message
                else:
                    #error message
            elif 'fan' in query:
                if 'on' in query:
                    #read status and give message
                elif 'off' in query:
                    #read status and give message
                else:
                    #error message
        elif 'light' in query or 'lights' in query:
            if 'is' in query or 'are' in query:
                if (query.index('is')<query.index('light') and query.index('is')<query.index('on')) or (query.index('are')<query.index('lights') and query.index('are')<query.index('on')):
                    #read status and give message
                elif (query.index('is')<query.index('light') and query.index('is')<query.index('off')) or (query.index('are')<query.index('lights') and query.index('are')<query.index('off')):
                    #read status and give message
                elif (query.index('is')<query.index('light') and query.index('is')<query.index('out')) or (query.index('are')<query.index('lights') and query.index('are')<query.index('out')):
                    #read status and give message
                else:
                    #error message
            elif 'on' in query:
                #send code and give message
            elif 'off' in query or 'out' in query:
                #send code and give message
            else:
                #error message
        elif 'fan' in query:
            if 'is' in query or 'are' in query:
                if query.index('is')<query.index('fan') and query.index('is')<query.index('on'):
                    #read status and give message
                elif query.index('is')<query.index('fan') and query.index('is')<query.index('off'):
                    #read status and give message
                else:
                    #error message
            elif 'on' in query:
                #send code and give message
            elif 'off' in query:
                #send code and give message
            else:
                #error message
        else:
            #error message
            
    elif 'bedroom' in query or 'room' in query:
        if any(word in query for word in q_wordList):
            if 'light' in query or 'lights' in query:
                if 'on' in query:
                    #read status and give message
                elif 'off' in query or 'out' in query:
                    #read status and give message
                else:
                    #error message
            elif 'fan' in query:
                if 'on' in query:
                    #read status and give message
                elif 'off' in query:
                    #read status and give message
                else:
                    #error message
        elif 'light' in query or 'lights' in query:
            if 'is' in query or 'are' in query:
                if (query.index('is')<query.index('light') and query.index('is')<query.index('on')) or (query.index('are')<query.index('lights') and query.index('are')<query.index('on')):
                    #read status and give message
                elif (query.index('is')<query.index('light') and query.index('is')<query.index('off')) or (query.index('are')<query.index('lights') and query.index('are')<query.index('off')):
                    #read status and give message
                elif (query.index('is')<query.index('light') and query.index('is')<query.index('out')) or (query.index('are')<query.index('lights') and query.index('are')<query.index('out')):
                    #read status and give message
                else:
                    #error message
            elif 'on' in query:
                #send code and give message
            elif 'off' in query or 'out' in query:
                #send code and give message
            else:
                #error message
        elif 'fan' in query:
            if 'is' in query or 'are' in query:
                if query.index('is')<query.index('fan') and query.index('is')<query.index('on'):
                    #read status and give message
                elif query.index('is')<query.index('fan') and query.index('is')<query.index('off'):
                    #read status and give message
                else:
                    #error message
            elif 'on' in query:
                #send code and give message
            elif 'off' in query:
                #send code and give message
            else:
                #error message
        else:
            #error message
       
    msgs.insert(END, "you : " + ' '.join(query))
    #print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)

engine = pp.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id) 
main = Tk()
main.geometry("500x650")
main.title("My Chat bot")
img = PhotoImage(file="bot1.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)

frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
#msgs1 = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
#msgs1.pack(side=RIGHT, fill=BOTH, pady=10)
frame.pack()
# creating text field
textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)
btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()

# going to bind main window with enter key...
main.bind('<Return>', enter_function)
t = threading.Thread(target=repeatL)
t.start()
main.mainloop()
