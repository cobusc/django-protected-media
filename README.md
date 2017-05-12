![Build Status](https://www.travis-ci.org/cobusc/protected-media-prototype.svg?branch=master)

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

1. Add "protected_media" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'protected_media',
    ]

2. Include the URLconf in your project urls.py like this::

    url(r'^protected/', include('protected_media.urls')),

3. Add the following settings to `settings.py`:

    TODO


