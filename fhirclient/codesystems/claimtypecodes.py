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

class ClaimTypeCodes(object):
    """ This value set includes Claim Type codes.
    URL: http://terminology.hl7.org/CodeSystem/claim-type
    ValueSet: http://hl7.org/fhir/ValueSet/claim-type
    """
    # Hospital, clinic and typically inpatient claims.
    INSTITUTIONAL = "institutional"
    # Dental, Denture and Hygiene claims.
    ORAL = "oral"
    # Pharmacy claims for goods and services.
    PHARMACY = "pharmacy"
    # Typically, outpatient claims from Physician, Psychological, Chiropractor, Physiotherapy, Speech Pathology,
    # rehabilitative, consulting.
    PROFESSIONAL = "professional"
    # Vision claims for professional services and products such as glasses and contact lenses.
    VISION = "vision"

    allowed_values = [INSTITUTIONAL, ORAL, PHARMACY, PROFESSIONAL, VISION]