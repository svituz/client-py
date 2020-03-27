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

class DetectedIssueSeverity(object):
    """ Indicates the potential degree of impact of the identified issue on the patient.
    URL: http://hl7.org/fhir/detectedissue-severity
    ValueSet: http://hl7.org/fhir/ValueSet/detectedissue-severity
    """
    """Indicates the issue may be life-threatening or has the potential to cause permanent injury."""
    HIGH = "high"
    """Indicates the issue may result in noticeable adverse consequences but is unlikely to be life-threatening or
	/// cause permanent injury."""
    MODERATE = "moderate"
    """Indicates the issue may result in some adverse consequences but is unlikely to substantially affect the
	/// situation of the subject."""
    LOW = "low"
    allowed_values = ['HIGH', 'MODERATE', 'LOW']