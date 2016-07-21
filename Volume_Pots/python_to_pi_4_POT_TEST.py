#! /usr/bin/python

from gpiozero import MCP3008
import os
from time import sleep

def send2Pd(message=' '):
    os.system("echo '" + message + "' | pdsend 3000");

while True:
    with MCP3008(channel=0) as pot1:
        print(pot1.value);
        message1 = '1 ' +  str(pot1.value) + ';'
        send2Pd(message1)

        #sleep(1)
        
    with MCP3008(channel=1) as pot2:
        print(pot2.value);
        message2 = '2 ' +  str(pot2.value) + ';'
        send2Pd(message2)

        #sleep(1)
        
    with MCP3008(channel=2) as pot3:
        print(pot3.value);
        message3 = '3 ' +  str(pot3.value) + ';'
        send2Pd(message3)

        #sleep(1)
        
    with MCP3008(channel=3) as pot4:
        print(pot4.value);
        message4 = '4 ' +  str(pot4.value) + ';'
        send2Pd(message4)

        sleep(0.02)
