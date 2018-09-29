import final_maps.py
import final_output.py

def main():
 #   print("%d \n\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors" % elevation
     numLocations = input()

     locations = []
     for ii in range(0, numLocations):
         value1 = input()
         locations.append[value1]
     numOutput = input()
     oneOut = input()
     eList= []
     while oneOut != '':
         if oneOut == "LATLONG":
             for ii in range (0, numLocations):
               print(LatLong.get_latLng())
             print(Directions.get_Directions())
         if oneOut == "TOTAL TIME":
             print(TotalTime.get_totalTime())
         if oneOut == "TOTAL DISTANCE":
             print(TotalDistance.get_totalDistance())
         if oneOut == "ELEVATION":
            for ii in range (0, numLocations):
                elevation1 = elevate
                eList.append[elevate]
            print(eList)
            print(Elevations.get_elevation())
         oneOut = input()

main()
