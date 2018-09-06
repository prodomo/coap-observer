# Using requests.
# The url only for WSN.

import requests
import string

url = "http://140.124.184.204:8082/~/in-cse/cnt-706018400"
def send(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16, data17, data18, data19, data20, data21, data22, data23, data24, data25, data26, data27, data28, data29, data30, data31, data32):
    payload = '{"m2m:cin": { "cnf": "json", "con": "'+str(data1)+', '+str(data2)+', '+str(data3)+', '+str(data4)+', '+str(data5)+', '+str(data6)+', '+str(data7)+', '+str(data8)+', '+str(data9)+', '+str(data10)+', '+str(data11)+', '+str(data12)+', '+str(data13)+', '+str(data14)+', '+str(data15)+', '+str(data16)+', '+str(data17)+', '+str(data18)+', '+str(data19)+', '+str(data20)+', '+str(data21)+', '+str(data22)+', '+str(data23)+', '+str(data24)+', '+str(data25)+', '+str(data26)+', '+str(data27)+', '+str(data28)+', '+str(data29)+', '+str(data30)+', '+str(data31)+', '+str(data32)+'" } }'

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
