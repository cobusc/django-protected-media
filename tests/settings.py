SECRET_KEY = "test"

BASE_DIR = "/tmp"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "/tmp/db.sqlite3"
    }
}

INCLUDED_APPS = [
    "protected_media"
]

PROTECTED_MEDIA_ROOT = "/tmp/protected-media-test/"
PROTECTED_MEDIA_URL = "/myprotectedmedia/"
PROTECTED_MEDIA_SERVER = "django"
PROTECTED_MEDIA_AS_DOWNLOADS = False


MEDIA_ROOT = "/tmp/media-test/"
MEDIA_URL = "/media/"
