#Find the nearest Pizza Place
from googlemaps import GoogleMaps
def FindPizza():
	print "Enter in an address to find Pizza places near it"
	address = raw_input()
	gmaps = GoogleMaps("AIzaSyA5R4PnzAcoe2vpVRKyWWby-d6RrMmIwtQ")
	lat, lng = gmaps.address_to_latlng(address)
	destination = gmaps.latlng_to_address(lat, lng)
	Pizza = gmaps.local_search('pizza near ' + destination)
	directions = gmaps.directions(address, destination)
	print "The nearest Pizza place is " + Pizza['responseData']['results'][0]['titleNoFormatting']
	for step in directions['Directions']['Routes'][0]['Steps']:
		print step['descriptionHtml']

FindPizza()