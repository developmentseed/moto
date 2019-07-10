import sure  # noqa
import boto3
from moto import mock_sqs

def test_reset_api():
    with mock_sqs() as sqs_mock:
        conn = boto3.client("sqs", region_name='us-west-1')
        conn.create_queue(QueueName="queue1")

        list(sqs_mock.backends['us-west-1'].queues.keys()).should.equal(['queue1'])