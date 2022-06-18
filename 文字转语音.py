# 文字转语音
# pip install pyttsx3
import pyttsx3 as s
item2 = input(">>>")
item = s.init()
item.say(item2)
item.runAndWait()