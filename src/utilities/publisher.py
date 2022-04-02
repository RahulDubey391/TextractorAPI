from google.cloud import pubsub_v1
import json

class Publisher:
    def __init__(self,PROJECT_ID,TOPIC_NAME):
        self._PROJECT_ID = PROJECT_ID
        self._TOPIC_NAME = TOPIC_NAME

    def publish_to_topic(self,message):
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(self._PROJECT_ID, self._TOPIC_NAME)        
        message_json = json.dumps({
        'data': {'message': message},
        })
        message = message_json.encode('utf-8')
        
        publish_future = publisher.publish(topic_path, data=message)
        publish_future.result()
        print('MESSAGE PUBLISHED TO THE TOPIC')