import psycopg2
connection = psycopg2.connect(host='localhost',port=5432,database='tubra',user='postgres',password='m1k2h3')

def make_linear_measure(coords_1,coords_2):
    # create two points from the coords
    with connection.cursor() as cur:
        p1,p2,d='','',''
        coords_1_lat = coords_1[0]
        coords_1_lng = coords_1[1]
        coords_2_lat = coords_2[0]
        coords_2_lng = coords_2[1]
    
    # postgres expects lng,lat in it's functions

        cur.execute(f'select ST_GeomFromText(ST_AsText(ST_SetSRID(ST_MakePoint({coords_1_lng},{coords_1_lat}),3785)),3785)')
        for i in cur:
            print('full cursor:',i)
            p1=i[0]
            print('point#1 - ',p1)
        cur.execute(f'select ST_GeomFromText(ST_AsText(ST_SetSRID(ST_MakePoint({coords_2_lng},{coords_2_lat}),3785)),3785)')
        for i in cur:
            p2=i[0]
            print('point#2 - ',p2)
        cur.execute(f"select ST_Distance('{p1}','{p2}')")
        for i in cur:
            d=i[0]
        return d

