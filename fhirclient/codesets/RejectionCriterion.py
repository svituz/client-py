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

class RejectionCriterion(object):
    """ Criterion for rejection of the specimen by laboratory.
    URL: http://terminology.hl7.org/CodeSystem/rejection-criteria
    ValueSet: http://hl7.org/fhir/ValueSet/rejection-criteria
    """
    # blood specimen hemolized.
    hemolized = "hemolized"
    # insufficient quantity of specimen.
    insufficient = "insufficient"
    # specimen container broken.
    broken = "broken"
    # specimen clotted.
    clotted = "clotted"
    # specimen temperature inappropriate.
    wrongTemperature = "wrong-temperature"