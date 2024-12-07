from kafka import KafkaProducer
import json

class Producer:
    def __init__(self, kakfa_broker='localhost:9092'):
        self.producer = KafkaProducer(
            bootstrap_servers=kakfa_broker,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send_event(self, topic, event):
        self.producer.send(topic, value=event)
        self.producer.flush()