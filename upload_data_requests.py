import requests,json

url = 'http://140.124.184.204:8082/~/in-cse/cnt-686670342'
raw_data = '{"m2m:cin": { "cnf": "json",	"con": " { Mote:A6F6, EnvTemp:3531, EnvHumi:6085, EnvCO:40, Alarm:0 } "	} }'
requests.post(url, data=raw_data, headers={'X-M2M-Origin':'admin:admin','Content-Type':'application/json;ty=4'})
