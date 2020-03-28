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

class RequestResourceType(object):
    """ A list of all the request resource types defined in this version of the FHIR specification.
    URL: http://hl7.org/fhir/request-resource-types
    ValueSet: http://hl7.org/fhir/ValueSet/request-resource-types
    """
    # A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a
    # specific date/time. This may result in one or more Encounter(s).
    APPOINTMENT = "Appointment"
    # A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection.
    APPOINTMENTRESPONSE = "AppointmentResponse"
    # Healthcare plan for patient or group.
    CAREPLAN = "CarePlan"
    # Claim, Pre-determination or Pre-authorization.
    CLAIM = "Claim"
    # A request for information to be sent to a receiver.
    COMMUNICATIONREQUEST = "CommunicationRequest"
    # Legal Agreement.
    CONTRACT = "Contract"
    # Medical device request.
    DEVICEREQUEST = "DeviceRequest"
    # Enrollment request.
    ENROLLMENTREQUEST = "EnrollmentRequest"
    # Guidance or advice relating to an immunization.
    IMMUNIZATIONRECOMMENDATION = "ImmunizationRecommendation"
    # Ordering of medication for patient or group.
    MEDICATIONREQUEST = "MedicationRequest"
    # Diet, formula or nutritional supplement request.
    NUTRITIONORDER = "NutritionOrder"
    # A record of a request for service such as diagnostic investigations, treatments, or operations to be performed.
    SERVICEREQUEST = "ServiceRequest"
    # Request for a medication, substance or device.
    SUPPLYREQUEST = "SupplyRequest"
    # A task to be performed.
    TASK = "Task"
    # Prescription for vision correction products for a patient.
    VISIONPRESCRIPTION = "VisionPrescription"

    allowed_values = [APPOINTMENT, APPOINTMENTRESPONSE, CAREPLAN, CLAIM, COMMUNICATIONREQUEST, CONTRACT, DEVICEREQUEST, ENROLLMENTREQUEST, IMMUNIZATIONRECOMMENDATION, MEDICATIONREQUEST, NUTRITIONORDER, SERVICEREQUEST, SUPPLYREQUEST, TASK, VISIONPRESCRIPTION]