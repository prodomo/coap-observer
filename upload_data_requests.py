# Using requests.
# The url only for WSN.

import requests
import string

url = "http://140.124.184.204:8082/~/in-cse/cnt-706018400"
def send(mote,packet_tcflow,temperature,humidity,gasValue,gasAlarm):
    payload = '{"m2m:cin": { "cnf": "json", "con": " { \\\"Mote\\\":\\\"'+mote+'\\\", \\\"Priority\\\":\\\"'+str(packet_tcflow)+'\\\",\\\"EnvTemp\\\":\\\"'+str(temperature*0.01)+'\\\",\\\"EnvHumi\\\":\\\"'+str(humidity*0.01)+'\\\",\\\"EnvCO\\\":\\\"'+str(gasValue)+'\\\",\\\"Alarm\\\":\\\"'+str(gasAlarm)+'\\\"  } " } }'

    headers = {
      'X-M2M-Origin': "admin:admin",
      'Content-Type': "application/json;ty=4",
      'Connection': "close"
      }
    try:
        requests.post(url, data=payload, headers=headers)
    except:
        print "The data can not pass to OM2M server, Please check the internet."
        pass
