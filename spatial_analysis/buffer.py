import psycopg2
import json 
connection = psycopg2.connect(host='localhost',port=5432,database='tubra',user='postgres',password='m1k2h3')

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

def helper_cur_return_geojson(geom):
    with connection.cursor() as cur:
        cur.execute(f"select ST_AsGeoJSON('{geom}')")
        for i in cur:
            return i[0]

def find_intersecting_geom(geom):
    if geom == None:
        return 
    else:
        with connection.cursor() as cur:
            ob = json.dumps(geom)
            all_features= []
            pavement_geom_list, entity_geom_list = [],[]

            print('buffer search view main:',ob)
            cur.execute(f"select * from \"Aerodrome_features_aerodrome_entity\",\"Aerodrome_features_pavement_construction\" where ST_Intersects(geom,ST_GeomFromGeoJSON('{ob}'))")
            print('buffer search view main:',ob)
            if cur.rowcount==0:
                return []
            else:
                for i in cur:
                    entity_geom_list.append({"Feature_Name":i[1],"entity_geom":helper_cur_return_geojson(i[2])}) # i need the keys in all lists to be the same name for a unified response
                    pavement_geom_list.append({"Feature_Name":i[11],"entity_geom":helper_cur_return_geojson(i[33])})
            
                all_features = entity_geom_list+pavement_geom_list
                return all_features
