## GPS-read v.001
## python(2 and 3) version 3.0 preferable
## cat gps-read.py | tr -d '\r' > gps-read1.py

"""
print coordinates and other data from GPS-devices.

compatible with windows and linux and python(2 and 3-preferable)
==
this script is property of antar235 27.09.17 (cc)
==
"""

import serial
import os
import sys
import serial.tools.list_ports

def aports():
    ports=list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)


aports()

print("enter port number for windows(1,2,3, etc)")
print("for linux only end after -tty- (USB0, ACM0, etc)")

if sys.version[0]=='3':
    m=input("COM port number:") #port number input for python 3
else:
    m=raw_input("COM port number:") #port number input for python 2


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
        if (text1=="Y" or text1=="y" or text1=="yes"):
            return(0) ##raw
        else:
            return(1) ##structured
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
        # latlist=[];
        # lonlist=[];
        while True:
            try:
                coord=(ser.readline()).decode() #just decode
                if coord[3]==coord[4]:
                    cleanscreen()
                    if len(coord)>70:
                        crd=coord.split(',')
                        timeutc=crd[1] # time utc format
                        lat=crd[2] # gps latitude
                        lon=crd[4] # gps longitude
                        nsat=crd[7] # number of sattelites
                        high_sea=crd[9] # high of sea
                        print("port "+m)
                        print("UTC:"+timeutc+" lat:"+lat+" lon:"+lon)
                        print("satellit:"+nsat+" sea lvl:"+high_sea)
                        print("                                (R)")
                        print("  _|_|_|  _|_|_|    _|_|_|_|_| ")
                        print("_|        _|    _|      _|     ")
                        print("  _|_|    _|_|_|        _|     ")
                        print("      _|  _|            _|     ")
                        print("_|_|_|    _|            _|     ")
                    else:
                        print("port "+m)
                        print("gps data not valid, wait...")
            except UnicodeDecodeError:
                ## flush com ports!!!!
                print("port "+m)
                print("gps data not valid, wait...")

                

gps_out()

