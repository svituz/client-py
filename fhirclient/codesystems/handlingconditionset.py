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

class HandlingConditionSet(object):
    """ Set of handling instructions prior testing of the specimen.
    URL: http://terminology.hl7.org/CodeSystem/handling-condition
    ValueSet: http://hl7.org/fhir/ValueSet/handling-condition
    """
    """room temperature."""
    ROOM = "room"
    """refrigerated temperature."""
    REFRIGERATED = "refrigerated"
    """frozen temperature."""
    FROZEN = "frozen"
    allowed_values = ['ROOM', 'REFRIGERATED', 'FROZEN']