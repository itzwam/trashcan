# coding: utf-8
import socket

import sys

def Main(): 
    host = '127.0.0.1'  
    port = 5555
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # déclare un socket
  

    alphabet = 'abcdefghijklmnopqrstuvwxyz' # alphabet, utilisé pour les réponses
    try: 
        s.connect((host,port)) # connexion au serveur
        print("Successfully connected to the server")

        nb_quest = input('How many questions do you want ? ') # demande combien de questions poser

        s.sendall(nb_quest.encode()) # envoi le nombre au serveur
        nb_quest = int(nb_quest)
        while nb_quest > 0:
    
            data = s.recv(1024) # reçoit la question / possibilités depuis le serveur
            infos = data.split(b'\0') 
            question = infos[0].decode() # question = 'blablabla'
            choices = [x.decode() for x in infos[1].split(b'|')] # choices = ['truc', 'bidule', 'chose']
    
            print(question)
            for i, choice in enumerate(choices):
                print(alphabet[i] + ") " + choice) # Affiche la possibilité, à coté d'une lettre

            ans = input('?> ') # demande la réponse
            s.sendall(b'%d' % alphabet.index(ans)) # transforme la lettre en nombre (et l'envoi au serveur)

            data = s.recv(1024) # attend la réponse du serveur
            if data.decode() == "OK": # Bonne réponse
                print("Right answer !")
            else: # Mauvaise réponse
                print("Bruh")
            nb_quest -= 1
        data = s.recv(1024) # Attend le score depuis le serveur
        if data:
            print("Your score : {}".format(data.splitlines()[0].decode())) # affiche le score si il est reçu depuis le serveur
        s.close()  # Ferme le socket
    except ConnectionResetError:
        s.close() # Si le socket se ferme, on quitte
        return


if __name__ == '__main__': 
    Main() 
