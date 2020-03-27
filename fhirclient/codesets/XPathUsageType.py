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

class XPathUsageType(object):
    """ How a search parameter relates to the set of elements returned by evaluating its xpath query.
    URL: http://hl7.org/fhir/search-xpath-usage
    ValueSet: http://hl7.org/fhir/ValueSet/search-xpath-usage
    """
    # The search parameter is derived directly from the selected nodes based on the type definitions.
    normal = "normal"
    # The search parameter is derived by a phonetic transform from the selected nodes.
    phonetic = "phonetic"
    # The search parameter is based on a spatial transform of the selected nodes.
    nearby = "nearby"
    # The search parameter is based on a spatial transform of the selected nodes, using physical distance from the
	/// middle.
    distance = "distance"
    # The interpretation of the xpath statement is unknown (and can't be automated).
    other = "other"