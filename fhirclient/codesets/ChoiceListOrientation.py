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

class ChoiceListOrientation(object):
    """ Direction in which lists of possible answers should be displayed.
    URL: http://terminology.hl7.org/CodeSystem/choice-list-orientation
    ValueSet: http://hl7.org/fhir/ValueSet/choice-list-orientation
    """
    # List choices along the horizontal axis.
    horizontal = "horizontal"
    # List choices down the vertical axis.
    vertical = "vertical"