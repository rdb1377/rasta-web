from django.core.exceptions import ValidationError
from django.test import TestCase
from django.core.files import File
from PIL import Image
from io import BytesIO
from apps.events.models import Event, EventPhoto, Document
from os import urandom


class UtilsTest(TestCase):
    @staticmethod
    def get_image_file(name, ext='png', size=(50, 50)):
        file_obj = BytesIO()
        Image.frombytes('L', size, urandom(size[0] * size[1])).save(file_obj, format=ext, quality=100)
        file_obj.seek(0)
        return File(file_obj, name=name)

    @staticmethod
    def get_document(name, ext='txt', size=1024):
        file_obj = BytesIO()
        file_obj.write(bytearray(size))
        return File(file_obj, name=name + '.' + ext)

    @classmethod
    def setUpTestData(cls):
        Event.objects.create(name='test event', poster=cls.get_image_file(name='poster', size=(200, 100)),
                             summary='a brief description of test event',
                             description='a detailed story of event so that everyone gets it correctly',
                             location='Tehran', date='2020-4-21')

    def test_invalid_file_size(self):
        invalid_doc = Document.objects.create(file=self.get_document(name='InvalidFile', size=12 * 1024 * 1024),
                                              caption='This file is too big for uploading.',
                                              event=Event.objects.get(id=1))
        self.assertRaises(ValidationError, invalid_doc.full_clean)

    def test_valid_file_size(self):
        valid_doc = Document.objects.create(file=self.get_document(name='ValidFile', size=10 * 1024 * 1024),
                                            caption='This file should be successfully uploaded',
                                            event=Event.objects.get(id=1))
        try:
            valid_doc.full_clean()
        except ValidationError:
            self.fail()

    def test_invalid_image_size(self):
        invalid_img = EventPhoto.objects.create(photo=self.get_image_file(name='InvalidImg', size=(3 * 1024, 2 * 1024)),
                                                caption='This image is too big for uploading.',
                                                event=Event.objects.get(id=1))
        self.assertRaises(ValidationError, invalid_img.full_clean)

    def test_valid_image_size(self):
        valid_img = EventPhoto.objects.create(photo=self.get_image_file(name='InvalidImg', size=(2 * 1024, 2 * 1024)),
                                              caption='This image should be successfully uploaded.',
                                              event=Event.objects.get(id=1))
        try:
            valid_img.full_clean()
        except ValidationError:
            self.fail()

    def test_doc_downloader(self):
        doc = Document.objects.create(file=self.get_document(name='test_doc', size=1024 * 1024),
                                      caption='This file should be successfully uploaded and downloaded',
                                      event=Event.objects.get(id=1))

        response = self.client.post('/download/', HTTP_USER_AGENT='test_download.com',
                                    data={'original_file_name': doc.file.name})
        self.assertEqual(response.status_code, 200)
