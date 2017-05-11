# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.static import serve

from utils import server_header
from settings import PROTECTED_MEDIA_LOCATION_PREFIX, PROTECTED_MEDIA_ROOT


@login_required
def protected_view(request, path, server="django"):
    if server != "django":
        response = HttpResponse()
        response[server_header(server)] = os.path.join(
            PROTECTED_MEDIA_LOCATION_PREFIX, path
        ).encode("utf8")
    else:
        response = serve(
            request, path, document_root=PROTECTED_MEDIA_ROOT,
            show_indexes=False
        )

    return response
