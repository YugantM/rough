from difflib import SequenceMatcher
import os

def main(text):
    no1 = "play music"
    no2 = "open image"
    no3 = "open photo"
    if(SequenceMatcher(None,text,no1).ratio()>0.6):
        os.startfile("E:\Dog-barking-aggressive.mp3")
        return "playing..."

    elif(SequenceMatcher(None,text,no2).ratio()>0.6):
        os.startfile("E:\yugant.jpg")
        return "opening image"

    elif (SequenceMatcher(None, text,no3).ratio() > 0.6):
        os.startfile("E:\yugant.jpg")
        return "opening photo"

    else:
        return "no such command available right now, please try music or images"




