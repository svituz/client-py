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

class UnknownContentCode(object):
    """ A code that indicates whether an application accepts unknown elements or extensions when reading resources.
    URL: http://hl7.org/fhir/unknown-content-code
    ValueSet: http://hl7.org/fhir/ValueSet/unknown-content-code
    """
    # The application does not accept either unknown elements or extensions.
    no = "no"
    # The application accepts unknown extensions, but not unknown elements.
    extensions = "extensions"
    # The application accepts unknown elements, but not unknown extensions.
    elements = "elements"
    # The application accepts unknown elements and extensions.
    both = "both"