# coding: utf-8
# import socket programming library 

import socket 

import random

import sys

import codecs
  
# import thread module 
from threading import Thread  

# thread fuction 
def threaded(c, q):
    player_score = 0
    questions = q.copy()
    try:
        data = c.recv(1024) # reçoit le nombre de questions a poser
        if not data: 
            c.close() # Si pas de réponse, on ferme
            return
        nb_quest=int(data) 
        for _i in range(nb_quest):
            question = random.choice(questions) # on choisit une question au hasard
            ask = question[0] # question
            choices = question[1:4] # possibilitées de réponse
            answer = question[4] # bonne réponse
            questions.remove(question) # enlève la question de la liste
            c.sendall((ask + "\0" + "|".join(choices)).encode('utf8')) # envoi au client la question et les possibilités de réponse 
            data = c.recv(1024) # attend la proposition du client
            if not data: 
                c.sendall(b'KO') # Si pas de réponse -> mauvaise réponse
                break
            user_input=int(data)
            if choices[user_input] != answer: 
                c.sendall(b'KO') # Mauvaise réponse
                player_score -= 1 
            else:
                c.sendall(b'OK') # Bonne réponse
                player_score += 2 
        c.sendall(b'%d' % player_score) # Envoi le score au client
    except ConnectionResetError:
        c.close() # Si le socket coupe, on quitte 
        return
    c.close() # si tout est fini, on ferme le socket
  
def Main():
    host = "127.0.0.1" 
    port = 5555
    doStop = False
    threads = []
    questions = []
    with codecs.open('quiz.txt', 'r', encoding='latin-1', errors='replace') as fdata:
        data = fdata.read().splitlines()
    questions = [question.split(';') for question in data]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    s.listen(1)
    print("Listening on", host, port) 

    try:
        # a forever loop until client wants to exit 
        while not doStop: 
            # establish connection with client 
            c, addr = s.accept()

            print('Connection from :', addr[0], ':', addr[1]) 
            t = Thread(target=threaded, args=(c, questions , )) # déclare un thread pour répondre au client
            t.start() # lance ce thread
            threads.append(t) # ajoute ce thread a une liste
        s.close()
    except KeyboardInterrupt:
        print("End request received")
        doStop = True
        print("Waiting for all connections to end")
        for t in threads:  
            t.join() # attend que tous les threads de la liste se ferment
    s.close()

    
  
if __name__ == '__main__': 
    Main() 