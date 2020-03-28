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

class PractitionerSpecialty(object):
    """ This example value set defines a set of codes that can be used to indicate the specialty of a Practitioner.
    URL: http://hl7.org/fhir/practitioner-specialty
    ValueSet: http://hl7.org/fhir/ValueSet/practitioner-specialty
    """
    # cardio
    CARDIO = "cardio"
    # dent
    DENT = "dent"
    # dietary
    DIETARY = "dietary"
    # midw
    MIDW = "midw"
    # sysarch
    SYSARCH = "sysarch"

    allowed_values = [CARDIO, DENT, DIETARY, MIDW, SYSARCH]