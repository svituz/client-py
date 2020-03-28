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

class AdverseEventSeriousness(object):
    """ Overall seriousness of this event for the patient.
    URL: http://terminology.hl7.org/CodeSystem/adverse-event-seriousness
    ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-seriousness
    """
    # Non-serious.
    NONSERIOUS = "Non-serious"
    # Serious.
    SERIOUS = "Serious"
    # Results in death.
    SERIOUSRESULTSINDEATH = "SeriousResultsInDeath"
    # Is Life-threatening.
    SERIOUSISLIFETHREATENING = "SeriousIsLifeThreatening"
    # Requires inpatient hospitalization or causes prolongation of existing hospitalization.
    SERIOUSRESULTSINHOSPITALIZATION = "SeriousResultsInHospitalization"
    # Results in persistent or significant disability/incapacity.
    SERIOUSRESULTSINDISABILITY = "SeriousResultsInDisability"
    # Is a congenital anomaly/birth defect.
    SERIOUSISBIRTHDEFECT = "SeriousIsBirthDefect"
    # Requires intervention to prevent permanent impairment or damage (i.e., an important medical event that requires
    # medical judgement).
    SERIOUSREQUIRESPREVENTIMPAIRMENT = "SeriousRequiresPreventImpairment"

    allowed_values = [NONSERIOUS, SERIOUS, SERIOUSRESULTSINDEATH, SERIOUSISLIFETHREATENING, SERIOUSRESULTSINHOSPITALIZATION, SERIOUSRESULTSINDISABILITY, SERIOUSISBIRTHDEFECT, SERIOUSREQUIRESPREVENTIMPAIRMENT]