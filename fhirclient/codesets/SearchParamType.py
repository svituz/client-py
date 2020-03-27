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

class SearchParamType(object):
    """ Data types allowed to be used for search parameters.
    URL: http://hl7.org/fhir/search-param-type
    ValueSet: http://hl7.org/fhir/ValueSet/search-param-type
    """
    # Search parameter SHALL be a number (a whole number, or a decimal).
    number = "number"
    # Search parameter is on a date/time. The date format is the standard XML format, though other formats may be
	/// supported.
    date = "date"
    # Search parameter is a simple string, like a name part. Search is case-insensitive and accent-insensitive. May
	/// match just the start of a string. String parameters may contain spaces.
    string = "string"
    # Search parameter on a coded element or identifier. May be used to search through the text, display, code and
	/// code/codesystem (for codes) and label, system and key (for identifier). Its value is either a string or a pair
	/// of namespace and value, separated by a "|", depending on the modifier used.
    token = "token"
    # A reference to another resource (Reference or canonical).
    reference = "reference"
    # A composite search parameter that combines a search on two values together.
    composite = "composite"
    # A search parameter that searches on a quantity.
    quantity = "quantity"
    # A search parameter that searches on a URI (RFC 3986).
    uri = "uri"
    # Special logic applies to this parameter per the description of the search parameter.
    special = "special"