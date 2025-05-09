from django.urls import re_path

from aichannels import consumers

websocket_urlpatterns = [
    # we use the default consumer which saves prediction events to the database
    re_path(r"ws/demo/(?P<source_id>\w+)$", consumers.ClassificationEventConsumer.as_asgi()),
]
