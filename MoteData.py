import logging
log = logging.getLogger("moteData")

import upload_data_requests

import struct
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

#Base = declarative_base()

# parser payload information.

class MoteData(self)):
    __tablename__ = 'motor_data'

    # id = Column(Integer, primary_key=True)
    # mote = Column(String(200))
    # packet_tcflow = Column(Integer)
    # start_asn = Column(Integer)
    # end_asn = Column(Integer)
    # event_counter = Column(Integer)
    # event_threshold = Column(Integer)
    # event_threshold_last_change = Column(Integer)
    # packet_counter = Column(Integer)
    # parent_address = Column(String(10))
    # rank = Column(Integer)
    # parent_link_etx = Column(Integer)
    # parent_link_rssi = Column(Integer)
    # gasValue = Column(Integer) # Gas Value 16bit.
    # gasAlarm = Column(Integer) # Gas Alarm 8bit
    # temperature = Column(Integer) # temp 16bit
    # humidity = Column(Integer) # humi 16bit
    # created_at = Column(DateTime, default=datetime.datetime.now)
    # updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __str__(self):
        output = []
        output += ['Motor   : '+motor]
        output += ['Data 1  : '+data1]
        output += ['Data 2  : '+data2]
        output += ['Data 3  : '+data3]
        output += ['Data 4  : '+data4]
        output += ['Data 5  : '+data5]
        output += ['Data 6  : '+data6]
        output += ['Data 7  : '+data7]
        output += ['Data 8  : '+data8]
        output += ['Data 9  : '+data9]
        output += ['Data 10 : '+data10]
        output += ['Data 11 : '+data11]
        output += ['Data 12 : '+data12]
        output += ['Data 13 : '+data13]
        output += ['Data 14 : '+data14]
        output += ['Data 15 : '+data15]
        output += ['Data 16 : '+data16]
        output += ['Data 17 : '+data17]
        output += ['Data 18 : '+data18]
        output += ['Data 19 : '+data19]
        output += ['Data 20 : '+data20]
        output += ['Data 21 : '+data21]
        output += ['Data 22 : '+data22]
        output += ['Data 23 : '+data23]
        output += ['Data 24 : '+data24]
        output += ['Data 25 : '+data25]
        output += ['Data 26 : '+data26]
        output += ['Data 27 : '+data27]
        output += ['Data 28 : '+data28]
        output += ['Data 29 : '+data29]
        output += ['Data 30 : '+data30]
        output += ['Data 31 : '+data31]
        output += ['Data 32 : '+data32]


        return '\n'.join(output)

    @classmethod
    def make_from_bytes(cls, motor, data):
        packet_format = [
            "<xx",  # start_flag
            "xx",    # alignment_padding[2]
            "I",    # Moto Data 1
            "I",    # Moto Data 2
            "I",    # Moto Data 3
            "I",    # Moto Data 4
            "I",    # Moto Data 5
            "I",    # Moto Data 6
            "I",    # Moto Data 7
            "I",    # Moto Data 8
            "I",    # Moto Data 9
            "I",    # Moto Data 10
            "I",    # Moto Data 11
            "I",    # Moto Data 12
            "I",    # Moto Data 13
            "I",    # Moto Data 14
            "I",    # Moto Data 15
            "I",    # Moto Data 16
            "I",    # Moto Data 17
            "I",    # Moto Data 18
            "I",    # Moto Data 19
            "I",    # Moto Data 20
            "I",    # Moto Data 21
            "I",    # Moto Data 22
            "I",    # Moto Data 23
            "I",    # Moto Data 24
            "I",    # Moto Data 25
            "I",    # Moto Data 26
            "I",    # Moto Data 27
            "I",    # Moto Data 28
            "I",    # Moto Data 29
            "I",    # Moto Data 30
            "I",    # Moto Data 31
            "I",    # Moto Data 32
        ]
        packet_format_str = ''.join(packet_format)
        packet_item = struct.unpack(packet_format_str, data)
        mote_data = MoteData(
            motor="Motor_FFT_information",
            data1=packet_item[0],
            data2=packet_item[1],
            data3=packet_item[2],
            data4=packet_item[3],
            data5=packet_item[4],
            data6=packet_item[5],
            data7=packet_item[6],
            data8=packet_item[7],
            data9=packet_item[8],
            data10=packet_item[9],
            data11=packet_item[10],
            data12=packet_item[11],
            data13=packet_item[12],
            data14=packet_item[13],
            data15=packet_item[14],
            data16=packet_item[15],
            data17=packet_item[16],
            data18=packet_item[17],
            data19=packet_item[18],
            data20=packet_item[19],
            data21=packet_item[20],
            data22=packet_item[21],
            data23=packet_item[22],
            data24=packet_item[23],
            data25=packet_item[24],
            data26=packet_item[25],
            data27=packet_item[26],
            data28=packet_item[27],
            data29=packet_item[28],
            data30=packet_item[29],
            data31=packet_item[30],
            data32=packet_item[31],
        )
        #upload_data_requests.send(mote,packet_item[0],packet_item[14],packet_item[15],packet_item[13],packet_item[1])
        return mote_data
    
# add fd00::212:4b00:615:a5d4 g/sicslowpan