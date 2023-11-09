from random import *
import serial
import time

from pygame import mixer 



# Starting the mixer 
mixer.init() 

# Loading the song 
sons = [r"D:\Projetos\PyESP_Song\PyESP_Song\src\naometoque.mp3", r"D:\Projetos\PyESP_Song\PyESP_Song\src\saifora.mp3"]

mixer.music.load(sons[randint(0,1)]) 
#nao esta funcionando a parte do random pois está fora do while. Ele escolhe e seleciona só uma vez o som
#tem que rodar isso dentro do loop para escolher continuamente. tentei rapidamente mas n foi

# Setting the volume 
mixer.music.set_volume(1) 

# Start playing the song 
print("Hey")

esp32 = serial.Serial('COM3', 115200)
touchInfo = ""

while True:
    originalString = str(esp32.readline())
    print(len(originalString))
    if len(originalString) == 10:
        touchInfo = originalString[2:5]
    elif len(originalString) == 9:
        touchInfo = originalString[2:4]
    elif len(originalString) == 8:
        touchInfo = originalString[2]

    print(touchInfo)
    #time.sleep(0.1)
    if(int(touchInfo) < 20):
        mixer.music.play() 
        
