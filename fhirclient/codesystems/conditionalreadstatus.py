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

class ConditionalReadStatus(object):
    """ A code that indicates how the server supports conditional read.
    URL: http://hl7.org/fhir/conditional-read-status
    ValueSet: http://hl7.org/fhir/ValueSet/conditional-read-status
    """
    """No support for conditional reads."""
    NOTSUPPORTED = "not-supported"
    """Conditional reads are supported, but only with the If-Modified-Since HTTP Header."""
    MODIFIEDSINCE = "modified-since"
    """Conditional reads are supported, but only with the If-None-Match HTTP Header."""
    NOTMATCH = "not-match"
    """Conditional reads are supported, with both If-Modified-Since and If-None-Match HTTP Headers."""
    FULLSUPPORT = "full-support"
    allowed_values = ['NOTSUPPORTED', 'MODIFIEDSINCE', 'NOTMATCH', 'FULLSUPPORT']