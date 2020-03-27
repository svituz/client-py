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

class RepositoryType(object):
    """ Type for access of external URI.
    URL: http://hl7.org/fhir/repository-type
    ValueSet: http://hl7.org/fhir/ValueSet/repository-type
    """
    """When URL is clicked, the resource can be seen directly (by webpage or by download link format)."""
    DIRECTLINK = "directlink"
    """When the API method (e.g. [base_url]/[parameter]) related with the URL of the website is executed, the resource
	/// can be seen directly (usually in JSON or XML format)."""
    OPENAPI = "openapi"
    """When logged into the website, the resource can be seen."""
    LOGIN = "login"
    """When logged in and  follow the API in the website related with URL, the resource can be seen."""
    OAUTH = "oauth"
    """Some other complicated or particular way to get resource from URL."""
    OTHER = "other"
    allowed_values = ['DIRECTLINK', 'OPENAPI', 'LOGIN', 'OAUTH', 'OTHER']