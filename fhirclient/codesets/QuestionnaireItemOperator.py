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

class QuestionnaireItemOperator(object):
    """ The criteria by which a question is enabled.
    URL: http://hl7.org/fhir/questionnaire-enable-operator
    ValueSet: http://hl7.org/fhir/ValueSet/questionnaire-enable-operator
    """
    # True if whether an answer exists is equal to the enableWhen answer (which must be a boolean).
    exists = "exists"
    # True if whether at least one answer has a value that is equal to the enableWhen answer.
    eq = "="
    # True if whether at least no answer has a value that is equal to the enableWhen answer.
    ne = "!="
    # True if whether at least no answer has a value that is greater than the enableWhen answer.
    gt = ">"
    # True if whether at least no answer has a value that is less than the enableWhen answer.
    lt = "<"
    # True if whether at least no answer has a value that is greater or equal to the enableWhen answer.
    gte = ">="
    # True if whether at least no answer has a value that is less or equal to the enableWhen answer.
    lte = "<="