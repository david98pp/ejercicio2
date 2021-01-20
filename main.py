"""
Clase principal para consultar datos de Dweppy
author: David Pineda
created: 19/01/2021
"""
# pip install dweepy
import threading
import time

import dweepy

from guardar import guardar

start_time = time.time()
seconds = 30
datos = []


def temperatura():
    return dweepy.get_latest_dweet_for('thecore')[0]['content']['temperature']


def humedad():
    return dweepy.get_latest_dweet_for('thecore')[0]['content']['humidity']


def obtener_datos():
    t = temperatura()
    time.sleep(1)
    h = humedad()
    val = t, h
    datos.append(val)


def repeticiones():
    t = threading.Timer(5, lambda: obtener_datos())
    t.start()
    t.join()


while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    repeticiones()
    if elapsed_time > seconds:
        print("Finished iterating in: " + str(int(elapsed_time)) + " seconds")
        break

guardar(datos)
