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

class ConsentActionCodes(object):
    """ This value set includes sample Consent Action codes.
    URL: http://terminology.hl7.org/CodeSystem/consentaction
    ValueSet: http://hl7.org/fhir/ValueSet/consent-action
    """
    """Gather retrieved information for storage"""
    COLLECT = "collect"
    """Retrieval without permitting collection, use or disclosure. e.g., no screen-scraping for collection, use or
	/// disclosure (view-only access)"""
    ACCESS = "access"
    """Utilize the retrieved information"""
    USE = "use"
    """Transfer retrieved information"""
    DISCLOSE = "disclose"
    """Allow retrieval of a patient's information for the purpose of update or rectify"""
    CORRECT = "correct"
    allowed_values = ['COLLECT', 'ACCESS', 'USE', 'DISCLOSE', 'CORRECT']