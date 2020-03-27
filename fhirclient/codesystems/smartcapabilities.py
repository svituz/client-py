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
    """support for SMART’s EHR Launch mode."""
    LAUNCHEHR = "launch-ehr"
    """support for SMART’s Standalone Launch mode."""
    LAUNCHSTANDALONE = "launch-standalone"
    """support for SMART’s public client profile (no client authentication)."""
    CLIENTPUBLIC = "client-public"
    """support for SMART’s confidential client profile (symmetric client secret authentication)."""
    CLIENTCONFIDENTIALSYMMETRIC = "client-confidential-symmetric"
    """support for SMART’s OpenID Connect profile."""
    SSOOPENIDCONNECT = "sso-openid-connect"
    """support for “need patient banner” launch context (conveyed via need_patient_banner token parameter)."""
    CONTEXTPASSTHROUGHBANNER = "context-passthrough-banner"
    """support for “SMART style URL” launch context (conveyed via smart_style_url token parameter)."""
    CONTEXTPASSTHROUGHSTYLE = "context-passthrough-style"
    """support for patient-level launch context (requested by launch/patient scope, conveyed via patient token
	/// parameter)."""
    CONTEXTEHRPATIENT = "context-ehr-patient"
    """support for encounter-level launch context (requested by launch/encounter scope, conveyed via encounter token
	/// parameter)."""
    CONTEXTEHRENCOUNTER = "context-ehr-encounter"
    """support for patient-level launch context (requested by launch/patient scope, conveyed via patient token
	/// parameter)."""
    CONTEXTSTANDALONEPATIENT = "context-standalone-patient"
    """support for encounter-level launch context (requested by launch/encounter scope, conveyed via encounter token
	/// parameter)."""
    CONTEXTSTANDALONEENCOUNTER = "context-standalone-encounter"
    """support for refresh tokens (requested by offline_access scope)."""
    PERMISSIONOFFLINE = "permission-offline"
    """support for patient-level scopes (e.g. patient/Observation.read)."""
    PERMISSIONPATIENT = "permission-patient"
    """support for user-level scopes (e.g. user/Appointment.read)."""
    PERMISSIONUSER = "permission-user"
    allowed_values = ['LAUNCHEHR', 'LAUNCHSTANDALONE', 'CLIENTPUBLIC', 'CLIENTCONFIDENTIALSYMMETRIC', 'SSOOPENIDCONNECT', 'CONTEXTPASSTHROUGHBANNER', 'CONTEXTPASSTHROUGHSTYLE', 'CONTEXTEHRPATIENT', 'CONTEXTEHRENCOUNTER', 'CONTEXTSTANDALONEPATIENT', 'CONTEXTSTANDALONEENCOUNTER', 'PERMISSIONOFFLINE', 'PERMISSIONPATIENT', 'PERMISSIONUSER']