################
# Author: Marissa Valenzuela
# Final Project
# 11/27/2017
################
import requests

url = 'http://open.mapquestapi.com/directions/v2/route?key=UEQG5WFI9hb68vEfpfHIfIA8UOIN1DQP&from=Irvine%2cca\&to=Los+Angeles&2cca'
payLoad = {'myAPI':'UEQG5WFI9hb68vEfpfHIfIA8UOIN1DQP', 'from': value1, 'to':value2}
r = requests.get('http://open.mapquestapi.com/directions/v2/route?', params=payload)
r = r.json()
steps = r["route"]["legs"][0]["maneuvers"]
directions=[]
for ii in steps:
   directions.append(ii["narrative"])

eLoad = {'myAPI':'UEQG5WFI9hb68vEfpfHIfIA8UOIN1DQP', 'shapeFormat': 'value1'}
totalDistance = r['route']["distance"]
totalTime = r['route']["formattedTime"]
startLng = r['route']['locations'][0]["displayLatLng"]["lng"]
startLat = r['route']['locations'][0]["displayLatLng"]["lat"]
endLng = r['route']['locations'][1]["displayLatLng"]["lng"]
endLat = r['route']['locations'][1]["displayLatLng"]["lat"]

latLng = ("Start: %.2f, %.2f\nEnd: %.2f, %.2f"% (startLat, startLng, endLat, endLng))
e = requests.get('http://open.mapquestapi.com/elevation/v1/profile?key=myAPI&shapeFormat=raw&latLngCollection=value1', params=eLoad)
e = e.json()
elevation = e["elevationProfile"][0]["height"]


def main():
    print(latLng)

main()
