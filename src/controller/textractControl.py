from ..utilities import StorageConnection,TextRact,Publisher,Cleaner,FragmentLoader
from ..config.config import Config

class Textraction:
    def __init__(self):
        self._textract_obj = TextRact()
        self._fragLoader = FragmentLoader()
        self._Cleaner = Cleaner()

    def startExtraction(self,file,context):
        print(file)
        
        mime_type = file['contentType']
        batch_size = 2
        
        src_bucket = file['bucket']
        filename = file['name']
        
        gcs_source_uri = f'gs://{src_bucket}/{filename}'
        gcs_destination_uri = f'gs://{Config.DOWNLOAD_BUCKET_NAME}/'

        self._textract_obj.extract_text(gcs_source_uri,gcs_destination_uri,mime_type,batch_size)
        self._fragLoader.load_out_response(Config.DOWNLOAD_BUCKET_NAME)
        self._Cleaner.cleanup_files() 