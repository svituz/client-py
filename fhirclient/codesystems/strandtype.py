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

class StrandType(object):
    """ Type for strand.
    URL: http://hl7.org/fhir/strand-type
    ValueSet: http://hl7.org/fhir/ValueSet/strand-type
    """
    # Watson strand of reference sequence.
    WATSON = "watson"
    # Crick strand of reference sequence.
    CRICK = "crick"

    allowed_values = [WATSON, CRICK]