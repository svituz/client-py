#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Claim)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Claim(domainresource.DomainResource):
    """ Claim, Pre-determination or Pre-authorization.
    
    A provider issued list of professional services and products which have
    been provided, or are to be provided, to a patient which is sent to an
    insurer for reimbursement.
    """
    
    resource_type = "Claim"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier for claim.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.type = None
        """ Category or discipline.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subType = None
        """ More granular claim type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.use = None
        """ claim | preauthorization | predetermination.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.patient = None
        """ The recipient of the products and services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.billablePeriod = None
        """ Relevant time frame for the claim.
        Type `Period` (represented as `dict` in JSON). """
        
        self.created = None
        """ Resource creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.enterer = None
        """ Author of the claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.insurer = None
        """ Target.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Party responsible for the claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priority = None
        """ Desired processing ugency.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.fundsReserve = None
        """ For whom to reserve funds.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.related = None
        """ Prior or corollary claims.
        List of `ClaimRelated` items (represented as `dict` in JSON). """
        
        self.prescription = None
        """ Prescription authorizing services and products.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.originalPrescription = None
        """ Original prescription if superseded by fulfiller.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.payee = None
        """ Recipient of benefits payable.
        Type `ClaimPayee` (represented as `dict` in JSON). """
        
        self.referral = None
        """ Treatment referral.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.facility = None
        """ Servicing facility.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.careTeam = None
        """ Members of the care team.
        List of `ClaimCareTeam` items (represented as `dict` in JSON). """
        
        self.supportingInfo = None
        """ Supporting information.
        List of `ClaimSupportingInfo` items (represented as `dict` in JSON). """
        
        self.diagnosis = None
        """ Pertinent diagnosis information.
        List of `ClaimDiagnosis` items (represented as `dict` in JSON). """
        
        self.procedure = None
        """ Clinical procedures performed.
        List of `ClaimProcedure` items (represented as `dict` in JSON). """
        
        self.insurance = None
        """ Patient insurance information.
        List of `ClaimInsurance` items (represented as `dict` in JSON). """
        
        self.accident = None
        """ Details of the event.
        Type `ClaimAccident` (represented as `dict` in JSON). """
        
        self.item = None
        """ Product or service provided.
        List of `ClaimItem` items (represented as `dict` in JSON). """
        
        self.total = None
        """ Total claim cost.
        Type `Money` (represented as `dict` in JSON). """
        
        super(Claim, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Claim, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, financialresourcestatuscodes.FinancialResourceStatusCodes), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False, None), 
            ("use", "use", fhirdatatypes.FHIRCode, False, None, True, use.Use), 
            ("patient", "patient", fhirreference.FHIRReference, False, None, True, None), 
            ("billablePeriod", "billablePeriod", period.Period, False, None, False, None), 
            ("created", "created", fhirdatatypes.FHIRDateTime, False, None, True, None), 
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False, None), 
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False, None), 
            ("provider", "provider", fhirreference.FHIRReference, False, None, True, None), 
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, True, None), 
            ("fundsReserve", "fundsReserve", codeableconcept.CodeableConcept, False, None, False, None), 
            ("related", "related", ClaimRelated, True, None, False, None), 
            ("prescription", "prescription", fhirreference.FHIRReference, False, None, False, None), 
            ("originalPrescription", "originalPrescription", fhirreference.FHIRReference, False, None, False, None), 
            ("payee", "payee", ClaimPayee, False, None, False, None), 
            ("referral", "referral", fhirreference.FHIRReference, False, None, False, None), 
            ("facility", "facility", fhirreference.FHIRReference, False, None, False, None), 
            ("careTeam", "careTeam", ClaimCareTeam, True, None, False, None), 
            ("supportingInfo", "supportingInfo", ClaimSupportingInfo, True, None, False, None), 
            ("diagnosis", "diagnosis", ClaimDiagnosis, True, None, False, None), 
            ("procedure", "procedure", ClaimProcedure, True, None, False, None), 
            ("insurance", "insurance", ClaimInsurance, True, None, True, None), 
            ("accident", "accident", ClaimAccident, False, None, False, None), 
            ("item", "item", ClaimItem, True, None, False, None), 
            ("total", "total", money.Money, False, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class ClaimAccident(backboneelement.BackboneElement):
    """ Details of the event.
    
    Details of an accident which resulted in injuries which required the
    products and services listed in the claim.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ When the incident occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.type = None
        """ The nature of the accident.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.locationAddress = None
        """ Where the event occurred.
        Type `Address` (represented as `dict` in JSON). """
        
        self.locationReference = None
        """ Where the event occurred.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ClaimAccident, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimAccident, self).elementProperties()
        js.extend([
            ("date", "date", fhirdatatypes.FHIRDate, False, None, True, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("locationAddress", "locationAddress", address.Address, False, "location", False, None), 
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False, None), 
        ])
        return js




class ClaimCareTeam(backboneelement.BackboneElement):
    """ Members of the care team.
    
    The members of the team who provided the products and services.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequence = None
        """ Order of care team.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.provider = None
        """ Practitioner or organization.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.responsible = None
        """ Indicator of the lead practitioner.
        Type `bool`. """
        
        self.role = None
        """ Function within the team.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.qualification = None
        """ Practitioner credential or specialization.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimCareTeam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimCareTeam, self).elementProperties()
        js.extend([
            ("sequence", "sequence", fhirdatatypes.FHIRPositiveInt, False, None, True, None), 
            ("provider", "provider", fhirreference.FHIRReference, False, None, True, None), 
            ("responsible", "responsible", bool, False, None, False, None), 
            ("role", "role", codeableconcept.CodeableConcept, False, None, False, None), 
            ("qualification", "qualification", codeableconcept.CodeableConcept, False, None, False, None), 
        ])
        return js




class ClaimDiagnosis(backboneelement.BackboneElement):
    """ Pertinent diagnosis information.
    
    Information about diagnoses relevant to the claim items.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequence = None
        """ Diagnosis instance identifier.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.diagnosisCodeableConcept = None
        """ Nature of illness or problem.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.diagnosisReference = None
        """ Nature of illness or problem.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ Timing or nature of the diagnosis.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.onAdmission = None
        """ Present on admission.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.packageCode = None
        """ Package billing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimDiagnosis, self).elementProperties()
        js.extend([
            ("sequence", "sequence", fhirdatatypes.FHIRPositiveInt, False, None, True, None), 
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, False, "diagnosis", True, None), 
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, False, "diagnosis", True, None), 
            ("type", "type", codeableconcept.CodeableConcept, True, None, False, None), 
            ("onAdmission", "onAdmission", codeableconcept.CodeableConcept, False, None, False, None), 
            ("packageCode", "packageCode", codeableconcept.CodeableConcept, False, None, False, None), 
        ])
        return js




class ClaimInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.
    
    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequence = None
        """ Insurance instance identifier.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.focal = None
        """ Coverage to be used for adjudication.
        Type `bool`. """
        
        self.identifier = None
        """ Pre-assigned Claim number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.businessArrangement = None
        """ Additional provider contract number.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.preAuthRef = None
        """ Prior authorization reference number.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.claimResponse = None
        """ Adjudication results.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ClaimInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimInsurance, self).elementProperties()
        js.extend([
            ("sequence", "sequence", fhirdatatypes.FHIRPositiveInt, False, None, True, None), 
            ("focal", "focal", bool, False, None, True, None), 
            ("identifier", "identifier", identifier.Identifier, False, None, False, None), 
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True, None), 
            ("businessArrangement", "businessArrangement", fhirdatatypes.FHIRString, False, None, False, None), 
            ("preAuthRef", "preAuthRef", fhirdatatypes.FHIRString, True, None, False, None), 
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js




class ClaimItem(backboneelement.BackboneElement):
    """ Product or service provided.
    
    A claim line. Either a simple  product or service or a 'group' of details
    which can each be a simple items or groups of sub-details.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequence = None
        """ Item instance identifier.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.careTeamSequence = None
        """ Applicable careTeam members.
        List of `FHIRPositiveInt` items (represented as `int` in JSON). """
        
        self.diagnosisSequence = None
        """ Applicable diagnoses.
        List of `FHIRPositiveInt` items (represented as `int` in JSON). """
        
        self.procedureSequence = None
        """ Applicable procedures.
        List of `FHIRPositiveInt` items (represented as `int` in JSON). """
        
        self.informationSequence = None
        """ Applicable exception and supporting information.
        List of `FHIRPositiveInt` items (represented as `int` in JSON). """
        
        self.revenue = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.modifier = None
        """ Product or service billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.programCode = None
        """ Program the product or service is provided under.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.servicedDate = None
        """ Date or dates of service or product delivery.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        """ Date or dates of service or product delivery.
        Type `Period` (represented as `dict` in JSON). """
        
        self.locationCodeableConcept = None
        """ Place of service or where product was supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.locationAddress = None
        """ Place of service or where product was supplied.
        Type `Address` (represented as `dict` in JSON). """
        
        self.locationReference = None
        """ Place of service or where product was supplied.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique device identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Anatomical location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subSite = None
        """ Anatomical sub-location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounters related to this billed item.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.detail = None
        """ Product or service provided.
        List of `ClaimItemDetail` items (represented as `dict` in JSON). """
        
        super(ClaimItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimItem, self).elementProperties()
        js.extend([
            ("sequence", "sequence", fhirdatatypes.FHIRPositiveInt, False, None, True, None), 
            ("careTeamSequence", "careTeamSequence", fhirdatatypes.FHIRPositiveInt, True, None, False, None), 
            ("diagnosisSequence", "diagnosisSequence", fhirdatatypes.FHIRPositiveInt, True, None, False, None), 
            ("procedureSequence", "procedureSequence", fhirdatatypes.FHIRPositiveInt, True, None, False, None), 
            ("informationSequence", "informationSequence", fhirdatatypes.FHIRPositiveInt, True, None, False, None), 
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False, None), 
            ("category", "category", codeableconcept.CodeableConcept, False, None, False, None), 
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True, None), 
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False, None), 
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("servicedDate", "servicedDate", fhirdatatypes.FHIRDate, False, "serviced", False, None), 
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False, None), 
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, False, "location", False, None), 
            ("locationAddress", "locationAddress", address.Address, False, "location", False, None), 
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False, None), 
            ("quantity", "quantity", quantity.Quantity, False, None, False, None), 
            ("unitPrice", "unitPrice", money.Money, False, None, False, None), 
            ("factor", "factor", float, False, None, False, None), 
            ("net", "net", money.Money, False, None, False, None), 
            ("udi", "udi", fhirreference.FHIRReference, True, None, False, None), 
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False, None), 
            ("subSite", "subSite", codeableconcept.CodeableConcept, True, None, False, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, True, None, False, None), 
            ("detail", "detail", ClaimItemDetail, True, None, False, None), 
        ])
        return js




class ClaimItemDetail(backboneelement.BackboneElement):
    """ Product or service provided.
    
    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequence = None
        """ Item instance identifier.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.revenue = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.programCode = None
        """ Program the product or service is provided under.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique device identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.subDetail = None
        """ Product or service provided.
        List of `ClaimItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        super(ClaimItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimItemDetail, self).elementProperties()
        js.extend([
            ("sequence", "sequence", fhirdatatypes.FHIRPositiveInt, False, None, True, None), 
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False, None), 
            ("category", "category", codeableconcept.CodeableConcept, False, None, False, None), 
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True, None), 
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False, None), 
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("quantity", "quantity", quantity.Quantity, False, None, False, None), 
            ("unitPrice", "unitPrice", money.Money, False, None, False, None), 
            ("factor", "factor", float, False, None, False, None), 
            ("net", "net", money.Money, False, None, False, None), 
            ("udi", "udi", fhirreference.FHIRReference, True, None, False, None), 
            ("subDetail", "subDetail", ClaimItemDetailSubDetail, True, None, False, None), 
        ])
        return js




class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    """ Product or service provided.
    
    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequence = None
        """ Item instance identifier.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.revenue = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.programCode = None
        """ Program the product or service is provided under.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique device identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ClaimItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("sequence", "sequence", fhirdatatypes.FHIRPositiveInt, False, None, True, None), 
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False, None), 
            ("category", "category", codeableconcept.CodeableConcept, False, None, False, None), 
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True, None), 
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False, None), 
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("quantity", "quantity", quantity.Quantity, False, None, False, None), 
            ("unitPrice", "unitPrice", money.Money, False, None, False, None), 
            ("factor", "factor", float, False, None, False, None), 
            ("net", "net", money.Money, False, None, False, None), 
            ("udi", "udi", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js




class ClaimPayee(backboneelement.BackboneElement):
    """ Recipient of benefits payable.
    
    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Category of recipient.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.party = None
        """ Recipient reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ClaimPayee, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimPayee, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
            ("party", "party", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js




class ClaimProcedure(backboneelement.BackboneElement):
    """ Clinical procedures performed.
    
    Procedures performed on the patient relevant to the billing items with the
    claim.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequence = None
        """ Procedure instance identifier.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.type = None
        """ Category of Procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.date = None
        """ When the procedure was performed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.procedureCodeableConcept = None
        """ Specific clinical procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.procedureReference = None
        """ Specific clinical procedure.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique device identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ClaimProcedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimProcedure, self).elementProperties()
        js.extend([
            ("sequence", "sequence", fhirdatatypes.FHIRPositiveInt, False, None, True, None), 
            ("type", "type", codeableconcept.CodeableConcept, True, None, False, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("procedureCodeableConcept", "procedureCodeableConcept", codeableconcept.CodeableConcept, False, "procedure", True, None), 
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, False, "procedure", True, None), 
            ("udi", "udi", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js




class ClaimRelated(backboneelement.BackboneElement):
    """ Prior or corollary claims.
    
    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.claim = None
        """ Reference to the related claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ How the reference claim is related.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reference = None
        """ File or case reference.
        Type `Identifier` (represented as `dict` in JSON). """
        
        super(ClaimRelated, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimRelated, self).elementProperties()
        js.extend([
            ("claim", "claim", fhirreference.FHIRReference, False, None, False, None), 
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False, None), 
            ("reference", "reference", identifier.Identifier, False, None, False, None), 
        ])
        return js




class ClaimSupportingInfo(backboneelement.BackboneElement):
    """ Supporting information.
    
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequence = None
        """ Information instance identifier.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.category = None
        """ Classification of the supplied information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Type of information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.timingDate = None
        """ When it occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None
        """ When it occurred.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueBoolean = None
        """ Data to be provided.
        Type `bool`. """
        
        self.valueString = None
        """ Data to be provided.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueQuantity = None
        """ Data to be provided.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ Data to be provided.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Data to be provided.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Explanation for the information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimSupportingInfo, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimSupportingInfo, self).elementProperties()
        js.extend([
            ("sequence", "sequence", fhirdatatypes.FHIRPositiveInt, False, None, True, None), 
            ("category", "category", codeableconcept.CodeableConcept, False, None, True, None), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("timingDate", "timingDate", fhirdatatypes.FHIRDate, False, "timing", False, None), 
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False, None), 
            ("valueBoolean", "valueBoolean", bool, False, "value", False, None), 
            ("valueString", "valueString", fhirdatatypes.FHIRString, False, "value", False, None), 
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False, None), 
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False, None), 
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False, None), 
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False, None), 
        ])
        return js



from fhirclient.models import address

from fhirclient.models import attachment

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.codesystems import financialresourcestatuscodes

from fhirclient.models import identifier

from fhirclient.models import money

from fhirclient.models import period

from fhirclient.models import quantity

from fhirclient.codesystems import use

