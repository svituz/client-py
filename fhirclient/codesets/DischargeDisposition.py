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

class DischargeDisposition(object):
    """ This value set defines a set of codes that can be used to where the patient left the hospital.
    URL: http://terminology.hl7.org/CodeSystem/discharge-disposition
    ValueSet: http://hl7.org/fhir/ValueSet/encounter-discharge-disposition
    """
    # The patient was dicharged and has indicated that they are going to return home afterwards.
    home = "home"
    # The patient was discharged and has indicated that they are going to return home afterwards, but not the
	/// patient's home - e.g. a family member's home.
    altHome = "alt-home"
    # The patient was transferred to another healthcare facility.
    otherHcf = "other-hcf"
    # The patient has been discharged into palliative care.
    hosp = "hosp"
    # The patient has been discharged into long-term care where is likely to be monitored through an ongoing episode-
	/// of-care.
    long = "long"
    # The patient self discharged against medical advice.
    aadvice = "aadvice"
    # The patient has deceased during this encounter.
    exp = "exp"
    # The patient has been transferred to a psychiatric facility.
    psy = "psy"
    # The patient was discharged and is to receive post acute care rehabilitation services.
    rehab = "rehab"
    # The patient has been discharged to a skilled nursing facility for the patient to receive additional care.
    snf = "snf"
    # The discharge disposition has not otherwise defined.
    oth = "oth"