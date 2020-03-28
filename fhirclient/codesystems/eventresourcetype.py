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

class EventResourceType(object):
    """ A list of all the event resource types defined in this version of the FHIR specification.
    URL: http://hl7.org/fhir/event-resource-types
    ValueSet: http://hl7.org/fhir/ValueSet/event-resource-types
    """
    # Item containing charge code(s) associated with the provision of healthcare provider products.
    CHARGEITEM = "ChargeItem"
    # Remittance resource.
    CLAIMRESPONSE = "ClaimResponse"
    # A clinical assessment performed when planning treatments and management strategies for a patient.
    CLINICALIMPRESSION = "ClinicalImpression"
    # A record of information transmitted from a sender to a receiver.
    COMMUNICATION = "Communication"
    # A set of resources composed into a single coherent clinical statement with clinical attestation.
    COMPOSITION = "Composition"
    # Detailed information about conditions, problems or diagnoses.
    CONDITION = "Condition"
    # A healthcare consumer's policy choices to permits or denies recipients or roles to perform actions for specific
    # purposes and periods of time.
    CONSENT = "Consent"
    # Insurance or medical plan or a payment agreement.
    COVERAGE = "Coverage"
    # Record of use of a device.
    DEVICEUSESTATEMENT = "DeviceUseStatement"
    # A Diagnostic report - a combination of request information, atomic results, images, interpretation, as well as
    # formatted reports.
    DIAGNOSTICREPORT = "DiagnosticReport"
    # A list that defines a set of documents.
    DOCUMENTMANIFEST = "DocumentManifest"
    # A reference to a document.
    DOCUMENTREFERENCE = "DocumentReference"
    # An interaction during which services are provided to the patient.
    ENCOUNTER = "Encounter"
    # EnrollmentResponse resource.
    ENROLLMENTRESPONSE = "EnrollmentResponse"
    # An association of a Patient with an Organization and  Healthcare Provider(s) for a period of time that the
    # Organization assumes some level of responsibility.
    EPISODEOFCARE = "EpisodeOfCare"
    # Explanation of Benefit resource.
    EXPLANATIONOFBENEFIT = "ExplanationOfBenefit"
    # Information about patient's relatives, relevant for patient.
    FAMILYMEMBERHISTORY = "FamilyMemberHistory"
    # The formal response to a guidance request.
    GUIDANCERESPONSE = "GuidanceResponse"
    # A set of images produced in single study (one or more series of references images).
    IMAGINGSTUDY = "ImagingStudy"
    # Immunization event information.
    IMMUNIZATION = "Immunization"
    # Results of a measure evaluation.
    MEASUREREPORT = "MeasureReport"
    # A photo, video, or audio recording acquired or used in healthcare. The actual content may be inline or provided
    # by direct reference.
    MEDIA = "Media"
    # Administration of medication to a patient.
    MEDICATIONADMINISTRATION = "MedicationAdministration"
    # Dispensing a medication to a named patient.
    MEDICATIONDISPENSE = "MedicationDispense"
    # Record of medication being taken by a patient.
    MEDICATIONSTATEMENT = "MedicationStatement"
    # Measurements and simple assertions.
    OBSERVATION = "Observation"
    # PaymentNotice request.
    PAYMENTNOTICE = "PaymentNotice"
    # PaymentReconciliation resource.
    PAYMENTRECONCILIATION = "PaymentReconciliation"
    # An action that is being or was performed on a patient.
    PROCEDURE = "Procedure"
    # ProcessResponse resource.
    PROCESSRESPONSE = "ProcessResponse"
    # A structured set of questions and their answers.
    QUESTIONNAIRERESPONSE = "QuestionnaireResponse"
    # Potential outcomes for a subject with likelihood.
    RISKASSESSMENT = "RiskAssessment"
    # Delivery of bulk Supplies.
    SUPPLYDELIVERY = "SupplyDelivery"
    # A task to be performed.
    TASK = "Task"

    allowed_values = [CHARGEITEM, CLAIMRESPONSE, CLINICALIMPRESSION, COMMUNICATION, COMPOSITION, CONDITION, CONSENT, COVERAGE, DEVICEUSESTATEMENT, DIAGNOSTICREPORT, DOCUMENTMANIFEST, DOCUMENTREFERENCE, ENCOUNTER, ENROLLMENTRESPONSE, EPISODEOFCARE, EXPLANATIONOFBENEFIT, FAMILYMEMBERHISTORY, GUIDANCERESPONSE, IMAGINGSTUDY, IMMUNIZATION, MEASUREREPORT, MEDIA, MEDICATIONADMINISTRATION, MEDICATIONDISPENSE, MEDICATIONSTATEMENT, OBSERVATION, PAYMENTNOTICE, PAYMENTRECONCILIATION, PROCEDURE, PROCESSRESPONSE, QUESTIONNAIRERESPONSE, RISKASSESSMENT, SUPPLYDELIVERY, TASK]