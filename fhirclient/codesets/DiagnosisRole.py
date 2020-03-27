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

class DiagnosisRole(object):
    """ This value set defines a set of codes that can be used to express the role of a diagnosis on the Encounter or
EpisodeOfCare record.
    URL: http://terminology.hl7.org/CodeSystem/diagnosis-role
    ValueSet: http://hl7.org/fhir/ValueSet/diagnosis-role
    """
    # AD
    AD = "AD"
    # DD
    DD = "DD"
    # CC
    CC = "CC"
    # CM
    CM = "CM"
    # preOp
    preOp = "pre-op"
    # postOp
    postOp = "post-op"
    # billing
    billing = "billing"