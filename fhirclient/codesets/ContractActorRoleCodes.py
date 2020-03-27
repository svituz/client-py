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

class ContractActorRoleCodes(object):
    """ This value set includes sample Contract Actor Role codes.
    URL: http://terminology.hl7.org/CodeSystem/contractactorrole
    ValueSet: http://hl7.org/fhir/ValueSet/contract-actorrole
    """
    # Someone who provides health care related services to people or animals including both clinical and support
	/// services.
    practitioner = "practitioner"
    # A receiver, human or animal, of health care related goods and services.
    patient = "patient"