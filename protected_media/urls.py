from django.conf.urls import url

from protected_media.views import protected_view
from .settings import PROTECTED_MEDIA_SERVER, PROTECTED_MEDIA_AS_DOWNLOADS

urlpatterns = [
    url(
        r"^(?P<path>.*)$", protected_view, {
            "server": PROTECTED_MEDIA_SERVER,
            "as_download": PROTECTED_MEDIA_AS_DOWNLOADS
        }
    ),
]