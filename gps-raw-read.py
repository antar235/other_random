##python vfersion 3.0
##

import serial
import os
import sys

if sys.version[0]=='3':
    m=input("port number:") #port number input for python 3
else:
    m=raw_input("port number:") #port number input for python 2

if os.name.title()=='Nt':
    ser=serial.Serial('COM'+m, 9600, timeout=1)
else:
    ser=serial.Serial('/dev/tty'+m, 9600, timeout=1) ##for linux

def cleanscreen(): ##clean console screen
    if os.name.title()=='Nt':
        os.system('cls') ##for windows
    else:
        os.system('clear') ##for linux

def parametr_input():
    if sys.version[0]=='3':
        text1=input("Output raw (y/n):")
    else:
        text1=raw_input("Output raw (y/n):")
        
    if (text1=="Y" or text1=="y" or text1=="yes"):
        return(0) ##raw
    else:
        return(1) ##structured

def gps_out():
    x=parametr_input()
    if x==0: ##raw
        while True:
            print(ser.readline())
    elif x==1: ##structured
        latlist=[];
        lonlist=[];
        while True:
            coordbyte=ser.readline()
            if coordbyte[3]==coordbyte[4]:
                cleanscreen()
                if len(coordbyte)>70:
                    timeutc=coordbyte[7:13].decode() # time utc format
                    lat=float(coordbyte[18:27].decode()) # gps latitude
                    lon=float(coordbyte[31:40].decode()) # gps longitude
                    nsat=coordbyte[45:47].decode() # number of sattelites
                    high_sea=coordbyte[53:60].decode() # high of sea
                    print("UTC:"+timeutc+" lat:",lat," lon:",lon)
                    print("satellit:"+nsat+" sea lvl:"+high_sea)
                    print()
                    print("  _|_|_|  _|_|_|    _|_|_|_|_| ")
                    print("_|        _|    _|      _|     ")
                    print("  _|_|    _|_|_|        _|     ")
                    print("      _|  _|            _|     ")
                    print("_|_|_|    _|            _|     ")
                else:
                    print("gps data not valid, wait...")

                

while True:
    gps_out()
