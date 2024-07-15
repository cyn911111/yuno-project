#語音轉文字
import speech_recognition as sr

# 建立Recognizer物件
r = sr.Recognizer()

# 開啟麥克風並進行錄音
with sr.Microphone() as source:
    print("請開始說話...")
    audio = r.listen(source)

# 使用Google語音辨識引擎將錄音轉換為文字
try:
    text = r.recognize_google(audio, language='zh-TW')
    
    print("您說的是：" + text)
except sr.UnknownValueError:
    print("無法辨識您的語音")
except sr.RequestError as e:
    print("無法連線至Google語音辨識服務：{0}".format(e))

    #串接GEMINI    
import google.generativeai as genai
import os

api_key = 'AIzaSyBCcg0skdWwwG-hBucIvDCLHY9FFtzw9-0'
genai.configure(api_key = api_key)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(text)

print(response.text)

#文字轉語音  
# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os 
  
mytext = response.text
  
# Language we want to use 
language = 'zh-tw'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("output.mp3") 
  
# Play the converted file 
os.system("start output.mp3")