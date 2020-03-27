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

class AdmitSource(object):
    """ This value set defines a set of codes that can be used to indicate from where the patient came in.
    URL: http://terminology.hl7.org/CodeSystem/admit-source
    ValueSet: http://hl7.org/fhir/ValueSet/encounter-admit-source
    """
    """The Patient has been transferred from another hospital for this encounter."""
    HOSPTRANS = "hosp-trans"
    """The patient has been transferred from the emergency department within the hospital. This is typically used in
	/// the transition to an inpatient encounter"""
    EMD = "emd"
    """The patient has been transferred from an outpatient department within the hospital."""
    OUTP = "outp"
    """The patient is a newborn and the encounter will track the baby related activities (as opposed to the Mothers
	/// encounter - that may be associated using the newborn encounters partof property)"""
    BORN = "born"
    """The patient has been admitted due to a referred from a General Practitioner."""
    GP = "gp"
    """The patient has been admitted due to a referred from a Specialist (as opposed to a General Practitioner)."""
    MP = "mp"
    """The patient has been transferred from a nursing home."""
    NURSING = "nursing"
    """The patient has been transferred from a psychiatric facility."""
    PSYCH = "psych"
    """The patient has been transferred from a rehabilitation facility or clinic."""
    REHAB = "rehab"
    """The patient has been admitted from a source otherwise not specified here."""
    OTHER = "other"
    allowed_values = ['HOSPTRANS', 'EMD', 'OUTP', 'BORN', 'GP', 'MP', 'NURSING', 'PSYCH', 'REHAB', 'OTHER']