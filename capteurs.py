# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:24:37 2026

@author: arnau

Classes Capteurs
"""

import datetime

class CameraA : 
    def __init__ (self, location):
        self.location = location
        
    def on_detect(self, callback):
        self.callback = callback
        print(f"Camera active dans : {self.location}")

class TemperatureSensorA:
    def __init__ (self, location, threshold):
        self.location = location
        self.threshold = threshold
    
    def on_detect(self, callback):
        self.callback = callback
        print(f"Seuil : {self.threshold} dans : {self.location}")

class ThermalSensorB : 
    def __init__ (self, position) : 
        self.position = position
    
    def trigger_heat_signature(self, process):
        data = { 
            "sensor":self.position,
            "detection" : "thermal",
            "date":datetime.datetime.now()  
                }
        process(data)

# J'ai choisi d'utiliser le design pattern ADAPTER car il permet de faire fonctionner deux interfaces différentes ensemble.

class ThermalSensorB_Adapter:
    def __init__ (self,position) :
        self.sensor_b = ThermalSensorB(position) 
        self.position = position
    
    def on_detect(self, callback):
        def json_to_string(json):
            message = f"Detection : {json['detection']}, capteur : {json['sensor']} à {json['date']}"
            callback(message)
        self.sensor_b.trigger_heat_signature(json_to_string)

