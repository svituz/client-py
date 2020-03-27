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

class BenefitTypeCodes(object):
    """ This value set includes a smattering of Benefit type codes.
    URL: http://terminology.hl7.org/CodeSystem/benefit-type
    ValueSet: http://hl7.org/fhir/ValueSet/benefit-type
    """
    """Maximum benefit allowable."""
    BENEFIT = "benefit"
    """Cost to be incurred before benefits are applied"""
    DEDUCTIBLE = "deductible"
    """Service visit"""
    VISIT = "visit"
    """Type of room"""
    ROOM = "room"
    """Copayment per service"""
    COPAY = "copay"
    """Copayment percentage per service"""
    COPAYPERCENT = "copay-percent"
    """Copayment maximum per service"""
    COPAYMAXIMUM = "copay-maximum"
    """Vision Exam"""
    VISIONEXAM = "vision-exam"
    """Frames and lenses"""
    VISIONGLASSES = "vision-glasses"
    """Contact Lenses"""
    VISIONCONTACTS = "vision-contacts"
    """Medical Primary Health Coverage"""
    MEDICALPRIMARYCARE = "medical-primarycare"
    """Pharmacy Dispense Coverage"""
    PHARMACYDISPENSE = "pharmacy-dispense"
    allowed_values = ['BENEFIT', 'DEDUCTIBLE', 'VISIT', 'ROOM', 'COPAY', 'COPAYPERCENT', 'COPAYMAXIMUM', 'VISIONEXAM', 'VISIONGLASSES', 'VISIONCONTACTS', 'MEDICALPRIMARYCARE', 'PHARMACYDISPENSE']