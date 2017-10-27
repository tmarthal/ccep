from django.http import HttpResponse

from django.views.decorators.http import require_http_methods

import json
import urllib
import certifi
from geopy.geocoders import Nominatim


def uo(args, **kwargs):
    """ monkey patching geopy to get the urllib to handle python3 certs"""
    return urllib.request.urlopen(args, cafile=certifi.where(), **kwargs)


@require_http_methods(["POST"])
def geocode(request):
    addr = request.POST.get("addr", None)

    data = {}
    if addr:
        geolocator = Nominatim()
        geolocator.urlopen = uo
        #TODO add try / catch? for rate limits and whatever
        location = geolocator.geocode(addr)
        print(dir(location))
        if location:
            print(addr, location.latitude, location.longitude)
            print(location.point)
            print(location.raw)
            data = {
                'addr': addr,
                'lat': location.latitude,
                'lon': location.longitude,
                'message': location.address,
            }
        else:
            data = {
                'addr': addr,
                'message': 'no location found'
            }


    return HttpResponse(json.dumps(data), content_type='application/json')

