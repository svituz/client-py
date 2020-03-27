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

class NameUse(object):
    """ The use of a human name.
    URL: http://hl7.org/fhir/name-use
    ValueSet: http://hl7.org/fhir/ValueSet/name-use
    """
    """Known as/conventional/the one you normally use."""
    USUAL = "usual"
    """The formal name as registered in an official (government) registry, but which name might not be commonly used.
	/// May be called "legal name"."""
    OFFICIAL = "official"
    """A temporary name. Name.period can provide more detailed information. This may also be used for temporary names
	/// assigned at birth or in emergency situations."""
    TEMP = "temp"
    """A name that is used to address the person in an informal manner, but is not part of their formal or usual name."""
    NICKNAME = "nickname"
    """Anonymous assigned name, alias, or pseudonym (used to protect a person's identity for privacy reasons)."""
    ANONYMOUS = "anonymous"
    """This name is no longer in use (or was never correct, but retained for records)."""
    OLD = "old"
    """A name used prior to changing name because of marriage. This name use is for use by applications that collect
	/// and store names that were used prior to a marriage. Marriage naming customs vary greatly around the world, and
	/// are constantly changing. This term is not gender specific. The use of this term does not imply any particular
	/// history for a person's name."""
    MAIDEN = "maiden"
    allowed_values = ['USUAL', 'OFFICIAL', 'TEMP', 'NICKNAME', 'ANONYMOUS', 'OLD', 'MAIDEN']