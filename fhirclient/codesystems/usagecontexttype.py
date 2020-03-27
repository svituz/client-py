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

class UsageContextType(object):
    """ A code that specifies a type of context being specified by a usage context.
    URL: http://terminology.hl7.org/CodeSystem/usage-context-type
    ValueSet: http://hl7.org/fhir/ValueSet/usage-context-type
    """
    """The gender of the patient. For this context type, appropriate values can be found in the
	/// http://hl7.org/fhir/ValueSet/administrative-gender value set."""
    GENDER = "gender"
    """The age of the patient. For this context type, the value could be a range that specifies the applicable ages or
	/// a code from an appropriate value set such as the MeSH value set
	/// http://terminology.hl7.org/ValueSet/v3-AgeGroupObservationValue."""
    AGE = "age"
    """The clinical concept(s) addressed by the artifact. For example, disease, diagnostic test interpretation,
	/// medication ordering as in http://hl7.org/fhir/ValueSet/condition-code."""
    FOCUS = "focus"
    """The clinical specialty of the context in which the patient is being treated - For example, PCP, Patient,
	/// Cardiologist, Behavioral Professional, Oral Health Professional, Prescriber, etc... taken from a specialty value
	/// set such as the NUCC Health Care provider taxonomy value set http://hl7.org/fhir/ValueSet/provider-taxonomy."""
    USER = "user"
    """The settings in which the artifact is intended for use. For example, admission, pre-op, etc. For example, the
	/// ActEncounterCode value set http://terminology.hl7.org/ValueSet/v3-ActEncounterCode."""
    WORKFLOW = "workflow"
    """The context for the clinical task(s) represented by this artifact. For example, this could be any task context
	/// represented by the HL7 ActTaskCode value set http://terminology.hl7.org/ValueSet/v3-ActTaskCode. General
	/// categories include: order entry, patient documentation and patient information review."""
    TASK = "task"
    """The venue in which an artifact could be used. For example, Outpatient, Inpatient, Home, Nursing home. The code
	/// value may originate from the HL7 ServiceDeliveryLocationRoleType value set
	/// (http://terminology.hl7.org/ValueSet/v3-ServiceDeliveryLocationRoleType)."""
    VENUE = "venue"
    """The species to which an artifact applies. For example, SNOMED - 387961004 | Kingdom Animalia (organism)."""
    SPECIES = "species"
    """A program/project of work for which this artifact is applicable."""
    PROGRAM = "program"
    allowed_values = ['GENDER', 'AGE', 'FOCUS', 'USER', 'WORKFLOW', 'TASK', 'VENUE', 'SPECIES', 'PROGRAM']