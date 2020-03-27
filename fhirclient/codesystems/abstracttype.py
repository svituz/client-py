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

class AbstractType(object):
    """ A list of the base types defined by this version of the FHIR specification - types that are defined, but for which only
specializations actually are created.
    URL: http://hl7.org/fhir/abstract-types
    """
    """A place holder that means any kind of data type"""
    TYPE = "Type"
    """A place holder that means any kind of resource"""
    ANY = "Any"
    allowed_values = ['TYPE', 'ANY']