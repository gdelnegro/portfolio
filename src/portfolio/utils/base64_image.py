def base64_image(mime, encoded_string):
    """
        Returns a uri data for html image display.
        Usage: base64_image(mimetype, base64_string)
    """
    return "data:%s;base64,%s" % (mime, encoded_string)
