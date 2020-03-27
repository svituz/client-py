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

class ContributorType(object):
    """ The type of contributor.
    URL: http://hl7.org/fhir/contributor-type
    ValueSet: http://hl7.org/fhir/ValueSet/contributor-type
    """
    """An author of the content of the module."""
    AUTHOR = "author"
    """An editor of the content of the module."""
    EDITOR = "editor"
    """A reviewer of the content of the module."""
    REVIEWER = "reviewer"
    """An endorser of the content of the module."""
    ENDORSER = "endorser"
    allowed_values = ['AUTHOR', 'EDITOR', 'REVIEWER', 'ENDORSER']