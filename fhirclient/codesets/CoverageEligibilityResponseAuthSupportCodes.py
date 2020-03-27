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
    # A request or authorization for laboratory diagnostic tests.
    laborder = "laborder"
    # A report on laboratory diagnostic test(s).
    labreport = "labreport"
    # A request or authorization for diagnostic imaging.
    diagnosticimageorder = "diagnosticimageorder"
    # A report on diagnostic image(s).
    diagnosticimagereport = "diagnosticimagereport"
    # A report from a licensed professional regarding the siutation, condition or proposed treatment.
    professionalreport = "professionalreport"
    # A formal accident report as would be filed with police or a simlar official body.
    accidentreport = "accidentreport"
    # A physical model of the affected area.
    model = "model"
    # A photograph of the affected area.
    picture = "picture"