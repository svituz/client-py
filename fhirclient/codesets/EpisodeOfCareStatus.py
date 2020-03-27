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

class EpisodeOfCareStatus(object):
    """ The status of the episode of care.
    URL: http://hl7.org/fhir/episode-of-care-status
    ValueSet: http://hl7.org/fhir/ValueSet/episode-of-care-status
    """
    # This episode of care is planned to start at the date specified in the period.start. During this status, an
	/// organization may perform assessments to determine if the patient is eligible to receive services, or be
	/// organizing to make resources available to provide care services.
    planned = "planned"
    # This episode has been placed on a waitlist, pending the episode being made active (or cancelled).
    waitlist = "waitlist"
    # This episode of care is current.
    active = "active"
    # This episode of care is on hold; the organization has limited responsibility for the patient (such as while on
	/// respite).
    onhold = "onhold"
    # This episode of care is finished and the organization is not expecting to be providing further care to the
	/// patient. Can also be known as "closed", "completed" or other similar terms.
    finished = "finished"
    # The episode of care was cancelled, or withdrawn from service, often selected during the planned stage as the
	/// patient may have gone elsewhere, or the circumstances have changed and the organization is unable to provide the
	/// care. It indicates that services terminated outside the planned/expected workflow.
    cancelled = "cancelled"
    # This instance should not have been part of this patient's medical record.
    enteredInError = "entered-in-error"