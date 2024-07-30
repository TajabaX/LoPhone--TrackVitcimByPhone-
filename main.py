# 1. In the main we must install Pip packages in the terminal
# 2. That the command we will use in our Terminal: pip install phonenumbers
# 3. after that we will import the packeges we just installed.
##Credits: i have use multipe times ChatGpt for making sure the code is clean and working, and used 3 youtube videos for installing the right packeges.

import opencage
import phonenumbers
from LocationByPhone import number
import folium

from phonenumbers import geocoder
# This will give us the Geography Code

pepenumber = phonenumbers.parse(number)

location = geocoder.description_for_number(pepenumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

key = '0'
# enter your open cage API after register to it
geocoder = OpenCageGeocode(key)
query = str(location)

results = geocoder.geocode(query)
#print(results)
# give us cordinates to track the location of the person

#For Easier thing do it as a shortcut

LAT = results[0]['geometry']['lat']
LNG = results[0]['geometry']['lng']

print(LAT,LNG)

#Install Another Packege now: pip install folium

OurLocation = folium.Map(location=[LAT, LNG]    , zoom_start= 9)
folium.Marker([LAT, LNG], popup=location).add_to(OurLocation)

OurLocation.save("TheLocationOfVictim.html")

#just run it and then go to the html file that was created and open it in your browser
# For educational purposes only hope you enjoyed (:
