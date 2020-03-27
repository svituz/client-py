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

class ReferenceVersionRules(object):
    """ Whether a reference needs to be version specific or version independent, or whether either can be used.
    URL: http://hl7.org/fhir/reference-version-rules
    ValueSet: http://hl7.org/fhir/ValueSet/reference-version-rules
    """
    # The reference may be either version independent or version specific.
    either = "either"
    # The reference must be version independent.
    independent = "independent"
    # The reference must be version specific.
    specific = "specific"