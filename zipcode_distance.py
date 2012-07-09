import sqlalchemy
import math

db = sqlalchemy.create_engine('sqlite:///zipcodes.db')
db.echo = False

def build_metadata():
    metadata = sqlalchemy.MetaData(db)
    metadata.bind.echo = False
    metadata.bind.text_factory = str

    return metadata

def select_zipcode(zipcode):
    fields = (
        'zip',
        'city',
        'state',
        'lat',
        'long',
        'timezone',
        'dst',
        )
    metadata = build_metadata()
    zipcodes_table = sqlalchemy.Table('zipcodes', metadata, autoload=True)
    result = zipcodes_table.select(zipcodes_table.c.zip == zipcode)
    try:
        return dict(zip(fields,result.execute().fetchone()))
    except (TypeError, sqlalchemy.exc.OperationalError):
        return False


def distance(zipcode1, zipcode2):
    z1 = select_zipcode(zipcode1)
    z2 = select_zipcode(zipcode2)
    if not(z1) or not(z2):
        print "Zip Code Not Found In Database."
        sys.exit()
    return haversine(z1['lat'], z1['long'], z2['lat'], z2['long'])

def haversine(lat1, long1, lat2, long2):
    """
    haversine formula to calculate the distance from lat/long coords on a sphere.
    Because the earth is somewhat elliptical can give errors up to 0.3%
    """
    radius = 3963.1676 #Radius of earth in miles
    lat1, long1, lat2, long2 = map(math.radians, [lat1, long1, lat2, long2])
    dlat = lat2 - lat1
    dlong = long2 - long1

    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlong/2) * math.sin(dlong/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d



if __name__ == "__main__":
    import sys
    try:
        print "Distance in miles: %.2f" % distance(sys.argv[1], sys.argv[2])
    except IndexError:
        print "arguements are 2 US Zip Codes\nzipcode_distance zipcode1 zipcode2"