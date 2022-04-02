from google.cloud.vision import ImageAnnotatorClient, Feature, GcsSource, InputConfig, OutputConfig, GcsDestination, AsyncAnnotateFileRequest

class TextRact:
    def __init__(self,GCS_SRC_URI,GCS_DEST_URI,MIME_TYPE,BATCH_SIZE):
        self._GCS_SRC_URI = GCS_SRC_URI
        self._GCS_DEST_URI = GCS_DEST_URI
        self._MIME_TYPE = MIME_TYPE
        self._BATCH_SIZE = BATCH_SIZE

    def extract_text(self):
        client = ImageAnnotatorClient()
        feature = Feature(type_= Feature.Type.DOCUMENT_TEXT_DETECTION)
        
        gcs_source = GcsSource(uri=self._GCS_SRC_URI)
        input_config = InputConfig(gcs_source=self._GCS_SRC_URI, mime_type=self._MIME_TYPE)

        gcs_destination = GcsDestination(uri=self._GCS_DEST_URI)
        output_config = OutputConfig(gcs_destination=gcs_destination, batch_size=self._BATCH_SIZE)

        async_request = AsyncAnnotateFileRequest(features=[feature], input_config=input_config,output_config=output_config)
        operation = client.async_batch_annotate_files(requests=[async_request])

        print('Waiting for the operation to finish.')
        operation.result()    
