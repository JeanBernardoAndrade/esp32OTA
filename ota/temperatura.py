
import esp32
from time import sleep
while True:
  temperatura_I = esp32.raw_temperature()
  print("Temperatura interna do Esp32 em 掳F 茅: ", temperatura_I)
  sleep(1)
  Celcius = (temperatura_I - 32)/1.8
  print("Temperatura interna do Esp32 em 掳C 茅: ", Celcius)
  sleep(1)   
