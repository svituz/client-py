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

class CoverageCopayTypeCodes(object):
    """ This value set includes sample Coverage Copayment Type codes.
    URL: http://terminology.hl7.org/CodeSystem/coverage-copay-type
    ValueSet: http://hl7.org/fhir/ValueSet/coverage-copay-type
    """
    # An office visit for a general practitioner of a discipline.
    gpvisit = "gpvisit"
    # An office visit for a specialist practitioner of a discipline
    spvisit = "spvisit"
    # An episode in an emergency department.
    emergency = "emergency"
    # An episode of an Inpatient hospital stay.
    inpthosp = "inpthosp"
    # A visit held where the patient is remote relative to the practitioner, e.g. by phone, computer or video
	/// conference.
    televisit = "televisit"
    # A visit to an urgent care facility - typically a community care clinic.
    urgentcare = "urgentcare"
    # A standard percentage applied to all classes or service or product not otherwise specified.
    copaypct = "copaypct"
    # A standard fixed currency amount applied to all classes or service or product not otherwise specified.
    copay = "copay"
    # The accumulated amount of patient payment before the coverage begins to pay for services.
    deductible = "deductible"
    # The maximum amout of payment for services which a patient, or family, is expected to incur - typically annually.
    maxoutofpocket = "maxoutofpocket"