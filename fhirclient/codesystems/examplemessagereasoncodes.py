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

class ExampleMessageReasonCodes(object):
    """ Example Message Reasons. These are the set of codes that might be used an updating an encounter using admin-update.
    URL: http://terminology.hl7.org/CodeSystem/message-reasons-encounter
    ValueSet: http://hl7.org/fhir/ValueSet/message-reason-encounter
    """
    # The patient has been admitted.
    ADMIT = "admit"
    # The patient has been discharged.
    DISCHARGE = "discharge"
    # The patient has temporarily left the institution.
    ABSENT = "absent"
    # The patient has returned from a temporary absence.
    RETURN = "return"
    # The patient has been moved to a new location.
    MOVED = "moved"
    # Encounter details have been updated (e.g. to correct a coding error).
    EDIT = "edit"

    allowed_values = [ADMIT, DISCHARGE, ABSENT, RETURN, MOVED, EDIT]