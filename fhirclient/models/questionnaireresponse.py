#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class QuestionnaireResponse(domainresource.DomainResource):
    """ A structured set of questions and their answers.
    
    A structured set of questions and their answers. The questions are ordered
    and grouped into coherent subsets, corresponding to the structure of the
    grouping of the questionnaire being responded to.
    """
    
    resource_type = "QuestionnaireResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Unique id for this set of answers.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.basedOn = None
        """ Request fulfilled by this QuestionnaireResponse.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Part of this action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.questionnaire = None
        """ Form being answered.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.status = None
        """ in-progress | completed | amended | entered-in-error | stopped.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.subject = None
        """ The subject of the questions.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.authored = None
        """ Date the answers were gathered.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.author = None
        """ Person who received and recorded the answers.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.source = None
        """ The person who answered the questions.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.item = None
        """ Groups and questions.
        List of `QuestionnaireResponseItem` items (represented as `dict` in JSON). """
        
        super(QuestionnaireResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireResponse, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False, None), 
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False, None), 
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False, None), 
            ("questionnaire", "questionnaire", fhirdatatypes.FHIRCanonical, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, questionnaireresponsestatus.QuestionnaireResponseStatus), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, False, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("authored", "authored", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("author", "author", fhirreference.FHIRReference, False, None, False, None), 
            ("source", "source", fhirreference.FHIRReference, False, None, False, None), 
            ("item", "item", QuestionnaireResponseItem, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class QuestionnaireResponseItem(backboneelement.BackboneElement):
    """ Groups and questions.
    
    A group or question item from the original questionnaire for which answers
    are provided.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.linkId = None
        """ Pointer to specific item from Questionnaire.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.definition = None
        """ ElementDefinition - details for the item.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.text = None
        """ Name for group or question text.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.answer = None
        """ The response(s) to the question.
        List of `QuestionnaireResponseItemAnswer` items (represented as `dict` in JSON). """
        
        self.item = None
        """ Nested questionnaire response items.
        List of `QuestionnaireResponseItem` items (represented as `dict` in JSON). """
        
        super(QuestionnaireResponseItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireResponseItem, self).elementProperties()
        js.extend([
            ("linkId", "linkId", fhirdatatypes.FHIRString, False, None, True, None), 
            ("definition", "definition", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("text", "text", fhirdatatypes.FHIRString, False, None, False, None), 
            ("answer", "answer", QuestionnaireResponseItemAnswer, True, None, False, None), 
            ("item", "item", QuestionnaireResponseItem, True, None, False, None), 
        ])
        return js




class QuestionnaireResponseItemAnswer(backboneelement.BackboneElement):
    """ The response(s) to the question.
    
    The respondent's answer(s) to the question.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.valueBoolean = None
        """ Single-valued answer to the question.
        Type `bool`. """
        
        self.valueDecimal = None
        """ Single-valued answer to the question.
        Type `float`. """
        
        self.valueInteger = None
        """ Single-valued answer to the question.
        Type `int`. """
        
        self.valueDate = None
        """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ Single-valued answer to the question.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valueTime = None
        """ Single-valued answer to the question.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.valueString = None
        """ Single-valued answer to the question.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueUri = None
        """ Single-valued answer to the question.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.valueAttachment = None
        """ Single-valued answer to the question.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ Single-valued answer to the question.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Single-valued answer to the question.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Single-valued answer to the question.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.item = None
        """ Nested groups and questions.
        List of `QuestionnaireResponseItem` items (represented as `dict` in JSON). """
        
        super(QuestionnaireResponseItemAnswer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireResponseItemAnswer, self).elementProperties()
        js.extend([
            ("valueBoolean", "valueBoolean", bool, False, "value", False, None), 
            ("valueDecimal", "valueDecimal", float, False, "value", False, None), 
            ("valueInteger", "valueInteger", int, False, "value", False, None), 
            ("valueDate", "valueDate", fhirdatatypes.FHIRDate, False, "value", False, None), 
            ("valueDateTime", "valueDateTime", fhirdatatypes.FHIRDateTime, False, "value", False, None), 
            ("valueTime", "valueTime", fhirdatatypes.FHIRTime, False, "value", False, None), 
            ("valueString", "valueString", fhirdatatypes.FHIRString, False, "value", False, None), 
            ("valueUri", "valueUri", fhirdatatypes.FHIRUri, False, "value", False, None), 
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False, None), 
            ("valueCoding", "valueCoding", coding.Coding, False, "value", False, None), 
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False, None), 
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False, None), 
            ("item", "item", QuestionnaireResponseItem, True, None, False, None), 
        ])
        return js



from fhirclient.models import attachment

from fhirclient.models import coding

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import quantity

from fhirclient.codesystems import questionnaireresponsestatus

