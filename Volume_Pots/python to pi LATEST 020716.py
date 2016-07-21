from gpiozero import MCP3008
import os
from time import sleep

pot1 = MCP3008(channel=0)
pot2 = MCP3008(channel=1)

def send2Pd(message=' '):
    os.system("echo '" + message + "' | pdsend 3000");

while True:

    #print "potONE str(pot1.value) ","potTWO str(pot2.value) "

    send2Pd('0 ' +  str(pot1.value) + ';')

    send2Pd('1 ' +  str(pot2.value) + ';')

    #sleep(0.01) 
