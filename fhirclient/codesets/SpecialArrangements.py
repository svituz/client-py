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

class SpecialArrangements(object):
    """ This value set defines a set of codes that can be used to indicate the kinds of special arrangements in place for a
patients visit.
    URL: http://terminology.hl7.org/CodeSystem/encounter-special-arrangements
    ValueSet: http://hl7.org/fhir/ValueSet/encounter-special-arrangements
    """
    # The patient requires a wheelchair to be made available for the encounter.
    wheel = "wheel"
    # An additional bed made available for a person accompanying the patient, for example a parent accompanying a
	/// child.
    addBed = "add-bed"
    # The patient is not fluent in the local language and requires an interpreter to be available. Refer to the
	/// Patient.Language property for the type of interpreter required.
    int = "int"
    # A person who accompanies a patient to provide assistive services necessary for the patient's care during the
	/// encounter.
    att = "att"
    # The patient has a guide dog and the location used for the encounter should be able to support the presence of
	/// the service animal.
    dog = "dog"