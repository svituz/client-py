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

class BasicResourceTypes(object):
    """ This value set defines codes for resources not yet supported by (or which will never be supported by) FHIR.  Many of the
codes listed here will eventually be turned into official resources.  However, there is no guarantee that any particular
resource will be created nor that the scope will be exactly as defined by the codes presented here.  Codes in this set
will be deprecated if/when formal resources are defined that encompass these concepts.
    URL: http://terminology.hl7.org/CodeSystem/basic-resource-type
    ValueSet: http://hl7.org/fhir/ValueSet/basic-resource-type
    """
    # An assertion of permission for an activity or set of activities to occur, possibly subject to particular
	/// limitations; e.g. surgical consent, information disclosure consent, etc.
    consent = "consent"
    # A request that care of a particular type be provided to a patient.  Could involve the transfer of care, a
	/// consult, etc.
    referral = "referral"
    # An undesired reaction caused by exposure to some agent (e.g. a medication, immunization, food, or environmental
	/// agent).
    advevent = "advevent"
    # A request that a time be scheduled for a type of service for a specified patient, potentially subject to other
	/// constraints
    aptmtreq = "aptmtreq"
    # The transition of a patient or set of material from one location to another
    transfer = "transfer"
    # The specification of a set of food and/or other nutritional material to be delivered to a patient.
    diet = "diet"
    # An occurrence of a non-care-related event in the healthcare domain, such as approvals, reviews, etc.
    adminact = "adminact"
    # Record of a situation where a subject was exposed to a substance.  Usually of interest to public health.
    exposure = "exposure"
    # A formalized inquiry into the circumstances surrounding a particular unplanned event or potential event for the
	/// purposes of identifying possible causes and contributing factors for the event
    investigation = "investigation"
    # A financial instrument used to track costs, charges or other amounts.
    account = "account"
    # A request for payment for goods and/or services.  Includes the idea of a healthcare insurance claim.
    invoice = "invoice"
    # The determination of what will be paid against a particular invoice based on coverage, plan rules, etc.
    adjudicat = "adjudicat"
    # A request for a pre-determination of the cost that would be paid under an insurance plan for a hypothetical
	/// claim for goods or services
    predetreq = "predetreq"
    # An adjudication of what would be paid under an insurance plan for a hypothetical claim for goods or services
    predetermine = "predetermine"
    # An investigation to determine information about a particular therapy or product
    study = "study"
    # A set of (possibly conditional) steps to be taken to achieve some aim.  Includes study protocols, treatment
	/// protocols, emergency protocols, etc.
    protocol = "protocol"