

# Show where the B52 are in latitude and langitude

from __future__ import print_function
import sys


import pylab as pl
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

pl.rc('font', size=15)

#taking key and  bus number from user
key = sys.argv[1]
busnumber = sys.argv[2]

print ("Bus line is ", busnumber)

#url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=71ea6d0f-db19-4f94-a6a6-4f0bf52ad31a&VehicleMonitoringDetailLevel=calls&LineRef=" +busnumber
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" +key+ "&VehicleMonitoringDetailLevel=calls&LineRef=" +busnumber
#print (url)
response = urllib.urlopen(url)
MTABUS = response.read().decode("utf-8")
MTABUS = json.loads(MTABUS)


# total number of  activity buses 
bus_info = MTABUS['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

tb = len(bus_info)


print ("Total number of", sys.argv[2],": ", tb)

for i in range(tb):
  latitude =  MTABUS['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
  longitude = MTABUS['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
  print ("Bus" ,i, "is at latitude ", latitude, "and at longitude ", longitude )


