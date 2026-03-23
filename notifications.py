# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:57:35 2026

@author: arnau

Gestion des notifications
"""

class Email_Notification:
    def __init__(self, email):
        self.email = email
        
    def send (self,message) :
        print(f"Envoi email à {self.email} : {message}")

class Discord_Notification:
    def __init__(self, pseudo):
        self.pseudo = pseudo
    
    def send (self,message) :
        print(f"Envoi message discord à {self.pseudo} : {message}")
        
class Log_Notification:
    def __init__ (self, nom_fichier='alerte.log'):
        self.nom_fichier = nom_fichier
    def send (self, message):
        print(f"LOG : Enreigistrement du message de détection dans {self.nom_fichier} : {message}")
        
