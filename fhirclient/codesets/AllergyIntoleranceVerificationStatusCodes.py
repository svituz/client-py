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

class AllergyIntoleranceVerificationStatusCodes(object):
    """ Preferred value set for AllergyIntolerance Verification Status.
    URL: http://terminology.hl7.org/CodeSystem/allergyintolerance-verification
    ValueSet: http://hl7.org/fhir/ValueSet/allergyintolerance-verification
    """
    # A low level of certainty about the propensity for a reaction to the identified substance.
    unconfirmed = "unconfirmed"
    # A high level of certainty about the propensity for a reaction to the identified substance, which may include
	/// clinical evidence by testing or rechallenge.
    confirmed = "confirmed"
    # A propensity for a reaction to the identified substance has been disputed or disproven with a sufficient level
	/// of clinical certainty to justify invalidating the assertion. This might or might not include testing or
	/// rechallenge.
    refuted = "refuted"
    # The statement was entered in error and is not valid.
    enteredInError = "entered-in-error"