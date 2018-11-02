import serial
from collections import OrderedDict
import MySQLdb
from datetime import datetime, timedelta
import socket, sys 
from thread import *
import Queue
import time
import logging
log = logging.getLogger("writetodb")

class WriteToDB():
	def __init__(self, db, data):
		self.db = db
		self.data = data

	def upload_to_DB(self, db, data):
		cursor = db.cursor()

		sql= "CREATE TABLE IF NOT EXISTS itri_MOEA_current_sensor ( `sn` INT(11), `position` VARCHAR(80), `mac_addr` VARCHAR(45), `led_status` VARCHAR(45), `pyranometer` INT(11), `int_temperature` FLOAT, `ext_temperature` FLOAT, `battery_volt` FLOAT, datetime DATETIME, `ID` INT(11), PRIMARY KEY(`mac_addr`))"

		try:
			cursor.execute(sql)
			db.commit()
			log.debug("1.connect SQL success !!")
		except:
			#db.rollback()
			log.debug("1.connect SQL failed !!")

		if(1):
			sensor_sql = "INSERT INTO itri_MOEA_sensor(sn, mac_addr, \
					ext_temperature, pyranometer, datetime, int_temperature, battery_volt) \
					VALUES ('%d', '%s', '%.2f', '%d', '%s', '%.2f', '%.2f')" %\
					(data.packet_counter, data.moteAddr, data.sensor_value,\
					0, \
					datetime.now(), 0, data.battery)

			sensor_current_sql = "REPLACE INTO itri_MOEA_current_sensor(sn, mac_addr, \
					ext_temperature, pyranometer, datetime, int_temperature, battery_volt) \
					VALUES ('%d', '%s', '%.2f', '%d', '%s', '%.2f', '%.2f')" %\
					(data.packet_counter, data.moteAddr, data.sensor_value,\
					0, \
					datetime.now(), 0, data.battery)
			try:
				# Execute the SQL command
				log.debug("2.insert senor data!")
				cursor.execute(sensor_sql)
				cursor.execute(sensor_current_sql)
				# Commit your changes in the database
				db.commit()
				# log.debug('D={1}, sql={0}'.format(sensor_sql, datetime.now()))
				log.debug('insert senor successed')
			except:
				# Rollback in case there is any error
				#db.rollback()
				log.debug('insert senor failed, do not rollback')

			pdr = 1.0/(float(data.parent_etx)/64)

			neighbors_sql = "INSERT INTO itri_topology_neighbors(mode, neighborNum, devAddr,PDR,\
				parentAddr, datetime, SN, rank, n1, rssi1)\
				VALUES ('%s', '%d', '%s', '%.2f', '%s', '%s', '%d', '%d', '%s', '%d')"\
				%('0x11', data.num_neighbor, data.moteAddr, pdr, data.parent, \
				datetime.now(), data.packet_counter, data.rank, data.parent, data.rssi)

			neighbors_current_sql = "REPLACE INTO itri_topology_current_neighbors(mode, neighborNum, devAddr,PDR,\
				parentAddr, datetime, SN, rank, n1, rssi1)\
				VALUES ('%s', '%d', '%s', '%.2f', '%s', '%s', '%d', '%d', '%s', '%d')"\
				%('0x11', data.num_neighbor, data.moteAddr, pdr, data.parent, \
				datetime.now(), data.packet_counter, data.rank, data.parent, data.rssi)
			

			try:
				cursor.execute(neighbors_sql)
				db.commit()
				cursor.execute(neighbors_current_sql)
				db.commit()
				# log.debug('sql={0}'.format(neighbors_sql))
				log.debug('insert neighbor table successed')
			except:
				# Rollback in case there is any error
				#db.rollback()
				log.debug('insert neighbor failed, do not rollback')