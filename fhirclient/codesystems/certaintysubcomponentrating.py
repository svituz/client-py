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

class CertaintySubcomponentRating(object):
    """ The quality rating of the subcomponent of a quality of evidence rating.
    URL: http://terminology.hl7.org/CodeSystem/certainty-subcomponent-rating
    ValueSet: http://hl7.org/fhir/ValueSet/certainty-subcomponent-rating
    """
    # no change to quality rating.
    NOCHANGE = "no-change"
    # reduce quality rating by 1.
    DOWNCODE1 = "downcode1"
    # reduce quality rating by 2.
    DOWNCODE2 = "downcode2"
    # reduce quality rating by 3.
    DOWNCODE3 = "downcode3"
    # increase quality rating by 1.
    UPCODE1 = "upcode1"
    # increase quality rating by 2.
    UPCODE2 = "upcode2"
    # no serious concern.
    NOCONCERN = "no-concern"
    # serious concern.
    SERIOUSCONCERN = "serious-concern"
    # critical concern.
    CRITICALCONCERN = "critical-concern"
    # possible reason for increasing quality rating was checked and found to bepresent.
    PRESENT = "present"
    # possible reason for increasing quality rating was checked and found to be absent.
    ABSENT = "absent"

    allowed_values = [NOCHANGE, DOWNCODE1, DOWNCODE2, DOWNCODE3, UPCODE1, UPCODE2, NOCONCERN, SERIOUSCONCERN, CRITICALCONCERN, PRESENT, ABSENT]