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
    # The Patient has been transferred from another hospital for this encounter.
    hospTrans = "hosp-trans"
    # The patient has been transferred from the emergency department within the hospital. This is typically used in
	/// the transition to an inpatient encounter
    emd = "emd"
    # The patient has been transferred from an outpatient department within the hospital.
    outp = "outp"
    # The patient is a newborn and the encounter will track the baby related activities (as opposed to the Mothers
	/// encounter - that may be associated using the newborn encounters partof property)
    born = "born"
    # The patient has been admitted due to a referred from a General Practitioner.
    gp = "gp"
    # The patient has been admitted due to a referred from a Specialist (as opposed to a General Practitioner).
    mp = "mp"
    # The patient has been transferred from a nursing home.
    nursing = "nursing"
    # The patient has been transferred from a psychiatric facility.
    psych = "psych"
    # The patient has been transferred from a rehabilitation facility or clinic.
    rehab = "rehab"
    # The patient has been admitted from a source otherwise not specified here.
    other = "other"