print('Led_Teste1')

from time import sleep
from machine import Pin

while True:
  led=Pin(2,Pin.OUT)
  led.value(1)
  sleep(0.5)
  led.value(0)
  sleep(0.5)



# Se voc锚 conseguiu fazer tudo certo, o print acima deve aparecer no relat贸rio do seu equipamento

# Procure mudar o que est谩 no script e veja atualizar

# Detalhe: em alguns equipamento entre uma atualiza莽茫o e outra pode levar alguns minutos
# Na minha ESP32 atualiza uma vez a cada uns 3 minutos sem nenhum erro
# J谩 na minha LoRa 32 atualiza direto sem intervalos de tempo 