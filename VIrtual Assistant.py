from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
import random

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[1].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


# pyttsx3
#bot = ChatBot("My Bot")

#convo = ['switch on dining room light','dining room fan','hall fan','hall light']

#trainer = ListTrainer(bot)

# now training the bot with the help of trainer

#trainer.train(convo)

# answer = bot.get_response("what is your name?")
# print(answer)

# print("Talk to bot ")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ", answer)

main = Tk()

main.geometry("500x650")

main.title("My Chat bot")
img = PhotoImage(file="bot1.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)


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


def ask_from_bot():
    answers=['Yes i have turned on the light','okk i\'ll do it for u']
    positive_answers=[]
    negative_answers=[]
    query = textF.get().split()
    if 'dining' in query and 'on' in query:
        if ('can' in query or 'what' in query or "what's" in query): 
            answer_from_bot=random.choice(answers)
        dining=103
    elif 'dining' in query and 'off' in query:
        answer_from_bot=random.choice(answers)
        dining=108
    elif ('bedroom' in query or 'room' in query) and 'on' in query:
        answer_from_bot=random.choice(answers)
        dining=102
    elif ('bedroom' in query or 'room'in query) and 'off' in query:
        answer_from_bot=random.choice(answers)
        dining=107
    elif ('livingroom' in query or 'living room' in query  or 'hall' in query):
        q_wordList = ['know','say','tell','inform','status']
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
                    
                    
                


        
        answer_from_bot=random.choice(answers)
        dining=101
#    elif ('livingroom' in query or 'living room' in query or 'hall'in query) and 'off' in query:
#        answer_from_bot=random.choice(answers)
#         dining=106
    elif ('fan' in query or 'Fan' in query) and 'on' in query :
        answer_from_bot=random.choice(answers)
        dining=104
    elif ('fan' in query or 'Fan' in query ) and 'off' in query :
        answer_from_bot=random.choice(answers)
        dining=109
    elif ('fan' in query or 'Fan' in query )and 'off' in query :
        answer_from_bot=random.choice(answers)
        dining=109
    
    
    
       
  #  answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)
   # msgs1.yview(END)


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


# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)

t.start()

main.mainloop()
