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

class MedicationDispenseStatusReasonCodes(object):
    """ MedicationDispense Status Codes
    URL: http://terminology.hl7.org/fhir/CodeSystem/medicationdispense-status-reason
    ValueSet: http://hl7.org/fhir/ValueSet/medicationdispense-status-reason
    """
    # The order has been stopped by the prescriber but this fact has not necessarily captured electronically. Example:
    # A verbal stop, a fax, etc.
    FRR01 = "frr01"
    # Order has not been fulfilled within a reasonable amount of time, and might not be current.
    FRR02 = "frr02"
    # Data needed to safely act on the order which was expected to become available independent of the order is not
    # yet available. Example: Lab results, diagnostic imaging, etc.
    FRR03 = "frr03"
    # Product not available or manufactured. Cannot supply.
    FRR04 = "frr04"
    # The dispenser has ethical, religious or moral objections to fulfilling the order/dispensing the product.
    FRR05 = "frr05"
    # Fulfiller not able to provide appropriate care associated with fulfilling the order. Example: Therapy requires
    # ongoing monitoring by fulfiller and fulfiller will be ending practice, leaving town, unable to schedule
    # necessary time, etc.
    FRR06 = "frr06"
    # This therapy has been ordered as a backup to a preferred therapy. This order will be released when and if the
    # preferred therapy is unsuccessful.
    ALTCHOICE = "altchoice"
    # Clarification is required before the order can be acted upon.
    CLARIF = "clarif"
    # The current level of the medication in the patient's system is too high. The medication is suspended to allow
    # the level to subside to a safer level.
    DRUGHIGH = "drughigh"
    # The patient has been admitted to a care facility and their community medications are suspended until hospital
    # discharge.
    HOSPADM = "hospadm"
    # The therapy would interfere with a planned lab test and the therapy is being withdrawn until the test is
    # completed.
    LABINT = "labint"
    # Patient not available for a period of time due to a scheduled therapy, leave of absence or other reason.
    NONAVAIL = "non-avail"
    # The patient is pregnant or breast feeding. The therapy will be resumed when the pregnancy is complete and the
    # patient is no longer breastfeeding.
    PREG = "preg"
    # The patient is believed to be allergic to a substance that is part of the therapy and the therapy is being
    # temporarily withdrawn to confirm.
    SAIG = "saig"
    # The drug interacts with a short-term treatment that is more urgently required. This order will be resumed when
    # the short-term treatment is complete.
    SDDI = "sddi"
    # Another short-term co-occurring therapy fulfills the same purpose as this therapy. This therapy will be resumed
    # when the co-occuring therapy is complete.
    SDUPTHER = "sdupther"
    # The patient is believed to have an intolerance to a substance that is part of the therapy and the therapy is
    # being temporarily withdrawn to confirm.
    SINTOL = "sintol"
    # The drug is contraindicated for patients receiving surgery and the patient is scheduled to be admitted for
    # surgery in the near future. The drug will be resumed when the patient has sufficiently recovered from the
    # surgery.
    SURG = "surg"
    # The patient was previously receiving a medication contraindicated with the current medication. The current
    # medication will remain on hold until the prior medication has been cleansed from their system.
    WASHOUT = "washout"
    # Drug out of stock. Cannot supply.
    OUTOFSTOCK = "outofstock"
    # Drug no longer marketed Cannot supply.
    OFFMARKET = "offmarket"

    allowed_values = [FRR01, FRR02, FRR03, FRR04, FRR05, FRR06, ALTCHOICE, CLARIF, DRUGHIGH, HOSPADM, LABINT, NONAVAIL, PREG, SAIG, SDDI, SDUPTHER, SINTOL, SURG, WASHOUT, OUTOFSTOCK, OFFMARKET]