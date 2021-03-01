import docx
import json
def docx_reader(path):
    """
    Reading Docx files from the file-system, and return results as json.
    """
    whole_file = docx.Document(path)
    text_str=''
    for para in whole_file.paragraphs:
        text_str +=para.text
    
    json_text = json.dumps(text_str)
    return json_text

#docx_reader('/home/mohab/Main Folder/Master degree/Research/Tubra/venv+django/testenv/Tubra/media/Design and Construction Supervision of Zalingi.docx')
