# from django.contrib.gis.geoip2 import GeoIP2
# from  bs4  import BeautifulSoup
# import requests
# def scraping () :
#
#         url = 'https://myexternalip.com/'
#         response = requests.get(url)
#         suop = BeautifulSoup(response.text, 'html.parser')
#         a = suop.find('textarea', {'id': 'ip'})
#
#         if a:
#             a = a.text
#             return a

#
# def get_geo(ip):
#     g = GeoIP2()
#     country = g.country(ip)
#     city = g.city(ip)
#     lat, lon = g.lat_lon(ip)
#     return country, city, lat, lon
def get_center_coordinates(latA, longA, latB=None, longB=None):
    cord = (latA, longA)
    if latB:
        cord = [(latA+latB)/2, (longA+longB)/2]
    return cord
def get_zoom(distance):
    if distance <=100:
        return 10
    elif distance > 100 and distance <= 5000:
        return 4
    else:
        return 2