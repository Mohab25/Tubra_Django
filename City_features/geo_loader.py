from django.contrib.gis.utils import LayerMapping
from .models import *

OB_Districts_mapping = {
    'name': 'Name',
    'e_name': 'E_Name',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

Obeid_streets_mapping = {
    'name': 'Name',
    'type': 'Type',
    'material': 'Material',
    'quality': 'Quality',
    'shape_leng': 'Shape_Leng',
    'geom': 'MULTILINESTRING',
}

ob_urban_area_mapping = {
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}




def load():
#     # OB_districtshp = '/home/mohab/Main Folder/Airport/nash/Airport/Obied Airport/Tubra/Shapefiles/Ob_districts_fin.shp'
#     # lm1 = LayerMapping(Obeid_districts,OB_districtshp,OB_Districts_mapping,transform=True,encoding='utf-8')
#     # lm1.save()
    OB_streets = '/home/mohab/Main Folder/Airport/nash/Airport/Obied Airport/Tubra/Shapefiles/Ob_streets.shp'
    lm2 = LayerMapping(Obeid_streets,OB_streets,Obeid_streets_mapping,transform=True,encoding='utf-8')
    lm2.save()
#     OB_urban_area = '/home/mohab/Main Folder/Airport/nash/Airport/Obied Airport/Tubra/Shapefiles/Ob_urban_area.shp'
#     lm3 = LayerMapping(Ob_urban_area,OB_urban_area,ob_urban_area_mapping,transform=True,encoding='utf-8')
#     lm3.save()



# import this file and run the load function in the shell 