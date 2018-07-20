# Using requests.
# The url only for WSN.

import requests
import string

url = 'http://140.124.184.204:8082/~/in-cse/cnt-686670342'
def send(mote,packet_tcflow,temperature,humidity,gasValue,gasAlarm):
  raw_data = '{"m2m:cin": { "cnf": "json",	"con": " { Mote:'+mote+', Priority:'+str(packet_tcflow)+', EnvTemp:'+str(temperature)+', EnvHumi:'+str(humidity)+', EnvCO:'+str(gasValue)+', Alarm:'+str(gasAlarm)+' } "	} }'
  requests.post(url, data=raw_data, headers={'X-M2M-Origin':'admin:admin','Content-Type':'application/json;ty=4'})
