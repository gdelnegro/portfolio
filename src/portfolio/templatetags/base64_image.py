from django import template
from django.conf import settings
from portfolio.models import Image
register = template.Library()


@register.filter('base64_image')
def base64_image(image_id):
    """
    Template tag made as a helper for displaying base64 images.
    Id a image with the given id doesn't exists, the placeholder image wil be returned
    Parameters:
        image_id: the id of the image you want to display
    Usage:
        {% load base64_image %}
        [...]
        <img src="{{ projects.images.all.first.id|base64_image }}">
        [...]
    Return:
        string, data:mime;base64,encoded_string
    """
    try:
        img = Image.objects.get(pk=image_id)
    except Image.DoesNotExist:
        return settings.PLACEHOLDER_B64_STRING
    else:
        return "data:%s;base64,%s" % (img.mimetype, img.image_string)
