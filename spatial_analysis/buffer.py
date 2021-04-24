import psycopg2
import json 
connection = psycopg2.connect(host='localhost',port='5432',database='tubra',user='postgres',password='m1k2h3')

def make_buffer(geom,radius=100):
    print('request data:',geom)
    # this is a geometry creation out of an input geometry via ST_Buffer 
    with connection.cursor() as cur:
        ob = json.dumps(geom)
        cur.execute(f"select ST_GeomFromGeoJSON('{ob}')")
        for i in cur:
            geom = i[0]
        cur.execute(f"select ST_AsGeoJSON(ST_Buffer('{geom}',{radius}))")
        for i in cur:
            buffer_geojson=i[0]
        print('Buffer geometry:',buffer_geojson)
        return buffer_geojson
