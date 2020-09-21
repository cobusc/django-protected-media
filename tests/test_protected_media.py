import django
django.setup()

from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models import Model, FileField, ImageField
from django.test import TestCase

from protected_media.models import ProtectedFileField, ProtectedImageField


class SomeModel(Model):
    protected_file = ProtectedFileField()
    protected_image = ProtectedImageField()
    public_file = FileField()
    public_image = ImageField()

    class Meta:
        app_label = "test"


class TestProtectedMedia(TestCase):

    def test_protected_media(self):
        m = SomeModel()
        m.protected_file = SimpleUploadedFile(
            "protected_file.txt", b"A test file"
        )
        m.protected_image = SimpleUploadedFile(
            "protected_image.png", b"A test image"
        )
        m.public_file = SimpleUploadedFile(
            "public_file.txt", b"A test file"
        )
        m.public_image = SimpleUploadedFile(
            "public_image.png", b"A test image"
        )

        self.assertEqual(m.protected_file.name, "protected_file.txt")
        self.assertEqual(m.protected_file.url,
                         "/myprotectedmedia/protected_file.txt")
        self.assertEqual(m.protected_image.name, "protected_image.png")
        self.assertEqual(m.protected_image.url,
                         "/myprotectedmedia/protected_image.png")

        self.assertEqual(m.public_file.name, "public_file.txt")
        self.assertEqual(m.public_file.url, "/media/public_file.txt")

        self.assertEqual(m.public_image.name, "public_image.png")
        self.assertEqual(m.public_image.url, "/media/public_image.png")
