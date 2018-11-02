import logging
log = logging.getLogger("moteData")

import struct
import datetime

class MoteData():

    def __init__(self, moteAddr, packet):
        split_data = moteAddr.split(':')
        self.moteAddr = split_data[5]
        self.packet_counter = packet[0]
        self.rank = packet[1]
        self.parent = "".join("{:02x}".format(ord(c)) for c in packet[2:4])
        self.parent_etx = packet[4]
        self.num_neighbor = packet[5]
        self.rssi = packet[6]
        self.sensor_value = packet[7]/10
        self.sensor_threshold = packet[8]
        self.battery = packet[9]
        self.battery_threshold = packet[10]
        self.type = packet[11]
        self.period = packet[12]
        self.priority = packet[13]

    def __str__(self):
        output = []
        output += ['moteAddr    : {0}'.format(self.moteAddr)]
        output += ['packet_counter: {0}'.format(self.packet_counter)]
        output += ['rank  : {0}'.format(self.rank)]
        output += ['parent      : {0}'.format(self.parent)]
        output += ['parent_etx      : {0}'.format(self.parent_etx)]
        output += ['num_neighbor    : {0}'.format(self.num_neighbor)]
        output += ['rssi      : {0}'.format(self.rssi)]
        output += ['battery  : {0}'.format(self.battery)]
        output += ['battery_threshold    : {0}'.format(self.battery_threshold)]
        output += ['type   : {0}'.format(self.type)]
        output += ['sensor_value  : {0}'.format(self.sensor_value)]
        output += ['sensor_threshold    : {0}'.format(self.sensor_threshold)]
        output += ['period   : {0}'.format(self.period)]
        output += ['priority   : {0}'.format(self.priority)]
        return '\n'.join(output)

    @classmethod
    def make_from_bytes(cls, mote, data):
        packet_format = [
            "H",    #packet_Conter
            "H",    #rank
            "cc",   #parent
            "H",    #parent_etx
            "H",    #num_neighbor
            "h",    #rssi
            "H",    #sensor_value
            "H",    #sensor_threshold
            "B",    #battery
            "B",    #battery_threshold
            "B",    #type
            "B",    #period
            "B",    #priority
            "x",  # alignment_padding[3]
        ]
        packet_format_str = ''.join(packet_format)
        packet_item = struct.unpack(packet_format_str, data) #according format change data to packet_item
        log.debug("mote data: {0}".format(mote))

        mote_data = MoteData(mote, packet_item)
        return mote_data