
#  show whole buses, where at, how many bus stop,  and etc
from __future__ import print_function
import sys
import csv
import pylab as pl
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

pl.rc('font', size=15)

#taking  key and bus number from user
key = sys.argv[1]
busnumber = sys.argv[2]


# url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=71ea6d0f-db19-4f94-a6a6-4f0bf52ad31a&VehicleMonitoringDetailLevel=calls&LineRef=B52"
#url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?" + "key=71ea6d0f-db19-4f94-a6a6-4f0bf52ad31a&VehicleMonitoringDetailLevel=calls&LineRef=B52" 
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" +key+ "&VehicleMonitoringDetailLevel=calls&LineRef=" +busnumber

response = urllib.urlopen(url)
MTABUS = response.read().decode("utf-8")
MTABUS = json.loads(MTABUS)


# save businfo as a variable
businfo = (MTABUS['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

# total number of activity nubses
tb = int(len(businfo))

print ("Latitude, Longitude, Stop Name, Stop Status")

fout = open(busnumber+".csv","w")
fout.write("Latitue,Longitude,Stop Name,Stop Status\n")

for i in range(tb):
    bus_info = MTABUS['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['MonitoredCall']
    latitude =  businfo[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = businfo[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    stop = businfo[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    where = businfo[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    print (latitude,",", longitude,",", stop,",", where) 
    fout.write(str(latitude)+","+ str(longitude)+","+stop+","+where+'\n')






