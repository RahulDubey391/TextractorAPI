import os
from src import Textraction

def triggerFunction(file,context):
    textractor = Textraction()
    textractor.startExtraction(file,context)