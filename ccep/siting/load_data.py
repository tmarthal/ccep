import os
import json
from siting.models import County
from django.contrib.gis.geos import GEOSGeometry


county_geojson = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'fixtures', 'counties', 'ca-counties.geojson'),
)



def load_counties(verbose=True):
    print(county_geojson)
    fh = open(county_geojson, 'r')
    geojson = fh.read()
    fh.close()

    gj = json.loads(geojson)

    for county_geo in gj['features']:
        name = county_geo['properties']['name']
        geoid = county_geo['properties']['geoid']
        geometry = GEOSGeometry(json.dumps(county_geo['geometry']))

        # will not create a county if one already exists
        # c = County(name=name, geoid=geoid, mpoly=geometry)
        # c.save()

        county, created = County.objects.update_or_create(
            name=name, defaults={"geoid": geoid, "mpoly": geometry}
        )
        print("created: {} county {} ".format(created, county.name))
