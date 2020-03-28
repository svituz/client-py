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

class TaskIntent(object):
    """ Distinguishes whether the task is a proposal, plan or full order.
    URL: http://hl7.org/fhir/task-intent
    """
    # The intent is not known.  When dealing with Task, it's not always known (or relevant) how the task was initiated
    # - i.e. whether it was proposed, planned, ordered or just done spontaneously.
    UNKNOWN = "unknown"

    allowed_values = [UNKNOWN]