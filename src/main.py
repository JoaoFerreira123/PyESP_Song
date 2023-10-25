import serial
import time

from playsound import playsound

esp32 = serial.Serial('COM5', 115200)

while True:
    originalString = str(esp32.readline())
    touchInfo = originalString[2]
    print(touchInfo)
    time.sleep(0.1)
    if(touchInfo == "1"):
        playsound('D:\Projetos\PyESP_Song\PyESP_Song\src\naometoque.mp3', True)


