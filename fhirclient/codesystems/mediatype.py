#
#  CodeSystems.py
#  client-py
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.
#
#  THIS HAS BEEN ADAPTED FROM Swift Enums WITHOUT EVER BEING IMPLEMENTED IN
#  Python, FOR DEMONSTRATION PURPOSES ONLY.
#

class MediaType(object):
    """ Codes for high level media categories.
    URL: http://terminology.hl7.org/CodeSystem/media-type
    ValueSet: http://hl7.org/fhir/ValueSet/media-type
    """
    # The media consists of one or more unmoving images, including photographs, computer-generated graphs and charts,
    # and scanned documents
    IMAGE = "image"
    # The media consists of a series of frames that capture a moving image
    VIDEO = "video"
    # The media consists of a sound recording
    AUDIO = "audio"

    allowed_values = [IMAGE, VIDEO, AUDIO]