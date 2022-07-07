from django.urls import re_path

from protected_media.views import protected_view
from .settings import PROTECTED_MEDIA_SERVER, PROTECTED_MEDIA_AS_DOWNLOADS

urlpatterns = [
    re_path(
        r"^(?P<path>.*)$", protected_view, {
            "server": PROTECTED_MEDIA_SERVER,
            "as_download": PROTECTED_MEDIA_AS_DOWNLOADS
        }
    ),
]