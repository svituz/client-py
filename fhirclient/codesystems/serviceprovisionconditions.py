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

class ServiceProvisionConditions(object):
    """ The code(s) that detail the conditions under which the healthcare service is available/offered.
    URL: http://terminology.hl7.org/CodeSystem/service-provision-conditions
    ValueSet: http://hl7.org/fhir/ValueSet/service-provision-conditions
    """
    # This service is available for no patient cost.
    FREE = "free"
    # There are discounts available on this service for qualifying patients.
    DISC = "disc"
    # Fees apply for this service.
    COST = "cost"

    allowed_values = [FREE, DISC, COST]