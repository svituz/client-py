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

class ImmunizationEvaluationDoseStatusReasonCodes(object):
    """ The value set to instantiate this attribute should be drawn from a terminologically robust code system that consists of
or contains concepts to support describing the reason why an administered dose has been assigned a particular status.
Often, this reason describes why a dose is considered invalid. This value set is provided as a suggestive example.
    URL: http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status-reason
    ValueSet: http://hl7.org/fhir/ValueSet/immunization-evaluation-dose-status-reason
    """
    # The product was stored in a manner inconsistent with manufacturer guidelines potentially reducing the
	/// effectiveness of the product.
    advstorage = "advstorage"
    # The product was stored at a temperature inconsistent with manufacturer guidelines potentially reducing the
	/// effectiveness of the product.
    coldchbrk = "coldchbrk"
    # The product was administered after the expiration date associated with lot of vaccine.
    explot = "explot"
    # The product was administered at a time inconsistent with the documented schedule.
    outsidesched = "outsidesched"
    # The product administered has been recalled by the manufacturer.
    prodrecall = "prodrecall"