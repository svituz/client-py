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

class MediaModality(object):
    """ Detailed information about the type of the image - its kind, purpose, or the kind of equipment used to generate it.
    URL: http://terminology.hl7.org/CodeSystem/media-modality
    """
    # A diagram. Often used in diagnostic reports
    DIAGRAM = "diagram"
    # A digital record of a fax document
    FAX = "fax"
    # A digital scan of a document. This is reserved for when there is not enough metadata to create a document
    # reference
    SCAN = "scan"
    # A retinal image used for identification purposes
    RETINA = "retina"
    # A finger print scan used for identification purposes
    FINGERPRINT = "fingerprint"
    # An iris scan used for identification purposes
    IRIS = "iris"
    # A palm scan used for identification purposes
    PALM = "palm"
    # A face scan used for identification purposes
    FACE = "face"

    allowed_values = [DIAGRAM, FAX, SCAN, RETINA, FINGERPRINT, IRIS, PALM, FACE]