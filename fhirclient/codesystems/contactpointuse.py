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

class ContactPointUse(object):
    """ Use of contact point.
    URL: http://hl7.org/fhir/contact-point-use
    ValueSet: http://hl7.org/fhir/ValueSet/contact-point-use
    """
    """A communication contact point at a home; attempted contacts for business purposes might intrude privacy and
	/// chances are one will contact family or other household members instead of the person one wishes to call.
	/// Typically used with urgent cases, or if no other contacts are available."""
    HOME = "home"
    """An office contact point. First choice for business related contacts during business hours."""
    WORK = "work"
    """A temporary contact point. The period can provide more detailed information."""
    TEMP = "temp"
    """This contact point is no longer in use (or was never correct, but retained for records)."""
    OLD = "old"
    """A telecommunication device that moves and stays with its owner. May have characteristics of all other use codes,
	/// suitable for urgent matters, not the first choice for routine business."""
    MOBILE = "mobile"
    allowed_values = ['HOME', 'WORK', 'TEMP', 'OLD', 'MOBILE']