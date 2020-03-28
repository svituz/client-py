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

class ImmunizationEvaluationDoseStatusCodes(object):
    """ The value set to instantiate this attribute should be drawn from a terminologically robust code system that consists of
or contains concepts to support describing the validity of a dose relative to a particular recommended schedule. This
value set is provided as a suggestive example.
    URL: http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status
    ValueSet: http://hl7.org/fhir/ValueSet/immunization-evaluation-dose-status
    """
    # The dose counts toward fulfilling a path to immunity for a patient, providing protection against the target
    # disease.
    VALID = "valid"
    # The dose does not count toward fulfilling a path to immunity for a patient.
    NOTVALID = "notvalid"

    allowed_values = [VALID, NOTVALID]