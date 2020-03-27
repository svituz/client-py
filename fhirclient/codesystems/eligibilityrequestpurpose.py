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

class EligibilityRequestPurpose(object):
    """ A code specifying the types of information being requested.
    URL: http://hl7.org/fhir/eligibilityrequest-purpose
    ValueSet: http://hl7.org/fhir/ValueSet/eligibilityrequest-purpose
    """
    """The prior authorization requirements for the listed, or discovered if specified, converages for the categories
	/// of service and/or specifed biling codes are requested."""
    AUTHREQUIREMENTS = "auth-requirements"
    """The plan benefits and optionally benefits consumed  for the listed, or discovered if specified, converages are
	/// requested."""
    BENEFITS = "benefits"
    """The insurer is requested to report on any coverages which they are aware of in addition to any specifed."""
    DISCOVERY = "discovery"
    """A check that the specified coverages are in-force is requested."""
    VALIDATION = "validation"
    allowed_values = ['AUTHREQUIREMENTS', 'BENEFITS', 'DISCOVERY', 'VALIDATION']