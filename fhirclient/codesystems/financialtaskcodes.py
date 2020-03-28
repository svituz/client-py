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

class FinancialTaskCodes(object):
    """ This value set includes Financial Task codes.
    URL: http://terminology.hl7.org/CodeSystem/financialtaskcode
    ValueSet: http://hl7.org/fhir/ValueSet/financial-taskcode
    """
    # Cancel or reverse a resource, such as a claim or preauthorization, which is in-process or complete.
    CANCEL = "cancel"
    # Retrieve selected or all queued resources or messages.
    POLL = "poll"
    # Release any reserved funds or material obligations associated with a resource. For example, any unused but
    # reserved funds or treatment allowance associated with a preauthorization once treatment is complete.
    RELEASE = "release"
    # Indication that the processing of a resource, such as a claim, for some or all of the required work is now being
    # requested.
    REPROCESS = "reprocess"
    # Check on the processing status of a resource such as the adjudication of a claim.
    STATUS = "status"

    allowed_values = [CANCEL, POLL, RELEASE, REPROCESS, STATUS]