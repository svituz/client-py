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

class CoverageEligibilityResponseAuthSupportCodes(object):
    """ This value set includes CoverageEligibilityResponse Auth Support codes.
    URL: http://terminology.hl7.org/CodeSystem/coverageeligibilityresponse-ex-auth-support
    ValueSet: http://hl7.org/fhir/ValueSet/coverageeligibilityresponse-ex-auth-support
    """
    """A request or authorization for laboratory diagnostic tests."""
    LABORDER = "laborder"
    """A report on laboratory diagnostic test(s)."""
    LABREPORT = "labreport"
    """A request or authorization for diagnostic imaging."""
    DIAGNOSTICIMAGEORDER = "diagnosticimageorder"
    """A report on diagnostic image(s)."""
    DIAGNOSTICIMAGEREPORT = "diagnosticimagereport"
    """A report from a licensed professional regarding the siutation, condition or proposed treatment."""
    PROFESSIONALREPORT = "professionalreport"
    """A formal accident report as would be filed with police or a simlar official body."""
    ACCIDENTREPORT = "accidentreport"
    """A physical model of the affected area."""
    MODEL = "model"
    """A photograph of the affected area."""
    PICTURE = "picture"
    allowed_values = ['LABORDER', 'LABREPORT', 'DIAGNOSTICIMAGEORDER', 'DIAGNOSTICIMAGEREPORT', 'PROFESSIONALREPORT', 'ACCIDENTREPORT', 'MODEL', 'PICTURE']