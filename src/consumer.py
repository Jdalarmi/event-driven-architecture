from kafka import KafkaConsumer
import json

class Consumer:
    def __init__(self, topic, kafka_broker='localhost:9092'):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=kafka_broker,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda v: json.loads(v.decode('utf-8'))
        )

    def consume(self):
        for message in self.consumer:
            print(f"Received message: {message.value}")