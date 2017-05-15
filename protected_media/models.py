# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files.storage import FileSystemStorage
from django.db import models

from .settings import PROTECTED_MEDIA_ROOT, PROTECTED_MEDIA_URL


class ProtectedFileSystemStorage(FileSystemStorage):
    """
    A class to manage protected files.
    We have to override the methods in the FileSystemStorage class which
    are decorated with cached_property for this class to work as intended.
    """
    def __init__(self, *args, **kwargs):
        kwargs["location"] = PROTECTED_MEDIA_ROOT
        kwargs["base_url"] = PROTECTED_MEDIA_URL
        super(ProtectedFileSystemStorage, self).__init__(*args, **kwargs)


class ProtectedFileField(models.FileField):
    def __init__(self, **kwargs):
        kwargs["storage"] = ProtectedFileSystemStorage()
        super(ProtectedFileField, self).__init__(**kwargs)


class ProtectedImageField(models.ImageField):
    def __init__(self, **kwargs):
        kwargs["storage"] = ProtectedFileSystemStorage()
        super(ProtectedImageField, self).__init__(**kwargs)
