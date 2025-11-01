import timesync, time, emlearn_trees, array

from openweather import *

lat = 42.36
lon = -71.01
apiKey = ""

# timesync.sync()

# with open("wifi_config.txt", "r") as f:
#     lines = f.readlines()
# apiKey = str(lines[2])
# print(apiKey)


model = emlearn_trees.new(5, 50000, 50000)
# Load a CSV file with the model
with open("dt.csv", "r") as f:
    emlearn_trees.load_model(model, f)

weatherData = getLatLonWeather(lat, lon, apiKey, exclude="minutely,daily,alerts")
temp, _, humidity = getCurrentTempHumidity(weatherData)
precip = getCurrentRain(weatherData)
wind, _, _ = getCurrentWind(weatherData)
cloud = getCurrentCloudCover(weatherData)

_, _, _, hr, _, _, _, _ = time.localtime()

# local hr, cloud, humidity, precip, temp, wind
currentCond = [int(hr), int(cloud), int(humidity), int(precip), int(temp), int(wind)] 

#print(model.outputs())
out = array.array("f", range(model.outputs()))
featuresArray = array.array("h", currentCond)

model.predict(featuresArray, out)
output = list(out)
print(list(featuresArray), '->', output)

alertLevel = output.index(max(output))
print("Heat alert level", alertLevel)

if alertLevel==2 or alertLevel==3:
  for i in range(0,10):
      beep(1000, 200)
      time.sleep(0.3)
      beep(500, 100)
      time.sleep(1)


