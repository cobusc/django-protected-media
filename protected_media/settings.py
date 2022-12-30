import os
from django.conf import settings

# Filesystem location to store protected media.
# The default location does not rely on BASE_DIR to be defined anymore.
PROTECTED_MEDIA_ROOT = getattr(
    settings, "PROTECTED_MEDIA_ROOT", "%s/protected/" % os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

# The URL prefix used by protected media
PROTECTED_MEDIA_URL = getattr(
    settings, "PROTECTED_MEDIA_URL", "/protected/"
)

# An alternative prefix to use with servers like Nginx, where we want to
# disambiguate requests routed to Django and internal redirects to serve
# files.
PROTECTED_MEDIA_LOCATION_PREFIX = getattr(
    settings, "PROTECTED_MEDIA_LOCATION_PREFIX", PROTECTED_MEDIA_URL
)

# The server used to server the media. Django will always perform the
# authorisation.
PROTECTED_MEDIA_SERVER = getattr(
    settings, "PROTECTED_MEDIA_SERVER", "django"
)

# Controls whether the protected media are served as downloads. If True, the
# Content-Disposition flag will be set.
PROTECTED_MEDIA_AS_DOWNLOADS = False

