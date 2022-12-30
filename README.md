[![Build Status](https://app.travis-ci.com/cobusc/django-protected-media.svg?branch=master)](https://app.travis-ci.com/cobusc/django-protected-media)


Django Protected Media
======================

Django Protected Media is a Django app that manages media that are considered
sensitive in a protected fashion.

Not only does the media get stored in a separate filesystem location, but authorisation
is also required to access it.

The application allows for setups where Django performs the authorisation, but
hands off the serving of the file to a web server, like Nginx.

Quick start
-----------

1. Add "protected_media" to your INSTALLED_APPS setting like this:
```python
INSTALLED_APPS = [
    ...
    'protected_media.apps.ProtectedMediaConfig',
]
```

2. Include the URLconf in your project urls.py like this::
```
path('protected/', include('protected_media.urls')),
```

3. Add the following settings to `settings.py` if the defaults need to be tweaked:
```python
PROTECTED_MEDIA_ROOT = "%s/protected/" % BASE_DIR
PROTECTED_MEDIA_URL = "/protected"
PROTECTED_MEDIA_SERVER = "nginx"  # Defaults to "django"
PROTECTED_MEDIA_LOCATION_PREFIX = "/internal"  # Prefix used in nginx config
PROTECTED_MEDIA_AS_DOWNLOADS = False  # Controls inclusion of a Content-Disposition header
```

4. Use the new field classes in your models:
```python
from protected_media.models import ProtectedImageField, ProtectedFileField

def SomeModel(models.Model):
    document = ProtectedFileField(upload_to="uploads/")
    picture = ProtectedImageField(upload_to="uploads/")
    # Files will be stored under PROTECTED_MEDIA_ROOT + upload_to
```

Overview
--------

Django manages media based on the following definitions:
```python
BASE_DIR = "/some/application/dir/"
MEDIA_ROOT = "%s/media/" % BASE_DIR
MEDIA_URL = "/media/"
```

File- and image fields are typically defined as:
```python
document = models.FileField(upload_to="uploads/")
picture = models.ImageField(upload_to="uploads/")
# Files will be stored under MEDIA_ROOT + upload_to
```

In a typical production environment one would let `nginx` (or some other server) serve the media:
```
# Publicly accessible media
location ^~ /media/ {
    alias /some/application/dir/media
}
```

This works well when the media should be publically accessible. However, if the media should be protected, we need a way for Django to check whether the request for the media should only be allowed for logged in (or more stringent criteria) users.

The `protected_media` application
--------------------------------
The `protected_media` application consists of
* new `settings.py` attributes,
* a customized FileSystemStorage class,
* a custom handler for the protected media URL and
* additional web server configuration if serving via `nginx` or something similar.

Protected media is stored in a different physical location to publically accessible media. The following settings can be specified in `settings.py`:
```python
PROTECTED_MEDIA_ROOT = "/some/application/dir/protected/"
PROTECTED_MEDIA_URL = "/protected"
PROTECTED_MEDIA_SERVER = "nginx"  # Defaults to "django"
PROTECTED_MEDIA_LOCATION_PREFIX = "/internal"  # Prefix used in nginx config
```

When defining a file or image field that needs to be protected, we use one of the
classes provided by the `protected_media` application:
* `ProtectedFileField`
* `ProtectedImageField`

Protected file- and image fields are typically defined as:
```python
document = ProtectedFileField(upload_to="uploads/")
picture = ProtectedImageField(upload_to="uploads/")
# Files will be stored under PROTECTED_MEDIA_ROOT + upload_to
```

These classes have a custom storage backend `ProtectedFileSystemStorage` which mananges the filesystem location and URLs associated with protected media.

When `nginx` is used, the configuration must be updated to look like this:
```
# Publicly accessible media
location /media  {
    alias /some/application/dir/media;
}

# Protected media
location /internal  {
    internal;
    alias /some/application/dir/protected;
}
```

