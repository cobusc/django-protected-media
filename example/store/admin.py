# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html

from . import models


class FileCollectionAdmin(admin.ModelAdmin):
    list_display = ["id",
        "public_file", "protected_file",
        "public_file_link", "protected_file_link"
    ]

    def public_file_link(self, obj):
        return format_html("<a href='{}'>{}</a>".format(
            obj.public_file.url, obj.public_file.name
        ))

    def protected_file_link(self, obj):
        return format_html("<a href='{}'>{}</a>".format(
            obj.protected_file.url, obj.protected_file.name
        ))

admin.site.register(models.FileCollection, FileCollectionAdmin)
