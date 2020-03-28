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

class FlagCategory(object):
    """ Example list of general categories for flagged issues. (Not complete or necessarily appropriate.)
    URL: http://terminology.hl7.org/CodeSystem/flag-category
    ValueSet: http://hl7.org/fhir/ValueSet/flag-category
    """
    # Flags related to the subject's dietary needs.
    DIET = "diet"
    # Flags related to the subject's medications.
    DRUG = "drug"
    # Flags related to performing laboratory tests and related processes (e.g. phlebotomy).
    LAB = "lab"
    # Flags related to administrative and financial processes.
    ADMIN = "admin"
    # Flags related to coming into contact with the patient.
    CONTACT = "contact"
    # Flags related to the subject's clinical data.
    CLINICAL = "clinical"
    # Flags related to behavior.
    BEHAVIORAL = "behavioral"
    # Flags related to research.
    RESEARCH = "research"
    # Flags related to subject's advance directives.
    ADVANCEDIRECTIVE = "advance-directive"
    # Flags related to safety precautions.
    SAFETY = "safety"

    allowed_values = [DIET, DRUG, LAB, ADMIN, CONTACT, CLINICAL, BEHAVIORAL, RESEARCH, ADVANCEDIRECTIVE, SAFETY]