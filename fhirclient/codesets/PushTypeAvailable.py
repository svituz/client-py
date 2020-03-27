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

class PushTypeAvailable(object):
    """ Type of alerts/updates the primary source can send
    URL: http://terminology.hl7.org/CodeSystem/push-type-available
    ValueSet: http://hl7.org/fhir/ValueSet/verificationresult-push-type-available
    """
    # specific
    specific = "specific"
    # any
    any = "any"
    # source
    source = "source"