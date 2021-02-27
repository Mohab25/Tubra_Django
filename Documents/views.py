from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *


# either you use a class based views or function views, and class based views either to
#  use django view or rest_framework class based generic api views 

class DocumentList(ListCreateAPIView):
    model = Document
    serializer_class = DocumentSerializer
    name = 'document-list' 
    # what happens here that the view evaluate either a post or get request, then 
    # if it get request the view performs a Doc.objects.all(), serialize the objects
    # and renders them 
    # and if it's a post request, it parses the request.data, serialize it and saves it
    # to the database.  

class WordDocumentList(ListCreateAPIView):
    queryset = Document.objects.filter(Document_type=1)
    serializer_class = DocumentSerializer
    name = 'ms_word_document-list' 

class ExcelDocumentList(ListCreateAPIView):
    queryset = Document.objects.filter(Document_type=2)
    serializer_class = DocumentSerializer
    name = 'ms_excel_document-list' 

class PDFDocumentList(ListCreateAPIView):
    queryset = Document.objects.filter(Document_type=3)
    serializer_class = DocumentSerializer
    name = 'pdf_document-list' 

class DocumentDetail(RetrieveUpdateDestroyAPIView):
    model = Document 
    serializer_class = DocumentSerializer
    name = 'document-detail'

class DocumentTypeDetail(RetrieveUpdateDestroyAPIView):
    model = Document 
    serializer_class = DocumentTypeSerializer
    name = 'document_type-detail'
