from django.urls import re_path
from social import consumers
websocket_urlpatterns = [
    re_path(r'ws/test/$', consumers.TestConsumer.as_asgi())
]