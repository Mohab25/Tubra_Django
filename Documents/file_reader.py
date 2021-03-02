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
    
    #json_text = json.dumps(text_str)
    return text_str
