import os 
from pathlib import Path 
for f in os.listdir():
    #print(os.path.splitext(f))
    if f.endswith('pdf'):
        print(os.path.abspath(f))