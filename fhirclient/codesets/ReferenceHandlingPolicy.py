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

class ReferenceHandlingPolicy(object):
    """ A set of flags that defines how references are supported.
    URL: http://hl7.org/fhir/reference-handling-policy
    ValueSet: http://hl7.org/fhir/ValueSet/reference-handling-policy
    """
    # The server supports and populates Literal references (i.e. using Reference.reference) where they are known (this
	/// code does not guarantee that all references are literal; see 'enforced').
    literal = "literal"
    # The server allows logical references (i.e. using Reference.identifier).
    logical = "logical"
    # The server will attempt to resolve logical references to literal references - i.e. converting
	/// Reference.identifier to Reference.reference (if resolution fails, the server may still accept resources; see
	/// logical).
    resolves = "resolves"
    # The server enforces that references have integrity - e.g. it ensures that references can always be resolved.
	/// This is typically the case for clinical record systems, but often not the case for middleware/proxy systems.
    enforced = "enforced"
    # The server does not support references that point to other servers.
    local = "local"