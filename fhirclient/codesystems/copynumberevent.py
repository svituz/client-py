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

class CopyNumberEvent(object):
    """ Copy Number Event.
    URL: http://terminology.hl7.org/CodeSystem/copy-number-event
    ValueSet: http://hl7.org/fhir/ValueSet/copy-number-event
    """
    # amplification.
    AMP = "amp"
    # deletion.
    DEL = "del"
    # loss of function.
    LOF = "lof"

    allowed_values = [AMP, DEL, LOF]