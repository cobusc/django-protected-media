from django.conf.urls import url

from protected_media.views import protected_view

urlpatterns = [
    url(
        r"^(?P<path>.*)$", protected_view, {"server": "nginx"}
    ),
]