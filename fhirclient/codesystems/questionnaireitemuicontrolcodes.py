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

class QuestionnaireItemUIControlCodes(object):
    """ Starter set of user interface control/display mechanisms that might be used when rendering an item in a questionnaire.
    URL: http://hl7.org/fhir/questionnaire-item-control
    ValueSet: http://hl7.org/fhir/ValueSet/questionnaire-item-control
    """
    """UI controls relevant to organizing groups of questions"""
    GROUP = "group"
    """Questions within the group should be listed sequentially"""
    LIST = "list"
    """Questions within the group are rows in the table with possible answers as columns.  Used for 'choice' questions."""
    TABLE = "table"
    """Questions within the group are columns in the table with possible answers as rows.  Used for 'choice' questions."""
    HTABLE = "htable"
    """Questions within the group are columns in the table with each group repetition as a row.  Used for single-answer
	/// questions."""
    GTABLE = "gtable"
    """This table has one row - for the question.  Permitted answers are columns.  Used for choice questions."""
    ATABLE = "atable"
    """The group is to be continuously visible at the top of the questionnaire"""
    HEADER = "header"
    """The group is to be continuously visible at the bottom of the questionnaire"""
    FOOTER = "footer"
    """UI controls relevant to rendering questionnaire text items"""
    TEXT = "text"
    """Text is displayed as a paragraph in a sequential position between sibling items (default behavior)"""
    INLINE = "inline"
    """Text is displayed immediately below or within the answer-entry area of the containing question item (typically
	/// as a guide for what to enter)"""
    PROMPT = "prompt"
    """Text is displayed adjacent (horizontally or vertically) to the answer space for the parent question, typically
	/// to indicate a unit of measure"""
    UNIT = "unit"
    """Text is displayed to the left of the set of answer choices or a scaling control for the parent question item to
	/// indicate the meaning of the 'lower' bound.  E.g. 'Strongly disagree'"""
    LOWER = "lower"
    """Text is displayed to the right of the set of answer choices or a scaling control for the parent question item to
	/// indicate the meaning of the 'upper' bound.  E.g. 'Strongly agree'"""
    UPPER = "upper"
    """Text is temporarily visible over top of an item if the mouse is positioned over top of the text for the
	/// containing item"""
    FLYOVER = "flyover"
    """Text is displayed in a dialog box or similar control if invoked by pushing a button or some other UI-appropriate
	/// action to request 'help' for a question, group or the questionnaire as a whole (depending what the text is
	/// nested within)"""
    HELP = "help"
    """UI controls relevant to capturing question data"""
    QUESTION = "question"
    """A control which provides a list of potential matches based on text entered into a control.  Used for large
	/// choice sets where text-matching is an appropriate discovery mechanism."""
    AUTOCOMPLETE = "autocomplete"
    """A control where an item (or multiple items) can be selected from a list that is only displayed when the user is
	/// editing the field."""
    DROPDOWN = "drop-down"
    """A control where choices are listed with a box beside them.  The box can be toggled to select or de-select a
	/// given choice.  Multiple selections may be possible."""
    CHECKBOX = "check-box"
    """A control where editing an item spawns a separate dialog box or screen permitting a user to navigate, filter or
	/// otherwise discover an appropriate match.  Useful for large choice sets where text matching is not an appropriate
	/// discovery mechanism.  Such screens must generally be tuned for the specific choice list structure."""
    LOOKUP = "lookup"
    """A control where choices are listed with a button beside them.  The button can be toggled to select or de-select
	/// a given choice.  Selecting one item deselects all others."""
    RADIOBUTTON = "radio-button"
    """A control where an axis is displayed between the high and low values and the control can be visually manipulated
	/// to select a value anywhere on the axis."""
    SLIDER = "slider"
    """A control where a list of numeric or other ordered values can be scrolled through via arrows."""
    SPINNER = "spinner"
    """A control where a user can type in their answer freely."""
    TEXTBOX = "text-box"
    allowed_values = ['GROUP', 'LIST', 'TABLE', 'HTABLE', 'GTABLE', 'ATABLE', 'HEADER', 'FOOTER', 'TEXT', 'INLINE', 'PROMPT', 'UNIT', 'LOWER', 'UPPER', 'FLYOVER', 'HELP', 'QUESTION', 'AUTOCOMPLETE', 'DROPDOWN', 'CHECKBOX', 'LOOKUP', 'RADIOBUTTON', 'SLIDER', 'SPINNER', 'TEXTBOX']