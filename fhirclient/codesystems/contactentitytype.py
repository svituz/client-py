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

class ContactEntityType(object):
    """ This example value set defines a set of codes that can be used to indicate the purpose for which you would contact a
contact party.
    URL: http://terminology.hl7.org/CodeSystem/contactentity-type
    ValueSet: http://hl7.org/fhir/ValueSet/contactentity-type
    """
    # Contact details for information regarding to billing/general finance enquiries.
    BILL = "BILL"
    # Contact details for administrative enquiries.
    ADMIN = "ADMIN"
    # Contact details for issues related to Human Resources, such as staff matters, OH&S etc.
    HR = "HR"
    # Contact details for dealing with issues related to insurance claims/adjudication/payment.
    PAYOR = "PAYOR"
    # Generic information contact for patients.
    PATINF = "PATINF"
    # Dedicated contact point for matters relating to press enquiries.
    PRESS = "PRESS"

    allowed_values = [BILL, ADMIN, HR, PAYOR, PATINF, PRESS]