#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Contract)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Contract(domainresource.DomainResource):
    """ Legal Agreement.
    
    Legally enforceable, formally recorded unilateral or bilateral directive
    i.e., a policy or agreement.
    """
    
    resource_type = "Contract"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Contract number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.url = None
        """ Basal definition.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.version = None
        """ Business edition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.status = None
        """ amended | appended | cancelled | disputed | entered-in-error |
        executable | executed | negotiable | offered | policy | rejected |
        renewed | revoked | resolved | terminated.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.legalState = None
        """ Negotiation status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ Source Contract Definition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.instantiatesUri = None
        """ External Contract Definition.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.contentDerivative = None
        """ Content derived from the basal information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.issued = None
        """ When this Contract was issued.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.applies = None
        """ Effective time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.expirationType = None
        """ Contract cessation cause.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Contract Target Entity.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.authority = None
        """ Authority under which this Contract has standing.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.domain = None
        """ A sphere of control governed by an authoritative jurisdiction,
        organization, or person.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.site = None
        """ Specific Location.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Computer friendly designation.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Human Friendly name.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.subtitle = None
        """ Subordinate Friendly name.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.alias = None
        """ Acronym or short name.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.author = None
        """ Source of Contract.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.scope = None
        """ Range of Legal Concerns.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.topicCodeableConcept = None
        """ Focus of contract interest.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.topicReference = None
        """ Focus of contract interest.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ Legal instrument category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subType = None
        """ Subtype within the context of type.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.contentDefinition = None
        """ Contract precursor content.
        Type `ContractContentDefinition` (represented as `dict` in JSON). """
        
        self.term = None
        """ Contract Term List.
        List of `ContractTerm` items (represented as `dict` in JSON). """
        
        self.supportingInfo = None
        """ Extra Information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.relevantHistory = None
        """ Key event in Contract History.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.signer = None
        """ Contract Signatory.
        List of `ContractSigner` items (represented as `dict` in JSON). """
        
        self.friendly = None
        """ Contract Friendly Language.
        List of `ContractFriendly` items (represented as `dict` in JSON). """
        
        self.legal = None
        """ Contract Legal Language.
        List of `ContractLegal` items (represented as `dict` in JSON). """
        
        self.rule = None
        """ Computable Contract Language.
        List of `ContractRule` items (represented as `dict` in JSON). """
        
        self.legallyBindingAttachment = None
        """ Binding Contract.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.legallyBindingReference = None
        """ Binding Contract.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(Contract, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Contract, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, False, contractresourcestatuscodes.ContractResourceStatusCodes), 
            ("legalState", "legalState", codeableconcept.CodeableConcept, False, None, False, None), 
            ("instantiatesCanonical", "instantiatesCanonical", fhirreference.FHIRReference, False, None, False, None), 
            ("instantiatesUri", "instantiatesUri", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("contentDerivative", "contentDerivative", codeableconcept.CodeableConcept, False, None, False, None), 
            ("issued", "issued", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("applies", "applies", period.Period, False, None, False, None), 
            ("expirationType", "expirationType", codeableconcept.CodeableConcept, False, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, True, None, False, None), 
            ("authority", "authority", fhirreference.FHIRReference, True, None, False, None), 
            ("domain", "domain", fhirreference.FHIRReference, True, None, False, None), 
            ("site", "site", fhirreference.FHIRReference, True, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("subtitle", "subtitle", fhirdatatypes.FHIRString, False, None, False, None), 
            ("alias", "alias", fhirdatatypes.FHIRString, True, None, False, None), 
            ("author", "author", fhirreference.FHIRReference, False, None, False, None), 
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, False, None), 
            ("topicCodeableConcept", "topicCodeableConcept", codeableconcept.CodeableConcept, False, "topic", False, None), 
            ("topicReference", "topicReference", fhirreference.FHIRReference, False, "topic", False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("subType", "subType", codeableconcept.CodeableConcept, True, None, False, None), 
            ("contentDefinition", "contentDefinition", ContractContentDefinition, False, None, False, None), 
            ("term", "term", ContractTerm, True, None, False, None), 
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False, None), 
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False, None), 
            ("signer", "signer", ContractSigner, True, None, False, None), 
            ("friendly", "friendly", ContractFriendly, True, None, False, None), 
            ("legal", "legal", ContractLegal, True, None, False, None), 
            ("rule", "rule", ContractRule, True, None, False, None), 
            ("legallyBindingAttachment", "legallyBindingAttachment", attachment.Attachment, False, "legallyBinding", False, None), 
            ("legallyBindingReference", "legallyBindingReference", fhirreference.FHIRReference, False, "legallyBinding", False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class ContractContentDefinition(backboneelement.BackboneElement):
    """ Contract precursor content.
    
    Precusory content developed with a focus and intent of supporting the
    formation a Contract instance, which may be associated with and
    transformable into a Contract.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Content structure and use.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subType = None
        """ Detailed Content Type Definition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.publisher = None
        """ Publisher Entity.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.publicationDate = None
        """ When published.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.publicationStatus = None
        """ amended | appended | cancelled | disputed | entered-in-error |
        executable | executed | negotiable | offered | policy | rejected |
        renewed | revoked | resolved | terminated.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.copyright = None
        """ Publication Ownership.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        super(ContractContentDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractContentDefinition, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False, None), 
            ("publisher", "publisher", fhirreference.FHIRReference, False, None, False, None), 
            ("publicationDate", "publicationDate", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("publicationStatus", "publicationStatus", fhirdatatypes.FHIRCode, False, None, True, contractresourcepublicationstatuscodes.ContractResourcePublicationStatusCodes), 
            ("copyright", "copyright", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
        ])
        return js




class ContractFriendly(backboneelement.BackboneElement):
    """ Contract Friendly Language.
    
    The "patient friendly language" versionof the Contract in whole or in
    parts. "Patient friendly language" means the representation of the Contract
    and Contract Provisions in a manner that is readily accessible and
    understandable by a layperson in accordance with best practices for
    communication styles that ensure that those agreeing to or signing the
    Contract understand the roles, actions, obligations, responsibilities, and
    implication of the agreement.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment = None
        """ Easily comprehended representation of this Contract.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Easily comprehended representation of this Contract.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractFriendly, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractFriendly, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True, None), 
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True, None), 
        ])
        return js




class ContractLegal(backboneelement.BackboneElement):
    """ Contract Legal Language.
    
    List of Legal expressions or representations of this Contract.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment = None
        """ Contract Legal Text.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Contract Legal Text.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractLegal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractLegal, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True, None), 
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True, None), 
        ])
        return js




class ContractRule(backboneelement.BackboneElement):
    """ Computable Contract Language.
    
    List of Computable Policy Rule Language Representations of this Contract.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment = None
        """ Computable Contract Rules.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Computable Contract Rules.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractRule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractRule, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True, None), 
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True, None), 
        ])
        return js




class ContractSigner(backboneelement.BackboneElement):
    """ Contract Signatory.
    
    Parties with legal standing in the Contract, including the principal
    parties, the grantor(s) and grantee(s), which are any person or
    organization bound by the contract, and any ancillary parties, which
    facilitate the execution of the contract such as a notary or witness.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Contract Signatory Role.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.party = None
        """ Contract Signatory Party.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.signature = None
        """ Contract Documentation Signature.
        List of `Signature` items (represented as `dict` in JSON). """
        
        super(ContractSigner, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractSigner, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, False, None, True, None), 
            ("party", "party", fhirreference.FHIRReference, False, None, True, None), 
            ("signature", "signature", signature.Signature, True, None, True, None), 
        ])
        return js




class ContractTerm(backboneelement.BackboneElement):
    """ Contract Term List.
    
    One or more Contract Provisions, which may be related and conveyed as a
    group, and may contain nested groups.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Contract Term Number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.issued = None
        """ Contract Term Issue Date Time.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.applies = None
        """ Contract Term Effective Time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.topicCodeableConcept = None
        """ Term Concern.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.topicReference = None
        """ Term Concern.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ Contract Term Type or Form.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subType = None
        """ Contract Term Type specific classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text = None
        """ Term Statement.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.securityLabel = None
        """ Protection for the Term.
        List of `ContractTermSecurityLabel` items (represented as `dict` in JSON). """
        
        self.offer = None
        """ Context of the Contract term.
        Type `ContractTermOffer` (represented as `dict` in JSON). """
        
        self.asset = None
        """ Contract Term Asset List.
        List of `ContractTermAsset` items (represented as `dict` in JSON). """
        
        self.action = None
        """ Entity being ascribed responsibility.
        List of `ContractTermAction` items (represented as `dict` in JSON). """
        
        self.group = None
        """ Nested Contract Term Group.
        List of `ContractTerm` items (represented as `dict` in JSON). """
        
        super(ContractTerm, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTerm, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False, None), 
            ("issued", "issued", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("applies", "applies", period.Period, False, None, False, None), 
            ("topicCodeableConcept", "topicCodeableConcept", codeableconcept.CodeableConcept, False, "topic", False, None), 
            ("topicReference", "topicReference", fhirreference.FHIRReference, False, "topic", False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False, None), 
            ("text", "text", fhirdatatypes.FHIRString, False, None, False, None), 
            ("securityLabel", "securityLabel", ContractTermSecurityLabel, True, None, False, None), 
            ("offer", "offer", ContractTermOffer, False, None, True, None), 
            ("asset", "asset", ContractTermAsset, True, None, False, None), 
            ("action", "action", ContractTermAction, True, None, False, None), 
            ("group", "group", ContractTerm, True, None, False, None), 
        ])
        return js




class ContractTermAction(backboneelement.BackboneElement):
    """ Entity being ascribed responsibility.
    
    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.doNotPerform = None
        """ True if the term prohibits the  action.
        Type `bool`. """
        
        self.type = None
        """ Type or form of the action.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Entity of the action.
        List of `ContractTermActionSubject` items (represented as `dict` in JSON). """
        
        self.intent = None
        """ Purpose for the Contract Term Action.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.linkId = None
        """ Pointer to specific item.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.status = None
        """ State of the action.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.context = None
        """ Episode associated with action.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.contextLinkId = None
        """ Pointer to specific item.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.occurrenceDateTime = None
        """ When action happens.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ When action happens.
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming = None
        """ When action happens.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.requester = None
        """ Who asked for action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requesterLinkId = None
        """ Pointer to specific item.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.performerType = None
        """ Kind of service performer.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.performerRole = None
        """ Competency of the performer.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Actor that wil execute (or not) the action.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performerLinkId = None
        """ Pointer to specific item.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.reasonCode = None
        """ Why is action (not) needed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why is action (not) needed?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.reason = None
        """ Why action is to be performed.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.reasonLinkId = None
        """ Pointer to specific item.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.note = None
        """ Comments about the action.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.securityLabelNumber = None
        """ Action restriction numbers.
        List of `FHIRUnsignedInt` items (represented as `int` in JSON). """
        
        super(ContractTermAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAction, self).elementProperties()
        js.extend([
            ("doNotPerform", "doNotPerform", bool, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
            ("subject", "subject", ContractTermActionSubject, True, None, False, None), 
            ("intent", "intent", codeableconcept.CodeableConcept, False, None, True, None), 
            ("linkId", "linkId", fhirdatatypes.FHIRString, True, None, False, None), 
            ("status", "status", codeableconcept.CodeableConcept, False, None, True, None), 
            ("context", "context", fhirreference.FHIRReference, False, None, False, None), 
            ("contextLinkId", "contextLinkId", fhirdatatypes.FHIRString, True, None, False, None), 
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatatypes.FHIRDateTime, False, "occurrence", False, None), 
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False, None), 
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False, None), 
            ("requester", "requester", fhirreference.FHIRReference, True, None, False, None), 
            ("requesterLinkId", "requesterLinkId", fhirdatatypes.FHIRString, True, None, False, None), 
            ("performerType", "performerType", codeableconcept.CodeableConcept, True, None, False, None), 
            ("performerRole", "performerRole", codeableconcept.CodeableConcept, False, None, False, None), 
            ("performer", "performer", fhirreference.FHIRReference, False, None, False, None), 
            ("performerLinkId", "performerLinkId", fhirdatatypes.FHIRString, True, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("reason", "reason", fhirdatatypes.FHIRString, True, None, False, None), 
            ("reasonLinkId", "reasonLinkId", fhirdatatypes.FHIRString, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("securityLabelNumber", "securityLabelNumber", fhirdatatypes.FHIRUnsignedInt, True, None, False, None), 
        ])
        return js




class ContractTermActionSubject(backboneelement.BackboneElement):
    """ Entity of the action.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ Entity of the action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.role = None
        """ Role type of the agent.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTermActionSubject, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermActionSubject, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, True, None, True, None), 
            ("role", "role", codeableconcept.CodeableConcept, False, None, False, None), 
        ])
        return js




class ContractTermAsset(backboneelement.BackboneElement):
    """ Contract Term Asset List.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.scope = None
        """ Range of asset.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ Asset category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.typeReference = None
        """ Associated entities.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.subtype = None
        """ Asset sub-category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.relationship = None
        """ Kinship of the asset.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.context = None
        """ Circumstance of the asset.
        List of `ContractTermAssetContext` items (represented as `dict` in JSON). """
        
        self.condition = None
        """ Quality desctiption of asset.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.periodType = None
        """ Asset availability types.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period of the asset.
        List of `Period` items (represented as `dict` in JSON). """
        
        self.usePeriod = None
        """ Time period.
        List of `Period` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Asset clause or question text.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.linkId = None
        """ Pointer to asset text.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.answer = None
        """ Response to assets.
        List of `ContractTermOfferAnswer` items (represented as `dict` in JSON). """
        
        self.securityLabelNumber = None
        """ Asset restriction numbers.
        List of `FHIRUnsignedInt` items (represented as `int` in JSON). """
        
        self.valuedItem = None
        """ Contract Valued Item List.
        List of `ContractTermAssetValuedItem` items (represented as `dict` in JSON). """
        
        super(ContractTermAsset, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAsset, self).elementProperties()
        js.extend([
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, True, None, False, None), 
            ("typeReference", "typeReference", fhirreference.FHIRReference, True, None, False, None), 
            ("subtype", "subtype", codeableconcept.CodeableConcept, True, None, False, None), 
            ("relationship", "relationship", coding.Coding, False, None, False, None), 
            ("context", "context", ContractTermAssetContext, True, None, False, None), 
            ("condition", "condition", fhirdatatypes.FHIRString, False, None, False, None), 
            ("periodType", "periodType", codeableconcept.CodeableConcept, True, None, False, None), 
            ("period", "period", period.Period, True, None, False, None), 
            ("usePeriod", "usePeriod", period.Period, True, None, False, None), 
            ("text", "text", fhirdatatypes.FHIRString, False, None, False, None), 
            ("linkId", "linkId", fhirdatatypes.FHIRString, True, None, False, None), 
            ("answer", "answer", ContractTermOfferAnswer, True, None, False, None), 
            ("securityLabelNumber", "securityLabelNumber", fhirdatatypes.FHIRUnsignedInt, True, None, False, None), 
            ("valuedItem", "valuedItem", ContractTermAssetValuedItem, True, None, False, None), 
        ])
        return js




class ContractTermAssetContext(backboneelement.BackboneElement):
    """ Circumstance of the asset.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ Creator,custodian or owner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.code = None
        """ Codeable asset context.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Context description.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(ContractTermAssetContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAssetContext, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, False, None, False, None), 
            ("code", "code", codeableconcept.CodeableConcept, True, None, False, None), 
            ("text", "text", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js




class ContractTermAssetValuedItem(backboneelement.BackboneElement):
    """ Contract Valued Item List.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.entityCodeableConcept = None
        """ Contract Valued Item Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.entityReference = None
        """ Contract Valued Item Type.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Contract Valued Item Number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.effectiveTime = None
        """ Contract Valued Item Effective Tiem.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.quantity = None
        """ Count of Contract Valued Items.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Contract Valued Item fee, charge, or cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Contract Valued Item Price Scaling Factor.
        Type `float`. """
        
        self.points = None
        """ Contract Valued Item Difficulty Scaling Factor.
        Type `float`. """
        
        self.net = None
        """ Total Contract Valued Item Value.
        Type `Money` (represented as `dict` in JSON). """
        
        self.payment = None
        """ Terms of valuation.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.paymentDate = None
        """ When payment is due.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.responsible = None
        """ Who will make payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.recipient = None
        """ Who will receive payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.linkId = None
        """ Pointer to specific item.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.securityLabelNumber = None
        """ Security Labels that define affected terms.
        List of `FHIRUnsignedInt` items (represented as `int` in JSON). """
        
        super(ContractTermAssetValuedItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAssetValuedItem, self).elementProperties()
        js.extend([
            ("entityCodeableConcept", "entityCodeableConcept", codeableconcept.CodeableConcept, False, "entity", False, None), 
            ("entityReference", "entityReference", fhirreference.FHIRReference, False, "entity", False, None), 
            ("identifier", "identifier", identifier.Identifier, False, None, False, None), 
            ("effectiveTime", "effectiveTime", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("quantity", "quantity", quantity.Quantity, False, None, False, None), 
            ("unitPrice", "unitPrice", money.Money, False, None, False, None), 
            ("factor", "factor", float, False, None, False, None), 
            ("points", "points", float, False, None, False, None), 
            ("net", "net", money.Money, False, None, False, None), 
            ("payment", "payment", fhirdatatypes.FHIRString, False, None, False, None), 
            ("paymentDate", "paymentDate", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False, None), 
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, False, None), 
            ("linkId", "linkId", fhirdatatypes.FHIRString, True, None, False, None), 
            ("securityLabelNumber", "securityLabelNumber", fhirdatatypes.FHIRUnsignedInt, True, None, False, None), 
        ])
        return js




class ContractTermOffer(backboneelement.BackboneElement):
    """ Context of the Contract term.
    
    The matter of concern in the context of this provision of the agrement.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Offer business ID.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.party = None
        """ Offer Recipient.
        List of `ContractTermOfferParty` items (represented as `dict` in JSON). """
        
        self.topic = None
        """ Negotiable offer asset.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ Contract Offer Type or Form.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.decision = None
        """ Accepting party choice.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.decisionMode = None
        """ How decision is conveyed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.answer = None
        """ Response to offer text.
        List of `ContractTermOfferAnswer` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Human readable offer text.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.linkId = None
        """ Pointer to text.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.securityLabelNumber = None
        """ Offer restriction numbers.
        List of `FHIRUnsignedInt` items (represented as `int` in JSON). """
        
        super(ContractTermOffer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermOffer, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("party", "party", ContractTermOfferParty, True, None, False, None), 
            ("topic", "topic", fhirreference.FHIRReference, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("decision", "decision", codeableconcept.CodeableConcept, False, None, False, None), 
            ("decisionMode", "decisionMode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("answer", "answer", ContractTermOfferAnswer, True, None, False, None), 
            ("text", "text", fhirdatatypes.FHIRString, False, None, False, None), 
            ("linkId", "linkId", fhirdatatypes.FHIRString, True, None, False, None), 
            ("securityLabelNumber", "securityLabelNumber", fhirdatatypes.FHIRUnsignedInt, True, None, False, None), 
        ])
        return js




class ContractTermOfferAnswer(backboneelement.BackboneElement):
    """ Response to offer text.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.valueBoolean = None
        """ The actual answer response.
        Type `bool`. """
        
        self.valueDecimal = None
        """ The actual answer response.
        Type `float`. """
        
        self.valueInteger = None
        """ The actual answer response.
        Type `int`. """
        
        self.valueDate = None
        """ The actual answer response.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ The actual answer response.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valueTime = None
        """ The actual answer response.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.valueString = None
        """ The actual answer response.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueUri = None
        """ The actual answer response.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.valueAttachment = None
        """ The actual answer response.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ The actual answer response.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ The actual answer response.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ The actual answer response.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractTermOfferAnswer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermOfferAnswer, self).elementProperties()
        js.extend([
            ("valueBoolean", "valueBoolean", bool, False, "value", True, None), 
            ("valueDecimal", "valueDecimal", float, False, "value", True, None), 
            ("valueInteger", "valueInteger", int, False, "value", True, None), 
            ("valueDate", "valueDate", fhirdatatypes.FHIRDate, False, "value", True, None), 
            ("valueDateTime", "valueDateTime", fhirdatatypes.FHIRDateTime, False, "value", True, None), 
            ("valueTime", "valueTime", fhirdatatypes.FHIRTime, False, "value", True, None), 
            ("valueString", "valueString", fhirdatatypes.FHIRString, False, "value", True, None), 
            ("valueUri", "valueUri", fhirdatatypes.FHIRUri, False, "value", True, None), 
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True, None), 
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True, None), 
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True, None), 
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True, None), 
        ])
        return js




class ContractTermOfferParty(backboneelement.BackboneElement):
    """ Offer Recipient.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ Referenced entity.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.role = None
        """ Participant engagement type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTermOfferParty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermOfferParty, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, True, None, True, None), 
            ("role", "role", codeableconcept.CodeableConcept, False, None, True, None), 
        ])
        return js




class ContractTermSecurityLabel(backboneelement.BackboneElement):
    """ Protection for the Term.
    
    Security labels that protect the handling of information about the term and
    its elements, which may be specifically identified..
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.number = None
        """ Link to Security Labels.
        List of `FHIRUnsignedInt` items (represented as `int` in JSON). """
        
        self.classification = None
        """ Confidentiality Protection.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.category = None
        """ Applicable Policy.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.control = None
        """ Handling Instructions.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(ContractTermSecurityLabel, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermSecurityLabel, self).elementProperties()
        js.extend([
            ("number", "number", fhirdatatypes.FHIRUnsignedInt, True, None, False, None), 
            ("classification", "classification", coding.Coding, False, None, True, None), 
            ("category", "category", coding.Coding, True, None, False, None), 
            ("control", "control", coding.Coding, True, None, False, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import attachment

from fhirclient.models import codeableconcept

from fhirclient.models import coding

from fhirclient.codesystems import contractresourcepublicationstatuscodes

from fhirclient.codesystems import contractresourcestatuscodes

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import money

from fhirclient.models import period

from fhirclient.models import quantity

from fhirclient.models import signature

from fhirclient.models import timing

