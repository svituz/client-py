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

class QuestionnaireResponseStatus(object):
    """ Lifecycle status of the questionnaire response.
    URL: http://hl7.org/fhir/questionnaire-answers-status
    ValueSet: http://hl7.org/fhir/ValueSet/questionnaire-answers-status
    """
    # This QuestionnaireResponse has been partially filled out with answers but changes or additions are still
    # expected to be made to it.
    INPROGRESS = "in-progress"
    # This QuestionnaireResponse has been filled out with answers and the current content is regarded as definitive.
    COMPLETED = "completed"
    # This QuestionnaireResponse has been filled out with answers, then marked as complete, yet changes or additions
    # have been made to it afterwards.
    AMENDED = "amended"
    # This QuestionnaireResponse was entered in error and voided.
    ENTEREDINERROR = "entered-in-error"
    # This QuestionnaireResponse has been partially filled out with answers but has been abandoned. It is unknown
    # whether changes or additions are expected to be made to it.
    STOPPED = "stopped"

    allowed_values = [INPROGRESS, COMPLETED, AMENDED, ENTEREDINERROR, STOPPED]