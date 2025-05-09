import json
import logging

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from aichannels.models import ClassificationEvent

logger = logging.getLogger(__name__)

@database_sync_to_async
def save_classification_event(source, classification, model_name=None):
    event = ClassificationEvent(
        source=source,
        classification=classification,
        model_name=model_name,
    )
    event.save()


class ClassificationEventConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.source_id = self.scope["url_route"]["kwargs"]["source_id"]
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        classification = text_data_json["classification"]
        logger.debug(f"Received AI even on {self.source_id}")
        logger.debug(classification)
        await save_classification_event(self.source_id, classification)


