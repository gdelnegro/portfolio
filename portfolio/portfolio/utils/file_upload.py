import base64
import datetime
import os
from portfolio.models import Image


def image_upload(form_image, filename, pk=None):
    """
    Method created to handle all image uploads.
    And to improve code maintainability
    Attributes:
        form_image: image from the view form
        filename: filename from the view
        pk: primary key, if you want to update
        a previosly uploaded image
    Return:
        if there is no error, returns uploaded image id,
            and an empty dict
        if there is error, returns False and error dict
            with "show" and "error_message" keys. The "show"
            key serves to filter if the error message must
            be displayed to the user (True) or not (False).
            And the "error_message" key has the error message.
    Usage:
        Upload/New image:
            from common.utils.file_upload import image_upload
            image_id, image_error = image_upload(request.FILES['image'], filename)
        Upload/update
            from common.utils.file_upload import image_upload
            image_id, image_error = image_upload(request.FILES['image'], filename, 1)
    """
    if form_image is None:
        error = {'show': False, 'error_message': "Invalid image object"}
        return False, error
    if pk is not None:
        try:
            model = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            error = {'show': True, 'error_message': "Image does not exist"}
            return False, error
    else:
        model = Image()
    if form_image.multiple_chunks():
        error = {'show': True, 'error_message': "Image is bigger than 2.5MB size limit"}
        return False, error
    else:
        try:
            encoded_image = base64.b64encode(form_image.read())
        except Exception:
            error = {"show": False, "error_message": "Error on base64 encode"}
            return False, error
    if encoded_image:
        name, extension = os.path.splitext(form_image.name)
        model.image_string = encoded_image
        model.mimetype = form_image.content_type
        model.extension = extension
        model.title = filename
        model.description = filename
        model.save()

        return model.id, {}
