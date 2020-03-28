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

class ISO210892017HealthRecordLifecycleEvents(object):
    """ Attached is vocabulary for the 27 record lifecycle events, as per ISO TS 21089-2017, Health Informatics - Trusted End-
to-End Information Flows, Section 3, Terms and Definitions (2017, at ISO Central Secretariat, passed ballot and ready
for publication).  This will also be included in the FHIR EHR Record Lifecycle Event Implementation Guide, balloted and
(to be) published with FHIR STU-3.
    URL: http://terminology.hl7.org/CodeSystem/iso-21089-lifecycle
    """
    # Occurs when an agent causes the system to obtain and open a record entry for inspection or review.
    ACCESS = "access"
    # Occurs when an agent causes the system to tag or otherwise indicate special access management and suspension of
    # record entry deletion/destruction, if deemed relevant to a lawsuit or which are reasonably anticipated to be
    # relevant or to fulfill organizational policy under the legal doctrine of “duty to preserve”.
    HOLD = "hold"
    # Occurs when an agent makes any change to record entry content currently residing in storage considered permanent
    # (persistent).
    AMEND = "amend"
    # Occurs when an agent causes the system to create and move archive artifacts containing record entry content,
    # typically to long-term offline storage.
    ARCHIVE = "archive"
    # Occurs when an agent causes the system to capture the agent’s digital signature (or equivalent indication)
    # during formal validation of record entry content.
    ATTEST = "attest"
    # Occurs when an agent causes the system to decode record entry content from a cipher.
    DECRYPT = "decrypt"
    # Occurs when an agent causes the system to scrub record entry content to reduce the association between a set of
    # identifying data and the data subject in a way that might or might not be reversible.
    DEIDENTIFY = "deidentify"
    # Occurs when an agent causes the system to tag record entry(ies) as obsolete, erroneous or untrustworthy, to warn
    # against its future use.
    DEPRECATE = "deprecate"
    # Occurs when an agent causes the system to permanently erase record entry content from the system.
    DESTROY = "destroy"
    # Occurs when an agent causes the system to release, transfer, provision access to, or otherwise divulge record
    # entry content.
    DISCLOSE = "disclose"
    # Occurs when an agent causes the system to encode record entry content in a cipher.
    ENCRYPT = "encrypt"
    # Occurs when an agent causes the system to selectively pull out a subset of record entry content, based on
    # explicit criteria.
    EXTRACT = "extract"
    # Occurs when an agent causes the system to connect related record entries.
    LINK = "link"
    # Occurs when an agent causes the system to combine or join content from two or more record entries, resulting in
    # a single logical record entry.
    MERGE = "merge"
    # Occurs when an agent causes the system to: a) initiate capture of potential record content, and b) incorporate
    # that content into the storage considered a permanent part of the health record.
    ORIGINATE = "originate"
    # Occurs when an agent causes the system to remove record entry content to reduce the association between a set of
    # identifying data and the data subject in a way that may be reversible.
    PSEUDONYMIZE = "pseudonymize"
    # Occurs when an agent causes the system to recreate or restore full status to record entries previously deleted
    # or deprecated.
    REACTIVATE = "reactivate"
    # Occurs when an agent causes the system to a) initiate capture of data content from elsewhere, and b) incorporate
    # that content into the storage considered a permanent part of the health record.
    RECEIVE = "receive"
    # Occurs when an agent causes the system to restore information to data that allows identification of information
    # source and/or information subject.
    REIDENTIFY = "reidentify"
    # Occurs when an agent causes the system to remove a tag or other cues for special access management had required
    # to fulfill organizational policy under the legal doctrine of “duty to preserve”.
    UNHOLD = "unhold"
    # Occurs when an agent causes the system to produce and deliver record entry content in a particular form and
    # manner.
    REPORT = "report"
    # Occurs when an agent causes the system to recreate record entries and their content from a previous created
    # archive artefact.
    RESTORE = "restore"
    # Occurs when an agent causes the system to change the form, language or code system used to represent record
    # entry content.
    TRANSFORM = "transform"
    # Occurs when an agent causes the system to send record entry content from one (EHR/PHR/other) system to another.
    TRANSMIT = "transmit"
    # Occurs when an agent causes the system to disconnect two or more record entries previously connected, rendering
    # them separate (disconnected) again.
    UNLINK = "unlink"
    # Occurs when an agent causes the system to reverse a previous record entry merge operation, rendering them
    # separate again.
    UNMERGE = "unmerge"
    # Occurs when an agent causes the system to confirm compliance of data or data objects with regulations,
    # requirements, specifications, or other imposed conditions based on organizational policy.
    VERIFY = "verify"

    allowed_values = [ACCESS, HOLD, AMEND, ARCHIVE, ATTEST, DECRYPT, DEIDENTIFY, DEPRECATE, DESTROY, DISCLOSE, ENCRYPT, EXTRACT, LINK, MERGE, ORIGINATE, PSEUDONYMIZE, REACTIVATE, RECEIVE, REIDENTIFY, UNHOLD, REPORT, RESTORE, TRANSFORM, TRANSMIT, UNLINK, UNMERGE, VERIFY]