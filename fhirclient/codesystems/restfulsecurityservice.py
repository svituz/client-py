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

class RestfulSecurityService(object):
    """ Types of security services used with FHIR.
    URL: http://terminology.hl7.org/CodeSystem/restful-security-service
    ValueSet: http://hl7.org/fhir/ValueSet/restful-security-service
    """
    """OAuth (unspecified version see oauth.net)."""
    OAUTH = "OAuth"
    """OAuth2 using SMART-on-FHIR profile (see http://docs.smarthealthit.org/)."""
    SMARTONFHIR = "SMART-on-FHIR"
    """Microsoft NTLM Authentication."""
    NTLM = "NTLM"
    """Basic authentication defined in HTTP specification."""
    BASIC = "Basic"
    """see http://www.ietf.org/rfc/rfc4120.txt."""
    KERBEROS = "Kerberos"
    """SSL where client must have a certificate registered with the server."""
    CERTIFICATES = "Certificates"
    allowed_values = ['OAUTH', 'SMARTONFHIR', 'NTLM', 'BASIC', 'KERBEROS', 'CERTIFICATES']