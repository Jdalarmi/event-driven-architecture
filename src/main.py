from fastapi import FastAPI
from producer import Producer
from events.event_types import EventTypes


app = FastAPI()
producer = Producer()


@app.post('/v1/send_event/')
async def send_event(event_type: str, payload: dict):
    producer.send_event('events', {'type': event_type, 'payload': payload})
    return {'message': 'Event send successfully'}