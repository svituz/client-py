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
    diet = "diet"
    # Flags related to the subject's medications.
    drug = "drug"
    # Flags related to performing laboratory tests and related processes (e.g. phlebotomy).
    lab = "lab"
    # Flags related to administrative and financial processes.
    admin = "admin"
    # Flags related to coming into contact with the patient.
    contact = "contact"
    # Flags related to the subject's clinical data.
    clinical = "clinical"
    # Flags related to behavior.
    behavioral = "behavioral"
    # Flags related to research.
    research = "research"
    # Flags related to subject's advance directives.
    advanceDirective = "advance-directive"
    # Flags related to safety precautions.
    safety = "safety"