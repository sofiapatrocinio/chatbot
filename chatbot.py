#-*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Teste')

trainer = ListTrainer(bot)

for arq in os.listdir('arq'):
    chats = open('arq/' + arq, 'r').readlines()
    trainer.train(chats)

while True:
    resq = input('Você: ')

    resp = bot.get_response(resq)
    print ('Bot: ' + str(resp))