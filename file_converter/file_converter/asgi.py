import os
import django
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_converter.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
})
