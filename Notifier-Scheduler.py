import pyttsx3 #pip install pyttsx3==2.6
import datetime
import time
from win10toast import ToastNotifier#pip install win10toast
toaster = ToastNotifier()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def nowtime():
    strTime = datetime.datetime.now().strftime("%H") 
    return strTime
nowtime=nowtime()
#print(nowtime)


query = {
    "Good Morning,wake Up":6,
    "Brush":6 ,
    "Take bath":7,
    "Have your breakfast ":8,
    "Be Ready for your online classes":9,
    "You can join your Classes":10,
    "Have your lunch":13,
    "Take Rest":13,
    "Play Outdoor Games":16,
    "Do your Study":18,
    "Have Your Dinner":21,
    "Take a review for Next day classes":22,
    "Go to Bed,Good Night":23
}

#print(tuple(query.items())[i]][0])

while True:
    for i in range(0,len(query)):
        task=tuple(query.items())[i][0]
        y=int(query.get(task))
        #print(task)
        #print(y)

        
        if y==int(nowtime):
            speak("Hello There,It is,"+str(nowtime)+",now"+str(task))
            toaster.show_toast(str(task),"It is "+str(nowtime),duration=10) 

    time.sleep(3600)