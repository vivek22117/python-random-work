import sys
import urllib.request
from xml.etree.ElementTree import XML

if(len(sys.argv)) != 3:
    raise SystemExit('Usagae: nextbus_enhance.py route stopId')

route = sys.argv[1]
stop_id = sys.argv[2]
print(route, stop_id)

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(route, stop_id))
data = u.read()
print(data)

doc = XML(data)
for pt in doc.findall('.//pt'):
    print(pt.text)

