import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number="+1 (647) 231-1536"

parsed_number = phonenumbers.parse(number)
location = geocoder.description_for_number(parsed_number, "en")
print(location)

service_provider = carrier.name_for_number(parsed_number, "en")
print(service_provider)

import opencage
from opencage.geocoder import OpenCageGeocode

key="cd726540b11b4caa933b6899a59796e1"
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
# print(result)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)

import folium

myMap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(myMap)
myMap.save("myLocation.html")