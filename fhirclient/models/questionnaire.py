#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Questionnaire)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Questionnaire(domainresource.DomainResource):
    """ A structured set of questions.
    
    A structured set of questions intended to guide the collection of answers
    from end-users. Questionnaires provide detailed control over order,
    presentation, phraseology and grouping to allow coherent, consistent data
    collection.
    """
    
    resource_type = "Questionnaire"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this questionnaire, represented as a URI
        (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the questionnaire.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the questionnaire.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this questionnaire (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this questionnaire (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.derivedFrom = None
        """ Instantiates protocol or definition.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.subjectType = None
        """ Resource that can be subject of QuestionnaireResponse.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Natural language description of the questionnaire.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for questionnaire (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.purpose = None
        """ Why this questionnaire is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.approvalDate = None
        """ When the questionnaire was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.lastReviewDate = None
        """ When the questionnaire was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ When the questionnaire is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.code = None
        """ Concept that represents the overall questionnaire.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.item = None
        """ Questions and sections within the Questionnaire.
        List of `QuestionnaireItem` items (represented as `dict` in JSON). """
        
        super(Questionnaire, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Questionnaire, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("derivedFrom", "derivedFrom", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, publicationstatus.PublicationStatus), 
            ("experimental", "experimental", bool, False, None, False, None), 
            ("subjectType", "subjectType", fhirdatatypes.FHIRCode, True, None, False, resourcetype.ResourceType), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False, None), 
            ("contact", "contact", contactdetail.ContactDetail, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False, None), 
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False, None), 
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("copyright", "copyright", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("approvalDate", "approvalDate", fhirdatatypes.FHIRDate, False, None, False, None), 
            ("lastReviewDate", "lastReviewDate", fhirdatatypes.FHIRDate, False, None, False, None), 
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False, None), 
            ("code", "code", coding.Coding, True, None, False, None), 
            ("item", "item", QuestionnaireItem, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class QuestionnaireItem(backboneelement.BackboneElement):
    """ Questions and sections within the Questionnaire.
    
    A particular question, question grouping or display text that is part of
    the questionnaire.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.linkId = None
        """ Unique id for item in questionnaire.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.definition = None
        """ ElementDefinition - details for the item.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.code = None
        """ Corresponding concept for this item in a terminology.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.prefix = None
        """ E.g. "1(a)", "2.5.3".
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.text = None
        """ Primary text for the item.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.type = None
        """ group | display | boolean | decimal | integer | date | dateTime +.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.enableWhen = None
        """ Only allow data when.
        List of `QuestionnaireItemEnableWhen` items (represented as `dict` in JSON). """
        
        self.enableBehavior = None
        """ all | any.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.required = None
        """ Whether the item must be included in data results.
        Type `bool`. """
        
        self.repeats = None
        """ Whether the item may repeat.
        Type `bool`. """
        
        self.readOnly = None
        """ Don't allow human editing.
        Type `bool`. """
        
        self.maxLength = None
        """ No more than this many characters.
        Type `int`. """
        
        self.answerValueSet = None
        """ Valueset containing permitted answers.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.answerOption = None
        """ Permitted answer.
        List of `QuestionnaireItemAnswerOption` items (represented as `dict` in JSON). """
        
        self.initial = None
        """ Initial value(s) when item is first rendered.
        List of `QuestionnaireItemInitial` items (represented as `dict` in JSON). """
        
        self.item = None
        """ Nested questionnaire items.
        List of `QuestionnaireItem` items (represented as `dict` in JSON). """
        
        super(QuestionnaireItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireItem, self).elementProperties()
        js.extend([
            ("linkId", "linkId", fhirdatatypes.FHIRString, False, None, True, None), 
            ("definition", "definition", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("code", "code", coding.Coding, True, None, False, None), 
            ("prefix", "prefix", fhirdatatypes.FHIRString, False, None, False, None), 
            ("text", "text", fhirdatatypes.FHIRString, False, None, False, None), 
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, questionnaireitemtype.QuestionnaireItemType), 
            ("enableWhen", "enableWhen", QuestionnaireItemEnableWhen, True, None, False, None), 
            ("enableBehavior", "enableBehavior", fhirdatatypes.FHIRCode, False, None, False, enablewhenbehavior.EnableWhenBehavior), 
            ("required", "required", bool, False, None, False, None), 
            ("repeats", "repeats", bool, False, None, False, None), 
            ("readOnly", "readOnly", bool, False, None, False, None), 
            ("maxLength", "maxLength", int, False, None, False, None), 
            ("answerValueSet", "answerValueSet", fhirdatatypes.FHIRCanonical, False, None, False, None), 
            ("answerOption", "answerOption", QuestionnaireItemAnswerOption, True, None, False, None), 
            ("initial", "initial", QuestionnaireItemInitial, True, None, False, None), 
            ("item", "item", QuestionnaireItem, True, None, False, None), 
        ])
        return js




class QuestionnaireItemAnswerOption(backboneelement.BackboneElement):
    """ Permitted answer.
    
    One of the permitted answers for a "choice" or "open-choice" question.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.valueInteger = None
        """ Answer value.
        Type `int`. """
        
        self.valueDate = None
        """ Answer value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueTime = None
        """ Answer value.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.valueString = None
        """ Answer value.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueCoding = None
        """ Answer value.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Answer value.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.initialSelected = None
        """ Whether option is selected by default.
        Type `bool`. """
        
        super(QuestionnaireItemAnswerOption, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireItemAnswerOption, self).elementProperties()
        js.extend([
            ("valueInteger", "valueInteger", int, False, "value", True, None), 
            ("valueDate", "valueDate", fhirdatatypes.FHIRDate, False, "value", True, None), 
            ("valueTime", "valueTime", fhirdatatypes.FHIRTime, False, "value", True, None), 
            ("valueString", "valueString", fhirdatatypes.FHIRString, False, "value", True, None), 
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True, None), 
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True, None), 
            ("initialSelected", "initialSelected", bool, False, None, False, None), 
        ])
        return js




class QuestionnaireItemEnableWhen(backboneelement.BackboneElement):
    """ Only allow data when.
    
    A constraint indicating that this item should only be enabled
    (displayed/allow answers to be captured) when the specified condition is
    true.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.question = None
        """ Question that determines whether item is enabled.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.operator = None
        """ exists | = | != | > | < | >= | <=.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.answerBoolean = None
        """ Value for question comparison based on operator.
        Type `bool`. """
        
        self.answerDecimal = None
        """ Value for question comparison based on operator.
        Type `float`. """
        
        self.answerInteger = None
        """ Value for question comparison based on operator.
        Type `int`. """
        
        self.answerDate = None
        """ Value for question comparison based on operator.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.answerDateTime = None
        """ Value for question comparison based on operator.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.answerTime = None
        """ Value for question comparison based on operator.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.answerString = None
        """ Value for question comparison based on operator.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.answerCoding = None
        """ Value for question comparison based on operator.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.answerQuantity = None
        """ Value for question comparison based on operator.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.answerReference = None
        """ Value for question comparison based on operator.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(QuestionnaireItemEnableWhen, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireItemEnableWhen, self).elementProperties()
        js.extend([
            ("question", "question", fhirdatatypes.FHIRString, False, None, True, None), 
            ("operator", "operator", fhirdatatypes.FHIRCode, False, None, True, questionnaireitemoperator.QuestionnaireItemOperator), 
            ("answerBoolean", "answerBoolean", bool, False, "answer", True, None), 
            ("answerDecimal", "answerDecimal", float, False, "answer", True, None), 
            ("answerInteger", "answerInteger", int, False, "answer", True, None), 
            ("answerDate", "answerDate", fhirdatatypes.FHIRDate, False, "answer", True, None), 
            ("answerDateTime", "answerDateTime", fhirdatatypes.FHIRDateTime, False, "answer", True, None), 
            ("answerTime", "answerTime", fhirdatatypes.FHIRTime, False, "answer", True, None), 
            ("answerString", "answerString", fhirdatatypes.FHIRString, False, "answer", True, None), 
            ("answerCoding", "answerCoding", coding.Coding, False, "answer", True, None), 
            ("answerQuantity", "answerQuantity", quantity.Quantity, False, "answer", True, None), 
            ("answerReference", "answerReference", fhirreference.FHIRReference, False, "answer", True, None), 
        ])
        return js




class QuestionnaireItemInitial(backboneelement.BackboneElement):
    """ Initial value(s) when item is first rendered.
    
    One or more values that should be pre-populated in the answer when
    initially rendering the questionnaire for user input.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.valueBoolean = None
        """ Actual value for initializing the question.
        Type `bool`. """
        
        self.valueDecimal = None
        """ Actual value for initializing the question.
        Type `float`. """
        
        self.valueInteger = None
        """ Actual value for initializing the question.
        Type `int`. """
        
        self.valueDate = None
        """ Actual value for initializing the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ Actual value for initializing the question.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valueTime = None
        """ Actual value for initializing the question.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.valueString = None
        """ Actual value for initializing the question.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueUri = None
        """ Actual value for initializing the question.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.valueAttachment = None
        """ Actual value for initializing the question.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ Actual value for initializing the question.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Actual value for initializing the question.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Actual value for initializing the question.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(QuestionnaireItemInitial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireItemInitial, self).elementProperties()
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



from fhirclient.models import attachment

from fhirclient.models import codeableconcept

from fhirclient.models import coding

from fhirclient.models import contactdetail

from fhirclient.codesystems import enablewhenbehavior

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.codesystems import publicationstatus

from fhirclient.models import quantity

from fhirclient.codesystems import questionnaireitemoperator

from fhirclient.codesystems import questionnaireitemtype

from fhirclient.codesystems import resourcetype

from fhirclient.models import usagecontext

