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

class ConditionCategoryCodes(object):
    """ Preferred value set for Condition Categories.
    URL: http://terminology.hl7.org/CodeSystem/condition-category
    ValueSet: http://hl7.org/fhir/ValueSet/condition-category
    """
    """An item on a problem list that can be managed over time and can be expressed by a practitioner (e.g. physician,
	/// nurse), patient, or related person."""
    PROBLEMLISTITEM = "problem-list-item"
    """A point in time diagnosis (e.g. from a physician or nurse) in context of an encounter."""
    ENCOUNTERDIAGNOSIS = "encounter-diagnosis"
    allowed_values = ['PROBLEMLISTITEM', 'ENCOUNTERDIAGNOSIS']