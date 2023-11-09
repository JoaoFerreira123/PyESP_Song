from random import *
import serial
from time import sleep
from pygame import * 


# Starting the mixer 
mixer.init() 

# Setting the volume 
mixer.music.set_volume(1) 

# Start playing the song 
print("Hey")

esp32 = serial.Serial('COM29', 115200)
touchInfo = ""


while True:
    choice = randint(0,5)
    originalString = str(esp32.readline())
    print(len(originalString))
    if len(originalString) == 10:
        touchInfo = originalString[2:5]
    elif len(originalString) == 9:
        touchInfo = originalString[2:4]
    elif len(originalString) == 8:
        touchInfo = originalString[2]

    print(touchInfo)

    if(int(touchInfo) < 20):
        match choice:
            case 0:
                mixer.music.load(r"C:\Users\gabri\OneDrive\Área de Trabalho\Plantas Falantes\naometoque.mp3")
                mixer.music.play()
                sleep(0.1)
            case 1:
                mixer.music.load(r"C:\Users\gabri\OneDrive\Área de Trabalho\Plantas Falantes\Estou com sede, me regue.mp3")
                mixer.music.play()
                sleep(0.1)
            case 2:
                mixer.music.load(r"C:\Users\gabri\OneDrive\Área de Trabalho\Plantas Falantes\Cuide da natureza.mp3")
                mixer.music.play()
                sleep(0.1)
            case 3:
                mixer.music.load(r"C:\Users\gabri\OneDrive\Área de Trabalho\Plantas Falantes\Cuidado com as minhas folhas.mp3")
                mixer.music.play()
                sleep(0.1)
            case 4:
                mixer.music.load(r"C:\Users\gabri\OneDrive\Área de Trabalho\Plantas Falantes\aaaaLuciana (mp3cut.net).mp3")
                mixer.music.play()
                sleep(0.1)
