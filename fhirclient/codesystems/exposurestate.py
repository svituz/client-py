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

class ExposureState(object):
    """ Whether the results by exposure is describing the results for the primary exposure of interest (exposure) or the
alternative state (exposureAlternative).
    URL: http://hl7.org/fhir/exposure-state
    ValueSet: http://hl7.org/fhir/ValueSet/exposure-state
    """
    """used when the results by exposure is describing the results for the primary exposure of interest."""
    EXPOSURE = "exposure"
    """used when the results by exposure is describing the results for the alternative exposure state, control state or
	/// comparator state."""
    EXPOSUREALTERNATIVE = "exposure-alternative"
    allowed_values = ['EXPOSURE', 'EXPOSUREALTERNATIVE']