from django.test import TestCase
from portfolio.utils.file_upload import image_upload, image_upload_from_url
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.

class ImageUpload(TestCase):

    def test_image_upload_from_empty_url(self):
        image_id, error = image_upload_from_url(image_url="", filename="url_test", pk=None)
        self.assertEqual(image_id, False)
        self.assertEqual(type(error), dict)

    def test_image_upload_from_invalid_url(self):
        image_id, error = image_upload_from_url(image_url="http://guuugle.com.br", filename="url_test", pk=None)
        self.assertEqual(image_id, False)
        self.assertEqual(type(error), dict)

    def test_image_upload_from_not_image_url(self):
        image_id, error = image_upload_from_url(image_url="https://www.google.com.br/?gws_rd=ssl", filename="url_test", pk=None)
        self.assertEqual(image_id, False)
        self.assertEqual(type(error), dict)

    def test_image_upload_from_image_url(self):
        img_url = "http://www.ford.pt/cs/BlobServer?blobtable=MungoBlobs&blobcol=urldata&blobheader=image%2Fjpeg&blobwhere=1214517273105&blobkey=id"
        image_id, error = image_upload_from_url(image_url=img_url, filename="url_test", pk=None)
        self.assertEqual(type(image_id), int)
        self.assertEqual(len(error), 0)

    def test_image_upload_from_image_url_with_id(self):
        img_url = "http://www.ford.pt/cs/BlobServer?blobtable=MungoBlobs&blobcol=urldata&blobheader=image%2Fjpeg&blobwhere=1214517273105&blobkey=id"
        image_id, error = image_upload_from_url(image_url=img_url, filename="url_test", pk=None)
        image_id, error = image_upload_from_url(image_url=img_url, filename="url_test", pk=image_id)
        self.assertEqual(type(image_id), int)
        self.assertEqual(len(error), 0)

    def test_image_upload_file_is_empty(self):
        image_id, error = image_upload(form_image=None, filename="test", pk=None)
        self.assertEqual(image_id, False)
        self.assertEqual(type(error), dict)

    def test_image_upload_file_type_is_not_image(self):
        file_path = "/home/gdelnegro/projects/test/requirements.txt"
        with open(file_path, 'rb') as open_file:
            file = SimpleUploadedFile(open_file.name, open_file.read(), content_type="text/plain")
            image_id, error = image_upload(form_image=file, filename="test", pk=None)
            self.assertEqual(image_id, False)
            self.assertEqual(type(error), dict)

    # def test_image_upload_file_type_is_image(self):
    #     """If file type is not image, return error"""
    #     image_id, error = image_upload(form_image=None, filename="test", pk=None)
    #     self.assertEqual(image_id, False)
    #     self.assertEqual(type(error), dict)