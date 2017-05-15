# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import mimetypes
import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.static import serve
from os.path import basename

from .utils import server_header
from .settings import PROTECTED_MEDIA_LOCATION_PREFIX, PROTECTED_MEDIA_ROOT


@login_required
def protected_view(request, path, server="django", as_download=False):
    if server != "django":
        mimetype, encoding = mimetypes.guess_type(path)
        response = HttpResponse()
        response["Content-Type"] = mimetype
        if encoding:
            response["Content-Encoding"] = encoding

        if as_download:
            response["Content-Disposition"] = "attachment; filename={}".format(
                basename(path))

        response[server_header(server)] = os.path.join(
            PROTECTED_MEDIA_LOCATION_PREFIX, path
        ).encode("utf8")
    else:
        response = serve(
            request, path, document_root=PROTECTED_MEDIA_ROOT,
            show_indexes=False
        )

    return response
