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

class EnableWhenBehavior(object):
    """ Controls how multiple enableWhen values are interpreted -  whether all or any must be true.
    URL: http://hl7.org/fhir/questionnaire-enable-behavior
    ValueSet: http://hl7.org/fhir/ValueSet/questionnaire-enable-behavior
    """
    # Enable the question when all the enableWhen criteria are satisfied.
    ALL = "all"
    # Enable the question when any of the enableWhen criteria are satisfied.
    ANY = "any"

    allowed_values = [ALL, ANY]