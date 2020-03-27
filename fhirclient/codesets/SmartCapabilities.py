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

class SmartCapabilities(object):
    """ Codes that define what the server is capable of.
    URL: http://terminology.hl7.org/CodeSystem/smart-capabilities
    ValueSet: http://hl7.org/fhir/ValueSet/smart-capabilities
    """
    # support for SMART’s EHR Launch mode.
    launchEhr = "launch-ehr"
    # support for SMART’s Standalone Launch mode.
    launchStandalone = "launch-standalone"
    # support for SMART’s public client profile (no client authentication).
    clientPublic = "client-public"
    # support for SMART’s confidential client profile (symmetric client secret authentication).
    clientConfidentialSymmetric = "client-confidential-symmetric"
    # support for SMART’s OpenID Connect profile.
    ssoOpenidConnect = "sso-openid-connect"
    # support for “need patient banner” launch context (conveyed via need_patient_banner token parameter).
    contextPassthroughBanner = "context-passthrough-banner"
    # support for “SMART style URL” launch context (conveyed via smart_style_url token parameter).
    contextPassthroughStyle = "context-passthrough-style"
    # support for patient-level launch context (requested by launch/patient scope, conveyed via patient token
	/// parameter).
    contextEhrPatient = "context-ehr-patient"
    # support for encounter-level launch context (requested by launch/encounter scope, conveyed via encounter token
	/// parameter).
    contextEhrEncounter = "context-ehr-encounter"
    # support for patient-level launch context (requested by launch/patient scope, conveyed via patient token
	/// parameter).
    contextStandalonePatient = "context-standalone-patient"
    # support for encounter-level launch context (requested by launch/encounter scope, conveyed via encounter token
	/// parameter).
    contextStandaloneEncounter = "context-standalone-encounter"
    # support for refresh tokens (requested by offline_access scope).
    permissionOffline = "permission-offline"
    # support for patient-level scopes (e.g. patient/Observation.read).
    permissionPatient = "permission-patient"
    # support for user-level scopes (e.g. user/Appointment.read).
    permissionUser = "permission-user"