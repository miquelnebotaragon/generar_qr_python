#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Mòduls a importar:
import qrcode
import time

# Variables:
url = (input("Introdueix la URL: ")) # URL de la qual volem crear un qr.
time.sleep(1) # Atura l'execució del programa durant 1 segon.
nom_guardar = (input("Amb quin nom vols guardar l'arxiu? ")) # Nom per guardar el qr generat.
imatge_qr = qrcode.make(url) # El mòdul "qrcode" genera el qr.

# Execució:
imatge_qr.save(nom_guardar+".png") # Guardam la imatge al mateix directori que el programa.
