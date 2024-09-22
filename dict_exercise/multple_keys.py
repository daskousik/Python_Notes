# Python dictionary with keys having multiple inputs to get access to the keys.
# Let us consider a dictionary where longitude and latitude are the keys and the place to which they belong to is the value.
places = {("19.07'53.2", "72.54'51.0"): "Mumbai",
          ("28.33'34.1", "77.06'16.6"):"Delhi"}

print(places)

keys =[]
lat = []
lang =[]
for key, value in places.items():
    print(key, value)
    keys.append(key)
print(keys)
for i in keys:
    lat.append(i[0])
    lang.append(i[1])
print(lat)
print(lang)
