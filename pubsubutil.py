from google.cloud import pubsub_v1
import time


class PubsubUtil():

    def publish_messages(self, project_id, topic_name, orderNumber):
        """Publishes multiple messages with custom attributes
        to a Pub/Sub topic."""

        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(project_id, topic_name)

        data = u'Message: {}'.format('test')
        # Data must be a bytestring
        data = data.encode('utf-8')
        # Add attribute to the message
        future = publisher.publish(
            topic_path, data, OrderNumber=orderNumber)
        print(future.result())

        print('Published messages with custom attributes.')

    def publish_messages_with_error_handler(self, project_id, topic_name, orderNumber):

        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(project_id, topic_name)

        futures = dict()

        def get_callback(f, data):
            def callback(f):
                try:
                    print(f.result())
                    futures.pop(data)
                except:
                    print("Please handle {} for {}.".format(f.exception(), data))
            return callback

        data = u'Message: {}'.format('test')
        # Data must be a bytestring
        data = data.encode('utf-8')
        # Add attribute to the message
        future = publisher.publish(
            topic_path, data, OrderNumber=orderNumber)
        print(future.result())
        futures[data] = future
        # Publish failures shall be handled in the callback function.
        future.add_done_callback(get_callback(future, data))

        # Wait for all the publish futures to resolve before exiting.
        while futures:
            time.sleep(5)

        print("Published message with error handler.")
