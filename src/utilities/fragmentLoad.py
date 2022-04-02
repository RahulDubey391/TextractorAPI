from src.utilities.storeCon import StorageConnection
from ..config.config import Config
from .storeCon import StorageConnection
from .publisher import Publisher
import json

class FragmentLoader:
    def load_out_response(self,dest_bucket):
        store = StorageConnection()
        bucket = store.get_con(Config.UPLOAD_BUCKET_NAME)
        blobs = bucket.list_blobs()
        for blob in blobs:
            json_string = blob.download_as_string()
            json_response = json.loads(json_string)
            
            file_meta = {}
            file_meta['filename'] = json_response['inputConfig']['gcsSource']['uri'].split('/')[-1]
            file_meta['uri'] = json_response['inputConfig']['gcsSource']['uri']
            file_meta['mimeType'] = json_response['inputConfig']['mimeType']
            file_meta['pages'] = {} 
            for i,res in enumerate(json_response['responses']):
                file_meta['pages'][i] = res['fullTextAnnotation']['text']
            print(file_meta)
            publisher = Publisher(Config.PROJECT_ID,Config.TRANSLATE_TOPIC)
            publisher.publish_to_topic(file_meta)