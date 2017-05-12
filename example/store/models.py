# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from protected_media.models import ProtectedFileField


class FileCollection(models.Model):
    public_file = models.FileField(upload_to="collection")
    protected_file = ProtectedFileField(upload_to="collection")
