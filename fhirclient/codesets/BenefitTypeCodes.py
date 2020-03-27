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
    # Maximum benefit allowable.
    benefit = "benefit"
    # Cost to be incurred before benefits are applied
    deductible = "deductible"
    # Service visit
    visit = "visit"
    # Type of room
    room = "room"
    # Copayment per service
    copay = "copay"
    # Copayment percentage per service
    copayPercent = "copay-percent"
    # Copayment maximum per service
    copayMaximum = "copay-maximum"
    # Vision Exam
    visionExam = "vision-exam"
    # Frames and lenses
    visionGlasses = "vision-glasses"
    # Contact Lenses
    visionContacts = "vision-contacts"
    # Medical Primary Health Coverage
    medicalPrimarycare = "medical-primarycare"
    # Pharmacy Dispense Coverage
    pharmacyDispense = "pharmacy-dispense"