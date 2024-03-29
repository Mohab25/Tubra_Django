from django.contrib.gis.utils import LayerMapping
from .models import * 

ob_airport_mapping = {
    'objectid': 'OBJECTID',
    'shape_leng': 'Shape_Leng',
    'shape_le_1': 'Shape_Le_1',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

airport_parts_mapping = {
    'name': 'Name',
    'geom': 'MULTIPOLYGON',
}

poi_mapping = {
    'point': 'Point',
    'ellipsoid': 'Ellipsoid',
    'altitude_EGM96': 'Altitude E',
    'type': 'Type',
    'geom': 'MULTIPOINT',
}


def loader():
    shp = '/home/mohab/Main Folder/Airport/nash/Airport/Obied Airport/Tubra/Shapefiles/test/obeid POIs.shp'
    lm1 = LayerMapping(POIs,shp,poi_mapping,transform=True,encoding='utf-8')
    lm1.save()
    # ob_airport_parts = '/home/mohab/Main Folder/Airport/nash/Airport/Obied Airport/Tubra/Shapefiles/test/airport parts.shp'
    # lm1 = LayerMapping(airport_parts,ob_airport_parts,airport_parts_mapping,transform=True,encoding='utf-8')
    # lm1.save()