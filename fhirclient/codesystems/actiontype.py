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

class ActionType(object):
    """ The type of action to be performed.
    URL: http://terminology.hl7.org/CodeSystem/action-type
    ValueSet: http://hl7.org/fhir/ValueSet/action-type
    """
    # The action is to create a new resource.
    CREATE = "create"
    # The action is to update an existing resource.
    UPDATE = "update"
    # The action is to remove an existing resource.
    REMOVE = "remove"
    # The action is to fire a specific event.
    FIREEVENT = "fire-event"

    allowed_values = [CREATE, UPDATE, REMOVE, FIREEVENT]