import logging
log = logging.getLogger("moteData")

import struct
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, VARCHAR, Float

Base = declarative_base()


class MoteData(Base):
    __tablename__ = 'itri_topology_neighbors'

    id = Column(Integer, primary_key=True)
    devAddr = Column(String(45))
    SN = Column(Integer)
    mode = Column(String(45))
    PDR = Column(Float)
    rank = Column(Integer)
    parentAddr = Column(String(45))
    neighborNum = Column(Integer)
    datetime = Column(DateTime, default=datetime.datetime.now)
    n1 = Column(String(45))
    rssi1=Column(Integer)

    def __str__(self):
        output = []
        output += ['devAddr    : {0}'.format(self.devAddr)]
        output += ['SN: {0}'.format(self.SN)]
        output += ['mode  : {0}'.format(self.mode)]
        output += ['PDR      : {0}'.format(self.PDR)]
        output += ['rank      : {0}'.format(self.rank)]
        output += ['parentAddr    : {0}'.format(self.parentAddr)]
        output += ['neighborNum      : {0}'.format(self.neighborNum)]
        output += ['datetime  : {0}'.format(self.datetime)]
        output += ['n1    : {0}'.format(self.n1)]
        output += ['rssi1   : {0}'.format(self.rssi1)]
        return '\n'.join(output)

    @classmethod
    def make_from_bytes(cls, mote, data):
        packet_format = [
            "H",    #packet_Conter
            "H",    #rank
            "h",    #parent
            "H",    #parent_etx
            "H",    #num_neighbor
            "H",    #rssi
            "H",    #battery
            "H",    #battery_threshold
            "H",    #int_tempature
            "H",    #ext_tempature
            "H",    #sensor_threshold
            "H",    #period
            "H",    #priority
        ]
        packet_format_str = ''.join(packet_format)
        packet_item = struct.unpack(packet_format_str, data) #according format change data to packet_item
        mote_data = MoteData(
            devAddr=mote,
            SN = packet_item[0],
            mode = None,
            PDR = float(1.0/float(packet_item[3]/64)),
            rank = packet_item[1],
            parentAddr = packet_item[2],
            neighborNum = 1,
            n1 = packet_item[2],
            rssi1 = packet_item[5],
        )
        return mote_data
