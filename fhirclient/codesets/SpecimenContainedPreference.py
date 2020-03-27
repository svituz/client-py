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

class SpecimenContainedPreference(object):
    """ Degree of preference of a type of conditioned specimen.
    URL: http://hl7.org/fhir/specimen-contained-preference
    ValueSet: http://hl7.org/fhir/ValueSet/specimen-contained-preference
    """
    # This type of contained specimen is preferred to collect this kind of specimen.
    preferred = "preferred"
    # This type of conditioned specimen is an alternate.
    alternate = "alternate"