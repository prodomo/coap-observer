# Using requests.
# The url only for WSN.

import requests

url = 'http://140.124.184.204:8082/~/in-cse/cnt-686670342'
raw_data = '{"m2m:cin": { "cnf": "json",	"con": " { Mote:A6FB, Priority:1, EnvTemp:3888, EnvHumi:5435, EnvCO:25, Alarm:0 } "	} }'
requests.post(url, data=raw_data, headers={'X-M2M-Origin':'admin:admin','Content-Type':'application/json;ty=4'})
