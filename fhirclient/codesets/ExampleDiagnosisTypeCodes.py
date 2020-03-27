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

class ExampleDiagnosisTypeCodes(object):
    """ This value set includes example Diagnosis Type codes.
    URL: http://terminology.hl7.org/CodeSystem/ex-diagnosistype
    ValueSet: http://hl7.org/fhir/ValueSet/ex-diagnosistype
    """
    # The diagnosis given as the reason why the patient was admitted to the hospital.
    admitting = "admitting"
    # A diagnosis made on the basis of medical signs and patient-reported symptoms, rather than diagnostic tests.
    clinical = "clinical"
    # One of a set of the possible diagnoses that could be connected to the signs, symptoms, and lab findings.
    differential = "differential"
    # The diagnosis given when the patient is discharged from the hospital.
    discharge = "discharge"
    # A diagnosis based significantly on laboratory reports or test results, rather than the physical examination of
	/// the patient.
    laboratory = "laboratory"
    # A diagnosis which identifies people's responses to situations in their lives, such as a readiness to change or a
	/// willingness to accept assistance.
    nursing = "nursing"
    # A diagnosis determined prior to birth.
    prenatal = "prenatal"
    # The single medical diagnosis that is most relevant to the patient's chief complaint or need for treatment.
    principal = "principal"
    # A diagnosis based primarily on the results from medical imaging studies.
    radiology = "radiology"
    # A diagnosis determined using telemedicine techniques.
    remote = "remote"
    # The labeling of an illness in a specific historical event using modern knowledge, methods and disease
	/// classifications.
    retrospective = "retrospective"
    # A diagnosis determined by the patient.
    self = "self"