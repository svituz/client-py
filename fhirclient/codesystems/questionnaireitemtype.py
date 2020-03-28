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

class QuestionnaireItemType(object):
    """ Distinguishes groups from questions and display text and indicates data type for questions.
    URL: http://hl7.org/fhir/item-type
    ValueSet: http://hl7.org/fhir/ValueSet/item-type
    """
    # An item with no direct answer but should have at least one child item.
    GROUP = "group"
    # Text for display that will not capture an answer or have child items.
    DISPLAY = "display"
    # An item that defines a specific answer to be captured, and which may have child items. (the answer provided in
    # the QuestionnaireResponse should be of the defined datatype).
    QUESTION = "question"
    # Question with a yes/no answer (valueBoolean).
    BOOLEAN = "boolean"
    # Question with is a real number answer (valueDecimal).
    DECIMAL = "decimal"
    # Question with an integer answer (valueInteger).
    INTEGER = "integer"
    # Question with a date answer (valueDate).
    DATE = "date"
    # Question with a date and time answer (valueDateTime).
    DATETIME = "dateTime"
    # Question with a time (hour:minute:second) answer independent of date. (valueTime).
    TIME = "time"
    # Question with a short (few words to short sentence) free-text entry answer (valueString).
    STRING = "string"
    # Question with a long (potentially multi-paragraph) free-text entry answer (valueString).
    TEXT = "text"
    # Question with a URL (website, FTP site, etc.) answer (valueUri).
    URL = "url"
    # Question with a Coding drawn from a list of possible answers (specified in either the answerOption property, or
    # via the valueset referenced in the answerValueSet property) as an answer (valueCoding).
    CHOICE = "choice"
    # Answer is a Coding drawn from a list of possible answers (as with the choice type) or a free-text entry in a
    # string (valueCoding or valueString).
    OPENCHOICE = "open-choice"
    # Question with binary content such as an image, PDF, etc. as an answer (valueAttachment).
    ATTACHMENT = "attachment"
    # Question with a reference to another resource (practitioner, organization, etc.) as an answer (valueReference).
    REFERENCE = "reference"
    # Question with a combination of a numeric value and unit, potentially with a comparator (<, >, etc.) as an
    # answer. (valueQuantity) There is an extension 'http://hl7.org/fhir/StructureDefinition/questionnaire-unit' that
    # can be used to define what unit should be captured (or the unit that has a ucum conversion from the provided
    # unit).
    QUANTITY = "quantity"

    allowed_values = [GROUP, DISPLAY, QUESTION, BOOLEAN, DECIMAL, INTEGER, DATE, DATETIME, TIME, STRING, TEXT, URL, CHOICE, OPENCHOICE, ATTACHMENT, REFERENCE, QUANTITY]