from robust import MQTTClient
import re #regex para coletar os valores do form
import json
from machine import ADC, Pin, I2C
import machine
import random
from time import sleep
import time
import utime


try:
  import usocket as socket
except:
  import socket

#Funcoes para integarir via mqtt com o iothub
def create_mqtt_client(client_id, hostname, username, password, port=8883, keepalive=120, ssl=True):
    if not keepalive:
        keepalive = 120
    if not ssl:
        ssl = True
    c = MQTTClient(client_id=client_id, server=hostname, port=8883, user=username, password=password, keepalive=120, ssl=True)
    c.DEBUG = True
    return c


def get_telemetry_topic(device_id):
    return get_topic_base(device_id) + "/messages/events/"
    
def get_c2d_topic(device_id):
     return get_topic_base(device_id) + "/messages/devicebound/#"

def get_topic_base(device_id, module_id=None):
    if module_id:
        base_str = "devices/" + device_id + "/modules/" + module_id
    else:
        base_str = "devices/" + device_id
    return base_str

DELIMITER = ";"
VALUE_SEPARATOR = "="

def parse_connection(connection_string):
    cs_args = connection_string.split(DELIMITER)
    dictionary = dict(arg.split(VALUE_SEPARATOR, 1) for arg in cs_args)
    return dictionary

def save_json(dictValues):
    with open('vars.json', 'w') as sj: 
        json.dump(dictValues, sj)
    sj.close()
    print("Arquivo salvo!. Reiniciando")
    sleep(1)
    reset()

def open_json():
    with open('vars.json', 'r') as rj:
        survey_data = json.load(rj)
        survey_data['sas_token_str'] = survey_data['sas_token_str'].replace(" ","_")
    rj.close()
    return survey_data

##############################################
#Projeto com Sensores

#Sensor Jean
sound_sensor = Pin(4, Pin.IN, Pin.PULL_UP)

def sensor_get_values():
  sound_value = "Sound captured"

  if sound_sensor.value() == 0: sound_value = "No Sound"

  
  msg = {}
  msgfull = {}
  msg["Sound_Sensor"] = Sound_value
  msg["time"] = time.time()
  return json.dumps(msg)









