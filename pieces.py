 # -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:12:58 2026

@author: arnau

Gestion des différentes pièces du bâtiment
"""

class Piece:
    def __init__ (self,nom) : 
        self.nom = nom
        self.sensor = []
        self.notifications = []

# On ajoute le système de notifications à la pièce  

    def add_notif(self, notifications):
        self.notifications.append(notifications)
        
# On ajoute un ou plsrs capteurs par pièce
    
    def add_sensor(self, sensor):
        self.sensor.append(sensor)
        sensor.on_detect(self.notify_everyone)
        
# On ajoute un systeme pour envoyer un message à tout le monde

    def notify_everyone(self, message):
        full_message = f"Alerte dans {self.nom} : {message}"
        for n in self.notifications:
            n.send(full_message)

