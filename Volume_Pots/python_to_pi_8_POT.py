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

        #sleep(0.2)
        
    with MCP3008(channel=1) as pot2:
        print(pot2.value);
        message2 = '2 ' +  str(pot2.value) + ';'
        send2Pd(message2)

        #sleep(0.2)
        
    with MCP3008(channel=2) as pot3:
        print(pot3.value);
        message3 = '3 ' +  str(pot3.value) + ';'
        send2Pd(message3)

        #sleep(0.2)
        
    with MCP3008(channel=3) as pot4:
        print(pot4.value);
        message4 = '4 ' +  str(pot4.value) + ';'
        send2Pd(message4)

        #sleep(0.2)

    with MCP3008(channel=4) as pot5:
        print(pot5.value);
        message5 = '5 ' +  str(pot5.value) + ';'
        send2Pd(message5)

        #sleep(0.2)
        
    with MCP3008(channel=5) as pot6:
        print(pot6.value);
        message6 = '6 ' +  str(pot6.value) + ';'
        send2Pd(message6)

        #sleep(0.2)

    with MCP3008(channel=6) as pot7:
        print(pot7.value);
        message7 = '7 ' +  str(pot7.value) + ';'
        send2Pd(message7)

        #sleep(0.2)

    with MCP3008(channel=7) as pot8:
        print(pot8.value);
        message8 = '8 ' +  str(pot8.value) + ';'
        send2Pd(message8)
        
        #sleep(0.02)
