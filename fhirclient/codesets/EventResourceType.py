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
    chargeItem = "ChargeItem"
    # Remittance resource.
    claimResponse = "ClaimResponse"
    # A clinical assessment performed when planning treatments and management strategies for a patient.
    clinicalImpression = "ClinicalImpression"
    # A record of information transmitted from a sender to a receiver.
    communication = "Communication"
    # A set of resources composed into a single coherent clinical statement with clinical attestation.
    composition = "Composition"
    # Detailed information about conditions, problems or diagnoses.
    condition = "Condition"
    # A healthcare consumer's policy choices to permits or denies recipients or roles to perform actions for specific
	/// purposes and periods of time.
    consent = "Consent"
    # Insurance or medical plan or a payment agreement.
    coverage = "Coverage"
    # Record of use of a device.
    deviceUseStatement = "DeviceUseStatement"
    # A Diagnostic report - a combination of request information, atomic results, images, interpretation, as well as
	/// formatted reports.
    diagnosticReport = "DiagnosticReport"
    # A list that defines a set of documents.
    documentManifest = "DocumentManifest"
    # A reference to a document.
    documentReference = "DocumentReference"
    # An interaction during which services are provided to the patient.
    encounter = "Encounter"
    # EnrollmentResponse resource.
    enrollmentResponse = "EnrollmentResponse"
    # An association of a Patient with an Organization and  Healthcare Provider(s) for a period of time that the
	/// Organization assumes some level of responsibility.
    episodeOfCare = "EpisodeOfCare"
    # Explanation of Benefit resource.
    explanationOfBenefit = "ExplanationOfBenefit"
    # Information about patient's relatives, relevant for patient.
    familyMemberHistory = "FamilyMemberHistory"
    # The formal response to a guidance request.
    guidanceResponse = "GuidanceResponse"
    # A set of images produced in single study (one or more series of references images).
    imagingStudy = "ImagingStudy"
    # Immunization event information.
    immunization = "Immunization"
    # Results of a measure evaluation.
    measureReport = "MeasureReport"
    # A photo, video, or audio recording acquired or used in healthcare. The actual content may be inline or provided
	/// by direct reference.
    media = "Media"
    # Administration of medication to a patient.
    medicationAdministration = "MedicationAdministration"
    # Dispensing a medication to a named patient.
    medicationDispense = "MedicationDispense"
    # Record of medication being taken by a patient.
    medicationStatement = "MedicationStatement"
    # Measurements and simple assertions.
    observation = "Observation"
    # PaymentNotice request.
    paymentNotice = "PaymentNotice"
    # PaymentReconciliation resource.
    paymentReconciliation = "PaymentReconciliation"
    # An action that is being or was performed on a patient.
    procedure = "Procedure"
    # ProcessResponse resource.
    processResponse = "ProcessResponse"
    # A structured set of questions and their answers.
    questionnaireResponse = "QuestionnaireResponse"
    # Potential outcomes for a subject with likelihood.
    riskAssessment = "RiskAssessment"
    # Delivery of bulk Supplies.
    supplyDelivery = "SupplyDelivery"
    # A task to be performed.
    task = "Task"