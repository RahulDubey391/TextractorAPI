from .storeCon import StorageConnection
from ..config.config import Config

class Cleaner:
    def cleanup_files(self):
        store = StorageConnection()
        bucket = store.get_con(Config.UPLOAD_BUCKET_NAME)
        blobs = bucket.list_blobs()
        for blob in blobs:
            blob.delete()
        print('BUCKET CLEANED!!')