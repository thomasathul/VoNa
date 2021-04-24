from gtts import gTTS
import speech_recognition as sr
import pyttsx3
import os 
from playsound import playsound
from google_trans_new import google_translator


#to translate into different languages
translator = google_translator()



#function to employ voice commands
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

#Assistant introduction
SpeakText("Welcome Sir! Which document do you want me to read?")

#Path where your text file is located. (Update it to your path)
path = "C:\\Users\\Dell\\Documents\\VoNa\\"

#Listening and recognizing the text filename.
r = sr.Recognizer()
while(1):
  with sr.Microphone() as source3:
    r.adjust_for_ambient_noise(source3,duration=0.000001)
    audio3 = r.listen(source3)
    try:
      filename = r.recognize_google(audio3)
      filename = filename.lower()
      mytext = open(os.path.join(path, filename+".txt"), "r")
      SpeakText("Found filename "+filename+".txt")
      break

    #If file not found, asking for a different file name
    except FileNotFoundError:
      SpeakText("Can't find the file "+filename +".txt, Please say a different textfile name")
      continue
      #filename = input()
      #filename = filename.lower()
      #mytext = open(os.path.join(path, filename+".txt"), "r")
      #break
      
    #If assistant didn't listen, asking to repeat
    except sr.UnknownValueError:
      SpeakText("Sorry, Cant understand, Please say again")
      continue

#Reading the text file    
readtext=mytext.read()

#Asking which language to be read
SpeakText("Which language do you want?")
while(1):
  with sr.Microphone() as source2:
    r.adjust_for_ambient_noise(source2, duration=0.000001)
    audio2 = r.listen(source2)
    try:
      name = r.recognize_google(audio2)
    except sr.UnknownValueError:
      SpeakText("Sorry, Cant understand, Please say again")
      continue 
     
    name = name.lower()
    if "english" in name:
      SpeakText("Okay,Reading in English")
      language = 'en-us'
      break
    elif "french" in name:
      SpeakText("Okay,Reading in French")
      readtext = translator.translate(readtext, lang_src='en', lang_tgt='fr')
      language='fr'
      break
    elif "dutch" in name:
      SpeakText("Okay,Reading in Dutch")
      readtext = translator.translate(readtext, lang_src='en', lang_tgt='nl')
      language = 'nl'
      break
    elif "russian" in name:
      SpeakText("Okay,Reading in Russian")
      readtext = translator.translate(readtext, lang_src='en', lang_tgt='ru')
      language = 'ru'
      break
    elif "tamil" in name:
      SpeakText("Okay,Reading in Tamil")
      readtext = translator.translate(readtext, lang_src='en', lang_tgt='ta')
      language = 'ta'
      break
    elif "spanish" in name:
      SpeakText("Okay,Reading in Spanish")
      readtext = translator.translate(readtext, lang_src='en', lang_tgt='es')
      language='es'
      break
    elif "malayalam" in name:
      SpeakText("Okay,Reading in Malayalam")
      readtext = translator.translate(readtext, lang_src='en', lang_tgt='ml')
      language = 'ml'
      break
    elif "arabic" in name:
      SpeakText("Okay,Reading in Arabic")
      readtext = translator.translate(readtext, lang_src='en', lang_tgt='ar')
      language='ar'
      break
    elif "german" in name:
      SpeakText("Okay,Reading in German")
      readtext = translator.translate(readtext, lang_src='en', lang_tgt='de')
      language = 'de'
      break
    elif "hindi" in name:
      SpeakText("Okay,Reading in Hindi")
      readtext = translator.translate(readtext, lang_src='en', lang_tgt='hi')
      language = 'hi'
      break
    elif "chinese" in name:
      SpeakText("Okay,Reading in Chinese")
      readtext = translator.translate(readtext, lang_src='en', lang_tgt='zh-cn')
      language = 'zh-cn'
      break
    elif "italian" in name:
      SpeakText("Okay,Reading in Italian")
      readtext = translator.translate(readtext, lang_src='en', lang_tgt='it')
      language = 'it'
      break
    elif "japanese" in name:
      SpeakText("Okay,Reading in Japanese")
      readtext = translator.translate(readtext, lang_src='en', lang_tgt='ja')
      language = 'ja'
      break
    else:
      SpeakText("Language not found. Please ask for another language")
      continue

#Getting the translation, language, converting into audiofile and playing it
readobj = gTTS(text=readtext, lang=language, slow=False)
readobj.save("speak.mp3")
playsound("C:\\Users\\Dell\\Documents\\VoNa\\speak.mp3")




