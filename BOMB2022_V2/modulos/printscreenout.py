import mss
import numpy
import time
import pyautogui
from datetime import datetime
import cv2 as cv2
#######################################################################################################
def printScreenTela():
    with mss.mss() as sct:
        # Não entendi o motivo deste comando
        monitor = {"top": 160, "left": 160, "width": 1000, "height": 135}

        sct_img = numpy.array(sct.grab(sct.monitors[0]))
        return sct_img[:,:,:3]
#######################################################################################################
def printScreenBox(x,y,w,h):
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": y, "left": x, "width": w, "height": h}
        # Grab the data
        sct_img = numpy.array(sct.grab(monitor))
        #mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        return sct_img[:,:,:3]    

#######################################################################################################
def Scroll(scroolnum = -100):#Padrão Baixo
    last = 1
    while last < 21:
        #carregando todos os usuarios
        pyautogui.scroll(scroolnum)
        if(last == 21):
            time.sleep(0.3)
            break

        last = last + 1
        time.sleep(0.1)
#######################################################################################################
def horarioexato():
    return datetime.today().strftime("%Hh%Mmin%Ss DO DIA %d/%m/%Y")