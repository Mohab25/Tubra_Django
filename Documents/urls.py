from django.urls import path,re_path
from .views import *
from .obeid_views import *

urlpatterns=[
    path('',DocumentList.as_view(),name='document-list'),
    path('word_docs/',WordDocumentList.as_view(),name='ms_word_document-list'),
    path('excel_docs/',ExcelDocumentList.as_view(),name='ms_excel_document-list'),
    path('pdf_docs/',PDFDocumentList.as_view(),name='pdf_document-list'),
    re_path(r'document/(?P<pk>\d+)/$',DocumentDetail.as_view(),name='document-detail'),
    re_path(r'doc_type/(?P<pk>\d+)/$',DocumentTypeDetail.as_view(),name='document_type-detail'),
    re_path(r'doc_content/(?P<pk>\d+)/$',doc_content,name='document-content'),
    path('obeid_runway_all_files/',ObeidAllRunwayDocsList.as_view(),name='obeid_all_runway_docs-list'),
    path('obeid_runway_pdf/',ObeidRunwayPDFDocsList.as_view(),name='obeid_runway_pdf_docs-list'),
    path('obeid_runway_word/',ObeidRunwayWordDocsList.as_view(),name='obeid_runway_word_docs-list'),
    path('obeid_runway_excel/',ObeidRunwayExcelDocsList.as_view(),name='obeid_runway_excel_docs-list'),
    path('obeid_taxiway_all_files/',ObeidAllTaxiwayDocsList.as_view(),name='obeid_all_taxiway_docs-list'),
    path('obeid_taxiway_pdf/',ObeidTaxiwayPDFDocsList.as_view(),name='obeid_taxiway_pdf_docs-list'),
    path('obeid_taxiway_word/',ObeidTaxiwayWordDocsList.as_view(),name='obeid_taxiway_word_docs-list'),
    path('obeid_taxiway_excel/',ObeidTaxiwayExcelDocsList.as_view(),name='obeid_taxiway_excel_docs-list'),
    path('obeid_apron_all_files/',ObeidAllApronDocsList.as_view(),name='obeid_all_Apron_docs-list'),
    path('obeid_apron_pdf/',ObeidApronPDFDocsList.as_view(),name='obeid_apron_pdf_docs-list'),
    path('obeid_apron_word/',ObeidApronWordDocsList.as_view(),name='obeid_apron_word_docs-list'),
    path('obeid_apron_excel/',ObeidApronExcelDocsList.as_view(),name='obeid_apron_excel_docs-list'),
    path('obeid_general_all_files/',ObeidGeneralPDFDocsList.as_view(),name='obeid_all_general_docs-list'),
    path('obeid_general_pdf/',ObeidGeneralPDFDocsList.as_view(),name='obeid_general_pdf_docs-list'),
    path('obeid_general_word/',ObeidGeneralWordDocsList.as_view(),name='obeid_general_word_docs-list'),
    path('obeid_general_excel/',ObeidGeneralExcelDocsList.as_view(),name='obeid_general_excel_docs-list'),
    path('obeid_reports_all_files/',ObeidAllReportsDocsList.as_view(),name='obeid_all_reports_docs-list'),
    path('obeid_reports_pdf/',ObeidReportsPDFDocsList.as_view(),name='obeid_reports_pdf_docs-list'),
    path('obeid_reports_word/',ObeidReportsWordDocsList.as_view(),name='obeid_reports_word_docs-list'),
    path('obeid_reports_excel/',ObeidReportsExcelDocsList.as_view(),name='obeid_reports_excel_docs-list'),

]