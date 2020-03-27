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

class SpecimenStatus(object):
    """ Codes providing the status/availability of a specimen.
    URL: http://hl7.org/fhir/specimen-status
    ValueSet: http://hl7.org/fhir/ValueSet/specimen-status
    """
    # The physical specimen is present and in good condition.
    available = "available"
    # There is no physical specimen because it is either lost, destroyed or consumed.
    unavailable = "unavailable"
    # The specimen cannot be used because of a quality issue such as a broken container, contamination, or too old.
    unsatisfactory = "unsatisfactory"
    # The specimen was entered in error and therefore nullified.
    enteredInError = "entered-in-error"