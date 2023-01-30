import os
import pyttsx3
pyttsx3.speak("Do you want to see menu...yes or no")
A = input("Do you want to see menu?...y/n  ")
while A == 'n':
    print('Ok Bye!!!!   ')
    break
while A == 'y':
    pyttsx3.speak("welcome to dial menu")
    print("welcome to dial menu")
    print("press 1: To open winword")
    print("press 2: To open chrome")
    print("press 3: To open firefox")
    print("press 4: To open notepad")
    print("press 5: To open mspaint")
    print("press 6: To open Gmail")
    print("press 7: To open whatsapp")
    print("press 8: To open Facebook")
    print("press 9: To open Calculator")
    print("press 10: To open file explorer")
    print("press 11: To open powerpoint")
    print("press 12: To open command prompt")
    print("press 13: To open microsoft edge")
    print("press 14: To open camera")
    print("press 15: To open Bluetooth")
    print("press 16: To shut down PC")
    print("press 17: To restart PC")
    print("press 18: To open vlc media player")
    print("press 19: To open adobe reader")
    print("press 20: To open windows media player")
    print("press 21: To exit the program")
    while True:
        x = int(input("Press any key.....    "))
        if x == 1:
            pyttsx3.speak("opening microsoft word")
            os.system("start winword")
        elif x == 2:
            pyttsx3.speak("opening google chrome")
            os.system("start chrome")
        elif x == 3:
            pyttsx3.speak("opening mozilla firefox")
            os.system("start firefox")
        elif x == 4:
            pyttsx3.speak("opening notepad")
            os.system("start notepad")
        elif x == 5:
            pyttsx3.speak("opening paint")
            os.system("start mspaint")
        elif x == 6:
            pyttsx3.speak("opening Gmail")
            os.system("start chrome gmail.com")
        elif x == 7:
            pyttsx3.speak("opening whatsapp")
            os.system("start chrome web.whatsapp.com")
        elif x == 8:
            pyttsx3.speak("opening facebook")
            os.system("start chrome facebook.com")
        elif x == 9:
            pyttsx3.speak("opening calculater")
            os.system("start calc")
        elif x == 10:
            pyttsx3.speak("file explorer")
            os.system("start explorer")
        elif x == 11:
            pyttsx3.speak("opening powerpoint")
            os.system("start powerpnt")
        elif x == 12:
            pyttsx3.speak("opening command prompt")
            os.system("start cmd")
        elif x == 13:
            pyttsx3.speak("opening microsoft edge")
            os.system("start microsoft-edge:")
        elif x == 14:
            pyttsx3.speak("opening camera")
            os.system("start microsoft.windows.camera:")
        elif x == 15:
            pyttsx3.speak("opening bluetooth")
            os.system("start fsquirt")
        elif x == 16:
            pyttsx3.speak("pc shutdown")
            os.system("shoutdown/s")
        elif x == 17:
            pyttsx3.speak("pc restart")
            os.system("shoutdown/r")
        elif x == 18:
            pyttsx3.speak("opening vlc media player")
            os.system("start vlc")
        elif x == 19:
            pyttsx3.speak("opening adobe reader")
            os.system("start acrord32")
	elif x==20:
	    pyttsx3.speak("opening windows media player")
	    os.system("start wmplayer")
        elif x==21:
            break
        else:
            pyttsx3.speak("You have not choose anything from given Menu....Please try again")
            print("You have not choose anything from given Menu...."'\n''Please try again')
else:
    pyttsx3.speak("you have entered wrong input")
    print("wrong input")