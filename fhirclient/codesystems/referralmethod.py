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

class ReferralMethod(object):
    """ The methods of referral can be used when referring to a specific HealthCareService resource.
    URL: http://terminology.hl7.org/CodeSystem/service-referral-method
    ValueSet: http://hl7.org/fhir/ValueSet/service-referral-method
    """
    # Referrals may be accepted by fax.
    FAX = "fax"
    # Referrals may be accepted over the phone from a practitioner.
    PHONE = "phone"
    # Referrals may be accepted via a secure messaging system. To determine the types of secure messaging systems
    # supported, refer to the identifiers collection. Callers will need to understand the specific identifier system
    # used to know that they are able to transmit messages.
    ELEC = "elec"
    # Referrals may be accepted via a secure email. To send please encrypt with the services public key.
    SEMAIL = "semail"
    # Referrals may be accepted via regular postage (or hand delivered).
    MAIL = "mail"

    allowed_values = [FAX, PHONE, ELEC, SEMAIL, MAIL]