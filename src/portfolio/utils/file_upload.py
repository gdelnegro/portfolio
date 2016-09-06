from django.conf import settings
from portfolio.models import Image
from django.utils.translation import ugettext_lazy as _, ugettext_noop as _noop, ugettext
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import os
import re
import base64


def image_upload(form_image, filename, pk=None):
    """
    Method created to handle all image uploads.
    And to improve code maintainability
    Attributes:
        form_image: image from the view form
        filename: filename from the view
        pk: primary key, if you want to update
        a previously uploaded image
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
        error = {'show': False, 'error_message': _('ME26')}
        return False, error
    if pk is not None:
        try:
            model = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            error = {'show': True, 'error_message': _('ME27')}
            return False, error
    else:
        model = Image()
    if form_image.multiple_chunks():
        error = {'show': True, 'error_message': _('ME28')}
        return False, error
    else:
        if "image" in form_image.content_type:
            try:
                encoded_image = base64.b64encode(form_image.read())
            except Exception:
                error = {"show": False, "error_message": _('ME29')}
                return False, error
            else:
                if encoded_image:
                    name, extension = os.path.splitext(form_image.name)
                    model.image_string = encoded_image
                    model.mimetype = form_image.content_type
                    model.extension = extension
                    model.title = filename
                    model.description = filename
                    model.save()

                    return model.id, {}
        else:
            error = {"show": False, "error_message": _('ME29')}
            return False, error

def image_upload_from_url(image_url, filename, pk=None):
    """
    Method created to handle all image uploads.
    And to improve code maintainability
    Attributes:
        image_url: url that contains the image
        filename: the name of the file
        pk: primary key, if you want to update
        a previously uploaded image
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
            image_id, image_error = image_upload_from_url("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", filename)
        Upload/update
            from common.utils.file_upload import image_upload
            image_id, image_error = image_upload("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", filename, 1)
    """
    import urllib.request

    val = URLValidator()
    try:
        val(image_url)
    except ValidationError as e:
        error = {"show": False, "error_message": _('ME29')}
        return False, error
    else:
        try:
            response = urllib.request.urlretrieve(image_url)
        except Exception as error_message:
            error = {"show": False, "error_message": error_message}
            return False, error
        else:
            local_filename = response[0]
            content = response[1]
            os.remove(local_filename)
            mimetype = "%s/%s" % (content.get_content_maintype(), content.get_content_subtype())
            if content.get_content_maintype() != "image":
                error = {"show": False, "error_message": _('ME29')}
                return False, error
            else:
                try:
                    encoded_image = base64.b64encode(urllib.request.urlopen(image_url).read())
                except Exception:
                    error = {"show": False, "error_message": _('ME29')}
                    return False, error
                else:
                    if pk is not None:
                        try:
                            model = Image.objects.get(pk=pk)
                        except Image.DoesNotExist:
                            error = {'show': True, 'error_message': _('ME27')}
                            return False, error
                    else:
                        model = Image()
                    if encoded_image:
                        model.image_string = encoded_image
                        model.mimetype = mimetype
                        model.extension = content.get_content_subtype()
                        model.title = filename
                        model.description = filename
                        model.save()

                        return model.id, {}


def document_upload(file, filename, pk=None):
    """
    Method created to handle all document uploads.
    Attributes:
        file: document from the form
        filename: the filename
        pk: primary key, if you want to update a previously uploaded document
    Return:
        if there is no error, returns uploaded image id,
            and an empty dict
        if there is error, returns False and error dict with "show" and "error_message" keys. The "show"
            key serves to filter if the error message must be displayed to the user (True) or not (False).
            And the "error_message" key has the error message.
    Usage:
        Upload-New document:
            from common.utils.file_upload import document_upload
            document_id, document_error = document_upload(request.FILES['document'], filename)
        Upload-update
            from common.utils.file_upload import document_upload
            document_id, document_error = document_upload(request.FILES['document'], filename, 1)
    """
    if file is None:
        error = {'show': False, 'error_message': _('ME26')}
        return False, error
    if pk is not None:
        try:
            model = Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            error = {'show': True, 'error_message': _('ME27')}
            return False, error
    else:
        model = Document()
    if file.multiple_chunks():
        error = {'show': True, 'error_message': _('ME28')}
        return False, error
    else:
        name, extension = os.path.splitext(file.name)
        document_binary_data = b''
        for chunk in file.chunks():
            document_binary_data += chunk
        # save to temporary file
        # temp_root = os.path.join(settings.STATIC_ROOT, 'temp')
        # temp_url = settings.STATIC_URL + 'temp/'
        # if not os.path.exists(temp_root):
        #     os.makedirs(temp_root)
        # temp_dir = tempfile.mkdtemp(dir=temp_root)
        # file_name = binascii.b2a_hex(os.urandom(15)).decode("utf-8") + extension
        # # Ensure the file is read/write by the creator only
        # saved_umask = os.umask(0o077)
        # path = os.path.join(temp_dir, file_name)
        # print("temp_var", tmp_var)
        # try:
        #     with open(path, "wb") as tmp_file:
        #         for chunk in file.chunks():
        #             tmp_file.write(chunk)
        #     os.umask(saved_umask)
        # except IOError as e:
        #     print('IOError', e)
        #     error = {"show": False, "error_message": e}
        #     return False, error
        # else:
        #     os.remove(path)
        # finally:
        #     os.rmdir(temp_dir)
        if len(document_binary_data) > 0:
            model.document_binary_data = document_binary_data
            model.mimetype = file.content_type
            model.extension = extension
            model.title = filename
            model.description = filename
            model.save()
            return model.id, {}
        else:
            error = {"show": False, "error_message": _('ME29')}
            return False, error


def svg_upload(file, filename, type, pk=None, remove_style=None):
    from common.models import SVGType
    """
    Method created to handle all SVG uploads.
    Attributes:
        @param file: document from the form
        @param filename: the filename
        @param pk: primary key, if you want to update a previously uploaded document
        @param remove_style: remove all style tags from the SVG
        @param type: SVG type, the type of the SVG (icon, diagram, etc) added on 31/08/2016 12:24
    Return:
        @return: if there is no error, returns uploaded image id, and an empty dict
        @return: if there is error, returns False and error dict with "show" and "error_message" keys. The "show"
            key serves to filter if the error message must be displayed to the user (True) or not (False).
            And the "error_message" key has the error message.
    Usage:
        Upload-New document:
            from common.utils.file_upload import document_upload
            document_id, document_error = svg_upload(request.FILES['document'], filename)
        Upload-update
            from common.utils.file_upload import document_upload
            document_id, document_error = svg_upload(request.FILES['document'], filename, 1)
    """
    if file is None:
        error = {'show': False, 'error_message': _('ME26')}
        return False, error
    if pk is not None:
        try:
            model = SVG.objects.get(pk=pk)
        except SVG.DoesNotExist:
            error = {'show': True, 'error_message': _('ME27')}
            return False, error
    else:
        model = SVG()
    if file.multiple_chunks():
        error = {'show': True, 'error_message': _('ME28')}
        return False, error
    else:
        name, extension = os.path.splitext(file.name)
        svg_binary_data = b''
        for chunk in file.chunks():
            svg_binary_data += chunk
        if remove_style:
            svg_binary_data = _remove_style(svg_binary_data)
        # fill = "#ED1C24"
        if len(svg_binary_data) > 0:
            model.svg_binary_data = svg_binary_data
            model.mimetype = file.content_type
            model.extension = extension
            model.title = filename
            model.description = filename
            model.type = SVGType.objects.filter(tag=type)[0] if len(SVGType.objects.filter(tag=type)) > 0 else \
                SVGType.objects.filter(tag="ICON")[0]
            model.save()
            return model.id, {}
        else:
            error = {"show": False, "error_message": _('ME29')}
            return False, error


def _remove_style(svg_binary_data):
    """
    Remove styles applied on SVG based on rules dict
    @param svg_binary_data: binary data
    @return: binary data
    @author Gustavo Del Negro <gustavodelnegro@gmail.com>
    """
    string = svg_binary_data.decode()

    rules = {
        '<style': r'(?s)<style.+?</style>',
        'fill=': r'fill=".+?"',
        'stroke=': r'stroke=".+?"'
    }

    for rule, regex in rules.items():
        if rule in string:
            string = re.sub(regex, '', string)

    svg_binary_data = string.encode()
    return svg_binary_data