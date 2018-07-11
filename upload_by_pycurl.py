import pycurl
import StringIO
import re
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

#buffer = BytesIO()
b = StringIO.StringIO()

mkdir_str = {"Mote":"A64A",
            "EnvTemp":"32.20",
            "EnvHumi":"77.88",
            "EnvCo":"21",
            "Alarm":"0"
            }

c = pycurl.Curl()
c.setopt(pycurl.WRITEFUNCTION, b.write) 
c.setopt(pycurl.FOLLOWLOCATION, 1) 
c.setopt(pycurl.MAXREDIRS, 5) 

c.setopt(pycurl.URL, "http://140.124.184.204:8082/~/in-cse/cnt-686670342")
c.setopt(pycurl.HTTPHEADER, ['X-M2M-Origin:admin:admin','Content-Type: application/xml;ty=4'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, urllib.urlencode(mkdir_str))

# c.setopt(c.WRITEFUNCTION, buffer.write)
# # Set our header function.
# c.setopt(c.HEADERFUNCTION, header_function)
c.perform()
c.close()

# Figure out what encoding was sent with the response, if any.
# Check against lowercased header name.
# encoding = None
# if 'content-type' in headers:
#     content_type = headers['content-type'].lower()
#     match = re.search('charset=(\S+)', content_type)
#     if match:
#         encoding = match.group(1)
#         print('Decoding using %s' % encoding)
# if encoding is None:
#     # Default encoding for HTML is iso-8859-1.
#     # Other content types may have different default encoding,
#     # or in case of binary data, may have no encoding at all.
#     encoding = 'iso-8859-1'
#     print('Assuming encoding is %s' % encoding)

# body = buffer.getvalue()
# # Decode using the encoding we figured out.
# print(body.decode(encoding))
body = b.getvalue()
print(body)
print("Done.")