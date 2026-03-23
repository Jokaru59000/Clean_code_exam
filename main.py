# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:21:09 2026

@author: arnau

Examen Clean Code

Arnaud Madou 5 INFO

Consigne : 
            Votre rôle est de concevoir un mini-système de surveillance pour un bâtiment. 
            Plusieurs types de capteurs provenant de deux marques différentes doivent pouvoir 
            fonctionner ensemble, générer des alertes, et notifier des observateurs. 
            Vous devez suivre les signatures indiquées ci-dessous. La logique interne et les interactions 
            sont à concevoir par vous. 
"""

from capteurs import CameraA, TemperatureSensorA, ThermalSensorB, ThermalSensorB_Adapter
from notifications import Email_Notification, Log_Notification, Discord_Notification
from pieces import Piece


def main():
    desk = Piece("Bureau")
    #cantine = Piece("Cafétéria")
    
    desk.add_notif(Email_Notification('arnaud@gmail.com'))
    desk.add_notif(Log_Notification())
    desk.add_notif(Discord_Notification('nono_du_59'))
    
    #cantine.add_notif(Log_Notification())
    #cantine.add_notif(Email_Notification('arnaud@gmail.com'))
    
    
    desk_camera = CameraA("Camera_bureau")
    desk.add_sensor(desk_camera)
    
    #cantine_thermalsensor = ThermalSensorB_Adapter("Capteur_thermique_cafet")
    #cantine.add_sensor(cantine_thermalsensor)
    
    desk_camera.callback("Mouvement detecté")
    #cantine_thermalsensor.sensor_b.trigger_heat_signature(lambda date: None)
    
if __name__ == "__main__":
    main()
