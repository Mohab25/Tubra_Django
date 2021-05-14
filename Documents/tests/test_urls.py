from django.test import TestCase,Client
from django.urls import reverse 
from Documents.models import Document,Document_Type
from Aerodrome_features.models import Aerodrome_Entity 
from Aerodrome.models import Aerodrome
from Documents.views import *
from rest_framework.test import APIClient

class UrlsTest(TestCase):
    def setUp(self) -> None:

        """setting up the client runs before every test, it's a browser-less client to 
        test req/res of the app """

        self.c = Client()
        return super().setUp()
    
    @classmethod
    def setUpTestData(cls):

        """ setting up the data to certain tests,
        note if you checked for a detailed view url, as f'/Reports/document/{5}/',
        it won't work because the data is not present on the temp database created by 
        the test, you need this class method."""

        # three doc types
        cls.doc_type = Document_Type.objects.create(Doc_type='word')
        cls.doc_type2 = Document_Type.objects.create(Doc_type='excel')
        cls.doc_type3 = Document_Type.objects.create(Doc_type='pdf')
        # aerodrome name and entity
        cls.aerodrome = Aerodrome.objects.create(Name='PortSudan')
        cls.aerodrome_feat = Aerodrome_Entity.objects.create(Aerodrome=cls.aerodrome,Feature_Name='Runway')
        # word docs
        cls.doc1 = Document.objects.create(Name='Doc1',Document_type=cls.doc_type,Document_file='file1',Aerodrome_Entity=cls.aerodrome_feat,Aerodrome=cls.aerodrome)
        cls.doc2 = Document.objects.create(Name='Doc2',Document_type=cls.doc_type,Document_file='file2',Aerodrome_Entity=cls.aerodrome_feat,Aerodrome=cls.aerodrome)
        # excel docs
        cls.doc3 = Document.objects.create(Name='Doc3',Document_type=cls.doc_type2,Document_file='file3',Aerodrome_Entity=cls.aerodrome_feat,Aerodrome=cls.aerodrome)
        cls.doc4 = Document.objects.create(Name='Doc4',Document_type=cls.doc_type2,Document_file='file4',Aerodrome_Entity=cls.aerodrome_feat,Aerodrome=cls.aerodrome)
        # pdf docs
        cls.doc5 = Document.objects.create(Name='Doc5',Document_type=cls.doc_type3,Document_file='file5',Aerodrome_Entity=cls.aerodrome_feat,Aerodrome=cls.aerodrome)
        cls.doc6 = Document.objects.create(Name='Doc6',Document_type=cls.doc_type3,Document_file='file6',Aerodrome_Entity=cls.aerodrome_feat,Aerodrome=cls.aerodrome)

       
    def test_docs_list(self):
        
        """ testing the documents list returned be DocumentList view, it represent all items being returned from a
         given matching title.
        """
        res = self.c.get('/Reports/',{'title':'D'}) # even if the title is empty the test will pass, it the request itself is ok and returns an empty queryset.
        # test the request status
        self.assertEqual(res.status_code,200)
        # test the view name
        self.assertEqual(res.resolver_match.func.__name__,DocumentList.as_view().__name__)
        # test the content size of the response
        self.assertEqual(len(res.json()),6)
        # checking the content first item
        items = res.json()
        d1 = items[0]
        self.assertEqual((d1['pk'],d1['Name'],d1['url']),(1,'Doc1','http://testserver/Reports/document/1/'))


    def test_word_docs_list(self):
        """ testing the files returned by WordDocumentList, the type is a word document
        """
        res = self.c.get('/Reports/word_docs/')
        # test the response status
        self.assertEqual(res.status_code,200)
        # test the view name
        self.assertEqual(res.resolver_match.func.__name__,WordDocumentList.as_view().__name__)
        # test the conetnt size of the response
        self.assertEqual(len(res.json()),2)
        # test content second item
        d2 = res.json()[1]
        self.assertEqual((d2['pk'],d2['Name'],d2['url']),(2,'Doc2','http://testserver/Reports/document/2/'))


    def test_excel_docs_list(self):
        """ testing the files returned by ExcelDocumentList, the type is a excel document
        """
        res = self.c.get('/Reports/excel_docs/')
        # test response status
        self.assertEqual(res.status_code,200)
        # test the view name
        self.assertEqual(res.resolver_match.func.__name__,ExcelDocumentList.as_view().__name__)
        # test the conetnt size of the response
        self.assertEqual(len(res.json()),2)
        # test content first item
        d1 = res.json()[0]
        self.assertEqual((d1['pk'],d1['Name'],d1['url']),(3,'Doc3','http://testserver/Reports/document/3/'))


    def test_pdf_docs_list(self):
        """ testing the files returned by PDFDocumentList, the type is a pdf document
        """
        res = self.c.get('/Reports/pdf_docs/')
        # test response status
        self.assertEqual(res.status_code,200)
        # test the view name
        self.assertEqual(res.resolver_match.func.__name__,PDFDocumentList.as_view().__name__)
        # test the conetnt size of the response
        self.assertEqual(len(res.json()),2)
        # test content first item
        d1 = res.json()[0]
        self.assertEqual((d1['pk'],d1['Name'],d1['url']),(5,'Doc5','http://testserver/Reports/document/5/'))


    def test_doc_by_id(self):
        """ testing a returned file according to it's id with DocumentDetail view
        """
        res = self.c.get(reverse('document-detail',kwargs={'pk':self.doc1.id}))
        # test the response status
        self.assertEqual(res.status_code,200)
        # test the view name 
        self.assertEqual(res.resolver_match.func.__name__,DocumentDetail.as_view().__name__)
        # test the first item of the response
        d1 = res.json()
        self.assertEqual((d1['pk'],d1['Name'],d1['url']),(1,'Doc1','http://testserver/Reports/document/1/'))


    def test_doc_type(self):
        """ testing a file_type according to file type id with DocumentTypeDetail view
        """
        res = self.c.get(reverse('document_type-detail',kwargs={'pk':self.doc_type.id}))
        # test the response status
        self.assertEqual(res.status_code,200)
        # test the view name 
        self.assertEqual(res.resolver_match.func.__name__,DocumentTypeDetail.as_view().__name__)
        # test the first item of the response
        d1 = res.json()
        self.assertEqual((d1['pk'],d1['Doc_type']),(1,'word'))


