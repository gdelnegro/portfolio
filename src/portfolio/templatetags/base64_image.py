from django import template
register = template.Library()


@register.filter('base64_image')
def base64_image(mime, encoded_string):
    """
    Template tag made as a helper for displaying
    base64 images.
    Parameters:
        mime: image mime type
        enconded_string:  image base64 string
    Usage:
        {% load base64_image %}
        [...]
        <img src="{{ user.userextend.photo.mimetype|base64_image:user.userextend.photo.image_string }}">
        [...]
    Return:
        string, data:mime;base64,encoded_string
    """
    return "data:%s;base64,%s" % (mime, encoded_string)
