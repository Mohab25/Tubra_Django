from django.urls import path,re_path
from .views import *

urlpatterns=[
    path('',DocumentList.as_view(),name='document-list'),
    path('word_docs/',WordDocumentList.as_view(),name='ms_word_document-list'),
    path('excel_docs/',ExcelDocumentList.as_view(),name='ms_excel_document-list'),
    path('pdf_docs/',PDFDocumentList.as_view(),name='pdf_document-list'),
    re_path(r'document/(?P<pk>\d+)/$',DocumentDetail.as_view(),name='document-detail'),
    re_path(r'doc_type/(?P<pk>\d+)/$',DocumentTypeDetail.as_view(),name='document_type-detail'),
]