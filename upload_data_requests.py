# Using requests.
# The url only for WSN.

import requests

class upload_data_requests(Base):

  url = 'http://140.124.184.204:8082/~/in-cse/cnt-686670342'
  
  def send(mote,packet_tcflow,temperature,humidity,gasValue,gasAlarm):
    raw_data = '{"m2m:cin": { "cnf": "json",	"con": " { Mote:'+mote+', Priority:'+packet_tcflow+', EnvTemp:'+temperature+', EnvHumi:'+humidity+', EnvCO:'+gasValue+', Alarm:'+gasAlarm+' } "	} }'
    requests.post(url, data=raw_data, headers={'X-M2M-Origin':'admin:admin','Content-Type':'application/json;ty=4'})
