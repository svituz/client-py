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

class GuideParameterCode(object):
    """ Code of parameter that is input to the guide.
    URL: http://hl7.org/fhir/guide-parameter-code
    ValueSet: http://hl7.org/fhir/ValueSet/guide-parameter-code
    """
    """If the value of this string 0..* parameter is one of the metadata fields then all conformance resources will
	/// have any specified [Resource].[field] overwritten with the ImplementationGuide.[field], where field is one of:
	/// version, date, status, publisher, contact, copyright, experimental, jurisdiction, useContext."""
    APPLY = "apply"
    """The value of this string 0..* parameter is a subfolder of the build context's location that is to be scanned to
	/// load resources. Scope is (if present) a particular resource type."""
    PATHRESOURCE = "path-resource"
    """The value of this string 0..1 parameter is a subfolder of the build context's location that contains files that
	/// are part of the html content processed by the builder."""
    PATHPAGES = "path-pages"
    """The value of this string 0..1 parameter is a subfolder of the build context's location that is used as the
	/// terminology cache. If this is not present, the terminology cache is on the local system, not under version
	/// control."""
    PATHTXCACHE = "path-tx-cache"
    """The value of this string 0..* parameter is a parameter (name=value) when expanding value sets for this
	/// implementation guide. This is particularly used to specify the versions of published terminologies such as
	/// SNOMED CT."""
    EXPANSIONPARAMETER = "expansion-parameter"
    """The value of this string 0..1 parameter is either "warning" or "error" (default = "error"). If the value is
	/// "warning" then IG build tools allow the IG to be considered successfully build even when there is no internal
	/// broken links."""
    RULEBROKENLINKS = "rule-broken-links"
    """The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in XML format. If
	/// not present, the Publication Tool decides whether to generate XML."""
    GENERATEXML = "generate-xml"
    """The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in JSON format. If
	/// not present, the Publication Tool decides whether to generate JSON."""
    GENERATEJSON = "generate-json"
    """The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in Turtle format.
	/// If not present, the Publication Tool decides whether to generate Turtle."""
    GENERATETURTLE = "generate-turtle"
    """The value of this string singleton parameter is the name of the file to use as the builder template for each
	/// generated page (see templating)."""
    HTMLTEMPLATE = "html-template"
    allowed_values = ['APPLY', 'PATHRESOURCE', 'PATHPAGES', 'PATHTXCACHE', 'EXPANSIONPARAMETER', 'RULEBROKENLINKS', 'GENERATEXML', 'GENERATEJSON', 'GENERATETURTLE', 'HTMLTEMPLATE']