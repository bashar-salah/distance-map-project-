from django.shortcuts import render
import folium
from geopy.geocoders import Nominatim
from .utiles import get_center_coordinates,get_zoom
from geopy.distance import geodesic
from.models import map
from django.http import HttpResponse
# Create your views here.
def  bashar_map (requset) :
    try:
        location = Nominatim(user_agent='map')
        model=map()

        m = folium.Map(location=get_center_coordinates(31.4380,34.3900),prefer_canvas =True,control_scale=True,zoom_start=10,tiles='cartodb positron')

        my = ''
        des = ''
        distance = 20


        if requset.method == 'POST':
            my = requset.POST.get('my', False)
            new = location.geocode(my)
            lat = new.latitude
            lon = new.longitude
            model.myplace=my
            point_a = [lat,lon]
            des = requset.POST.get('destination', False)
            a = location.geocode(des)
            point_b = [a.latitude,a.longitude]
            model.destnation=des
            distance = round(geodesic(point_a,point_b).km,2)

            print(distance)
            model.distance=distance
            model.save()

            m = folium.Map(location=get_center_coordinates(lat, lon,a.latitude,a.longitude), zoom_start=get_zoom(distance), tiles='cartodb positron')
            folium.Marker([lat,lon],popup=my).add_to(m)
            folium.Marker([a.latitude,a.longitude],popup=des).add_to(m)
            line = folium.PolyLine(locations=[point_a,point_b],wight=10,color='red',popup=str(distance)+'km',tooltip=str(distance)+'km')
            m.add_child(line)


        m=m._repr_html_()
        return render(requset,'map.html',{'map':m,'my':my,'des':des,'dis':distance})
    except Exception as a  :
        return HttpResponse(a)
