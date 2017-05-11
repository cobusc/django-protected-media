# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files.storage import FileSystemStorage, abspathu
from django.db import models

from settings import PROTECTED_MEDIA_ROOT, PROTECTED_MEDIA_URL


# Create your models here.
from django.utils.functional import cached_property


class ProtectedFileSystemStorage(FileSystemStorage):
    """
    A class to manage protected files.
    We have to override the methods in the FileSystemStorage class which
    are decorated with cached_property for this class to work as intended.
    """
    def __init__(self, *args, **kwargs):
        super(ProtectedFileSystemStorage, self).__init__(*args, **kwargs)

    @cached_property
    def base_location(self):
        return PROTECTED_MEDIA_ROOT

    @cached_property
    def location(self):
        return abspathu(self.base_location)

    @cached_property
    def base_url(self):
        result = PROTECTED_MEDIA_URL
        if not result.endswith('/'):
            result += '/'
        return result


class ProtectedFileField(models.FileField):
    def __init__(self, **kwargs):
        kwargs["storage"] = ProtectedFileSystemStorage()
        super(ProtectedFileField, self).__init__(**kwargs)


class ProtectedImageField(models.ImageField):
    def __init__(self, **kwargs):
        kwargs["storage"] = ProtectedFileSystemStorage()
        super(ProtectedFileField, self).__init__(**kwargs)
