from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import nltk
import csv
import os
import command

import pickle

with open('chat.csv','r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

jarvis = ChatBot("JARVIS")

jarvis.set_trainer(ListTrainer)

#y = jarvis.train(your_list)
#pickle.dump(y, open( "jarvis_bot.p", "wb" ) )

que = "who are you"
response = jarvis.get_response(que)

#print(response)

#print(response.text.find('command'))

if(response.text.find('command')>0):
    print(command.main(que))
else:
    print(response)
