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

class ExampleOnsetTypeReasonCodes(object):
    """ This value set includes example Onset Type codes which are used to identify the event for which the onset, starting
date, is required.
    URL: http://hl7.org/fhir/ex-onsettype
    ValueSet: http://hl7.org/fhir/ValueSet/ex-onsettype
    """
    # Date of last examination.
    lxm = "lxm"
    # Date when symptoms were first noticed.
    sym = "sym"
    # Start date of last menstruation.
    lmn = "lmn"