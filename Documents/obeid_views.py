from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from .file_reader import DataReader
import json

class ObeidRunwayPDFDocsList(ListCreateAPIView):
    queryset = Document.objects.filter(aerodrome_part__Name__iexact='runway',Document_type__Doc_type__iexact='pdf')
    serializer_class = ObeidDocumentsSerializer
    name='obeid_runway_pdf_docs-list'

class ObeidRunwayWordDocsList(ListCreateAPIView):
    queryset = Document.objects.filter(aerodrome_part__Name__iexact='runway',Document_type__Doc_type__iexact='word')
    serializer_class = ObeidDocumentsSerializer
    name='obeid_runway_word_docs-list'

class ObeidRunwayExcelDocsList(ListCreateAPIView):
    queryset = Document.objects.filter(aerodrome_part__Name__iexact='runway',Document_type__Doc_type__iexact='excel')
    serializer_class = ObeidDocumentsSerializer
    name='obeid_runway_excel_docs-list'

class ObeidTaxiwayPDFDocsList(ListCreateAPIView):
    queryset = Document.objects.filter(aerodrome_part__Name__iexact='taxiway',Document_type__Doc_type__iexact='pdf')
    serializer_class = ObeidDocumentsSerializer
    name='obeid_taxiway_pdf_docs-list'

class ObeidTaxiwayWordDocsList(ListCreateAPIView):
    queryset = Document.objects.filter(aerodrome_part__Name__iexact='taxiway',Document_type__Doc_type__iexact='word')
    serializer_class = ObeidDocumentsSerializer
    name='obeid_taxiway_word_docs-list'

class ObeidTaxiwayExcelDocsList(ListCreateAPIView):
    queryset = Document.objects.filter(aerodrome_part__Name__iexact='taxiway',Document_type__Doc_type__iexact='excel')
    serializer_class = ObeidDocumentsSerializer
    name='obeid_taxiway_excel_docs-list'


class ObeidApronPDFDocsList(ListCreateAPIView):
    queryset = Document.objects.filter(aerodrome_part__Name__iexact='apron',Document_type__Doc_type__iexact='pdf')
    serializer_class = ObeidDocumentsSerializer
    name='obeid_apron_pdf_docs-list'

class ObeidApronWordDocsList(ListCreateAPIView):
    queryset = Document.objects.filter(aerodrome_part__Name__iexact='apron',Document_type__Doc_type__iexact='word')
    serializer_class = ObeidDocumentsSerializer
    name='obeid_apron_word_docs-list'

class ObeidApronExcelDocsList(ListCreateAPIView):
    queryset = Document.objects.filter(aerodrome_part__Name__iexact='apron',Document_type__Doc_type__iexact='excel')
    serializer_class = ObeidDocumentsSerializer
    name='obeid_apron_excel_docs-list'


class ObeidGeneralPDFDocsList(ListCreateAPIView):
    queryset = Document.objects.filter(aerodrome_part__Name__iexact='general',Document_type__Doc_type__iexact='pdf')
    serializer_class = ObeidDocumentsSerializer
    name='obeid_general_pdf_docs-list'

class ObeidGeneralWordDocsList(ListCreateAPIView):
    queryset = Document.objects.filter(aerodrome_part__Name__iexact='general',Document_type__Doc_type__iexact='word')
    serializer_class = ObeidDocumentsSerializer
    name='obeid_general_word_docs-list'

class ObeidGeneralExcelDocsList(ListCreateAPIView):
    queryset = Document.objects.filter(aerodrome_part__Name__iexact='general',Document_type__Doc_type__iexact='excel')
    serializer_class = ObeidDocumentsSerializer
    name='obeid_general_excel_docs-list'


class ObeidReportsPDFDocsList(ListCreateAPIView):
    queryset = Document.objects.filter(aerodrome_part__Name__iexact='report',Document_type__Doc_type__iexact='pdf')
    serializer_class = ObeidDocumentsSerializer
    name='obeid_reports_pdf_docs-list'

class ObeidReportsWordDocsList(ListCreateAPIView):
    queryset = Document.objects.filter(aerodrome_part__Name__iexact='report',Document_type__Doc_type__iexact='word')
    serializer_class = ObeidDocumentsSerializer
    name='obeid_reports_word_docs-list'

class ObeidReportsExcelDocsList(ListCreateAPIView):
    queryset = Document.objects.filter(aerodrome_part__Name__iexact='report',Document_type__Doc_type__iexact='excel')
    serializer_class = ObeidDocumentsSerializer
    name='obeid_reports_excel_docs-list'