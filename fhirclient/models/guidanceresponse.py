#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/GuidanceResponse)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class GuidanceResponse(domainresource.DomainResource):
    """ The formal response to a guidance request.
    
    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the
    description of any proposed actions to be taken.
    """
    
    resource_type = "GuidanceResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.requestIdentifier = None
        """ The identifier of the request associated with this response, if any.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.moduleUri = None
        """ What guidance was requested.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.moduleCanonical = None
        """ What guidance was requested.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.moduleCodeableConcept = None
        """ What guidance was requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ success | data-requested | data-required | in-progress | failure |
        entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.subject = None
        """ Patient the request was performed for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter during which the response was returned.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ When the guidance response was processed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.performer = None
        """ Device returning the guidance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why guidance is needed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why guidance is needed.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Additional notes about the response.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.evaluationMessage = None
        """ Messages resulting from the evaluation of the artifact or artifacts.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.outputParameters = None
        """ The output parameters of the evaluation, if any.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.result = None
        """ Proposed actions, if any.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.dataRequirement = None
        """ Additional required data.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        super(GuidanceResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GuidanceResponse, self).elementProperties()
        js.extend([
            ("requestIdentifier", "requestIdentifier", identifier.Identifier, False, None, False, None), 
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("moduleUri", "moduleUri", fhirdatatypes.FHIRUri, False, "module", True, None), 
            ("moduleCanonical", "moduleCanonical", fhirdatatypes.FHIRCanonical, False, "module", True, None), 
            ("moduleCodeableConcept", "moduleCodeableConcept", codeableconcept.CodeableConcept, False, "module", True, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, guidanceresponsestatus.GuidanceResponseStatus), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, False, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("performer", "performer", fhirreference.FHIRReference, False, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("evaluationMessage", "evaluationMessage", fhirreference.FHIRReference, True, None, False, None), 
            ("outputParameters", "outputParameters", fhirreference.FHIRReference, False, None, False, None), 
            ("result", "result", fhirreference.FHIRReference, False, None, False, None), 
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import datarequirement

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.codesystems import guidanceresponsestatus

from fhirclient.models import identifier

