import docx
import json
import pandas

class DataReader:
    def __init__(self,Document):
        self.doc = Document

    def docx_reader(self):
        """
            Reading Docx files from the file-system, and return results as json.
        """
        path = self.doc.Document_file
        docx_file = docx.Document(path)
        text_str=''
        for para in docx_file.paragraphs:
            text_str +=para.text
        
        document = {'title':self.doc.Name,'content':text_str}
        document = json.dumps(document)
        return document
        
    def xlsx_reader(self):
        path = self.doc.Document_file
        xlsx_file = self.doc.Document_file
        xlsx_file = pandas.read_excel(xlsx_file)
        xlsx = {'title':self.doc.Name,'content':xlsx_file.to_json()}
        xlsx = json.dumps(xlsx)
        return xlsx