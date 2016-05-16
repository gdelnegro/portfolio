from django import template
import base64
from base64 import decodestring
from django.template.loader_tags import do_include
from django.template.defaulttags import CommentNode
register = template.Library()

@register.filter('base64_image')
def base64_image(mime,encoded_string):
    # decoded_string = decodestring(encoded_string)
    # print(mime,encoded_string)
    # decoded_string = base64.b64encode(encoded_string)
    return "data:%s;base64,%s" % (mime,encoded_string)
