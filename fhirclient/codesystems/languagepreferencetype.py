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

class LanguagePreferenceType(object):
    """ This value set defines the set of codes for describing the type or mode of the patient's preferred language.
    URL: http://hl7.org/fhir/language-preference-type
    """
    """The patient prefers to verbally communicate with the associated language."""
    VERBAL = "verbal"
    """The patient prefers to communicate in writing with the associated language."""
    WRITTEN = "written"
    allowed_values = ['VERBAL', 'WRITTEN']