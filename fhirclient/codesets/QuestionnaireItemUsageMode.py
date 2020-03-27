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

class QuestionnaireItemUsageMode(object):
    """ Identifies the modes of usage of a questionnaire that should enable a particular questionnaire item.
    URL: http://terminology.hl7.org/CodeSystem/questionnaire-usage-mode
    ValueSet: http://hl7.org/fhir/ValueSet/questionnaire-usage-mode
    """
    # Render the item regardless of usage mode.
    captureDisplay = "capture-display"
    # Render the item only when capturing data.
    capture = "capture"
    # Render the item only when displaying a completed form.
    display = "display"
    # Render the item only when displaying a completed form and the item has been answered (or has child items that
	/// have been answered).
    displayNonEmpty = "display-non-empty"
    # Render the item when capturing data or when displaying a completed form and the item has been answered (or has
	/// child items that have been answered).
    captureDisplayNonEmpty = "capture-display-non-empty"