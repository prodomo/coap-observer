import os
import serial
folder = 'D:/CPS_Moto_Data/'

# ser = serial.Serial('COM3', 115200,)

ser = serial.Serial()
ser.baudrate = 115200
ser.prot = 'COM4' # for NetLab_Desktop
ser.open() # open the UART port.

