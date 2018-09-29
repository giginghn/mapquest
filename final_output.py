class LatLong:
    def __init__(self, latLng):
        self.latLng = latLng
    def get_latLng(self):
        return self.latLng

class Directions:
    def __init__(self, steps):
        self.steps = steps
    def get_directions(self):
        return self.steps

class TotalTime:
    def __init__(self, totalTime):
        self.totalTime = totalTime
    def get_totalTime(self):
        return self.totalTime

class TotalDistance:
    def __init__(self, totalDistance):
        self.totalDistance = totalDistance
    def get_totalDistance(self):
        return self.totalDistance

class Elevation:
    def __init__(self, elevation):
        self.elevation = elevation
    def get_elevation(self):
        return self.elevation
class Test:
    def __init__(self, testlist):
        self.testlist = testlist
    def getTestList(self):
        for member in testlist:
            print(testlist)
#in main....
list= [1, 'hi', 34, 73.5]
test_object = Test(list)
test_object.getTestList()

