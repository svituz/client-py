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

class FinancialTaskInputTypeCodes(object):
    """ This value set includes Financial Task Input Type codes.
    URL: http://terminology.hl7.org/CodeSystem/financialtaskinputtype
    ValueSet: http://hl7.org/fhir/ValueSet/financial-taskinputtype
    """
    """The name of a resource to include in a selection."""
    INCLUDE = "include"
    """The name of a resource to not include in a selection."""
    EXCLUDE = "exclude"
    """A reference to the response resource to the original processing of a resource."""
    ORIGRESPONSE = "origresponse"
    """A reference value which must be quoted to authorize an action."""
    REFERENCE = "reference"
    """The sequence number associated with an item for reprocessing."""
    ITEM = "item"
    """The reference period for the action being requested."""
    PERIOD = "period"
    """The processing status from a check on the processing status of a resource such as the adjudication of a claim."""
    STATUS = "status"
    allowed_values = ['INCLUDE', 'EXCLUDE', 'ORIGRESPONSE', 'REFERENCE', 'ITEM', 'PERIOD', 'STATUS']