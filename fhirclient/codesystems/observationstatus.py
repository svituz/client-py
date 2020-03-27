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

class ObservationStatus(object):
    """ Codes providing the status of an observation.
    URL: http://hl7.org/fhir/observation-status
    ValueSet: http://hl7.org/fhir/ValueSet/observation-status
    """
    """The existence of the observation is registered, but there is no result yet available."""
    REGISTERED = "registered"
    """This is an initial or interim observation: data may be incomplete or unverified."""
    PRELIMINARY = "preliminary"
    """The observation is complete and there are no further actions needed. Additional information such "released",
	/// "signed", etc would be represented using [Provenance](provenance.html) which provides not only the act but also
	/// the actors and dates and other related data. These act states would be associated with an observation status of
	/// `preliminary` until they are all completed and then a status of `final` would be applied."""
    FINAL = "final"
    """Subsequent to being Final, the observation has been modified subsequent.  This includes updates/new information
	/// and corrections."""
    AMENDED = "amended"
    """Subsequent to being Final, the observation has been modified to correct an error in the test result."""
    CORRECTED = "corrected"
    """The observation is unavailable because the measurement was not started or not completed (also sometimes called
	/// "aborted")."""
    CANCELLED = "cancelled"
    """The observation has been withdrawn following previous final release.  This electronic record should never have
	/// existed, though it is possible that real-world decisions were based on it. (If real-world activity has occurred,
	/// the status should be "cancelled" rather than "entered-in-error".)."""
    ENTEREDINERROR = "entered-in-error"
    """The authoring/source system does not know which of the status values currently applies for this observation.
	/// Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the
	/// authoring/source system does not know which."""
    UNKNOWN = "unknown"
    allowed_values = ['REGISTERED', 'PRELIMINARY', 'FINAL', 'AMENDED', 'CORRECTED', 'CANCELLED', 'ENTEREDINERROR', 'UNKNOWN']