from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from .file_reader import DataReader
import json
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
    def get_queryset(self):
        title = self.request.query_params.get('title')
        title = title.strip('/')
        if title != '':
            queryset = Document.objects.filter(Name__istartswith=title)
            return queryset
        else:
            pass

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
    queryset = Document.objects.all() 
    serializer_class = DocumentSerializer
    name = 'document-detail'

class DocumentTypeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Document_Type.objects.all()
    serializer_class = DocumentTypeSerializer
    name = 'document_type-detail'

def doc_content(request,pk):
    """
        the view reads through the file and returns the actual content, 
        according to the file type a specific reader is applied.
    """
    _file = Document.objects.get(id=pk)
    content = DataReader(_file)
    doc_type = str(_file.Document_type).lower()
    print(doc_type)
    if doc_type=='word':
        content = content.docx_reader()
    elif doc_type=='excel':
        content = content.xlsx_reader()
    elif doc_type=='pdf':
        content = content.pdf_reader()
    return HttpResponse(content)
