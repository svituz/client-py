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

class ExpressionLanguage(object):
    """ The media type of the expression language.
    URL: http://hl7.org/fhir/expression-language
    ValueSet: http://hl7.org/fhir/ValueSet/expression-language
    """
    # Clinical Quality Language.
    textCql = "text/cql"
    # FHIRPath.
    textFhirpath = "text/fhirpath"
    # FHIR's RESTful query syntax - typically independent of base URL.
    applicationXFhirQuery = "application/x-fhir-query"