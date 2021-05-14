from django.test import TestCase
from Documents.models import Document,Document_Type
from Aerodrome_features.models import Aerodrome_Entity 
from Aerodrome.models import Aerodrome


class ModelTest(TestCase):
    def test_document_creation(self):
        doc_type = Document_Type.objects.create(Doc_type='word')
        aerodrome = Aerodrome.objects.create(Name='PortSudan')
        aerodrome_feat = Aerodrome_Entity.objects.create(Aerodrome=aerodrome,Feature_Name='Runway')
        doc = Document.objects.create(Name='Doc1',Document_type=doc_type,Document_file='file1',Aerodrome_Entity=aerodrome_feat,Aerodrome=aerodrome)
        self.assertTrue(isinstance(doc,Document))
        return doc 
