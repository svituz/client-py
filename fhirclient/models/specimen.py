#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Specimen)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Specimen(domainresource.DomainResource):
    """ Sample for analysis.
    
    A sample to be used for analysis.
    """
    
    resource_type = "Specimen"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.accessionIdentifier = None
        """ Identifier assigned by the lab.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.status = None
        """ available | unavailable | unsatisfactory | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.type = None
        """ Kind of material that forms the specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Where the specimen came from. This may be from patient(s), from a
        location (e.g., the source of an environmental sample), or a
        sampling of a substance or a device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.receivedTime = None
        """ The time when specimen was received for processing.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.parent = None
        """ Specimen from which this specimen originated.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.request = None
        """ Why the specimen was collected.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.collection = None
        """ Collection details.
        Type `SpecimenCollection` (represented as `dict` in JSON). """
        
        self.processing = None
        """ Processing and processing step details.
        List of `SpecimenProcessing` items (represented as `dict` in JSON). """
        
        self.container = None
        """ Direct container of specimen (tube/slide, etc.).
        List of `SpecimenContainer` items (represented as `dict` in JSON). """
        
        self.condition = None
        """ State of the specimen.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        super(Specimen, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Specimen, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("accessionIdentifier", "accessionIdentifier", identifier.Identifier, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, False, specimenstatus.SpecimenStatus), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, False, None), 
            ("receivedTime", "receivedTime", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("parent", "parent", fhirreference.FHIRReference, True, None, False, None), 
            ("request", "request", fhirreference.FHIRReference, True, None, False, None), 
            ("collection", "collection", SpecimenCollection, False, None, False, None), 
            ("processing", "processing", SpecimenProcessing, True, None, False, None), 
            ("container", "container", SpecimenContainer, True, None, False, None), 
            ("condition", "condition", codeableconcept.CodeableConcept, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class SpecimenCollection(backboneelement.BackboneElement):
    """ Collection details.
    
    Details concerning the specimen collection.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.collector = None
        """ Who collected the specimen.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.collectedDateTime = None
        """ Collection time.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.collectedPeriod = None
        """ Collection time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.duration = None
        """ How long it took to collect specimen.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ The quantity of specimen collected.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.method = None
        """ Technique used to perform collection.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Anatomical collection site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.fastingStatusCodeableConcept = None
        """ Whether or how long patient abstained from food and/or drink.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.fastingStatusDuration = None
        """ Whether or how long patient abstained from food and/or drink.
        Type `Duration` (represented as `dict` in JSON). """
        
        super(SpecimenCollection, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenCollection, self).elementProperties()
        js.extend([
            ("collector", "collector", fhirreference.FHIRReference, False, None, False, None), 
            ("collectedDateTime", "collectedDateTime", fhirdatatypes.FHIRDateTime, False, "collected", False, None), 
            ("collectedPeriod", "collectedPeriod", period.Period, False, "collected", False, None), 
            ("duration", "duration", duration.Duration, False, None, False, None), 
            ("quantity", "quantity", quantity.Quantity, False, None, False, None), 
            ("method", "method", codeableconcept.CodeableConcept, False, None, False, None), 
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False, None), 
            ("fastingStatusCodeableConcept", "fastingStatusCodeableConcept", codeableconcept.CodeableConcept, False, "fastingStatus", False, None), 
            ("fastingStatusDuration", "fastingStatusDuration", duration.Duration, False, "fastingStatus", False, None), 
        ])
        return js




class SpecimenContainer(backboneelement.BackboneElement):
    """ Direct container of specimen (tube/slide, etc.).
    
    The container holding the specimen.  The recursive nature of containers;
    i.e. blood in tube in tray in rack is not addressed here.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Id for the container.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Textual description of the container.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.type = None
        """ Kind of container directly associated with specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.capacity = None
        """ Container volume or size.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.specimenQuantity = None
        """ Quantity of specimen within container.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.additiveCodeableConcept = None
        """ Additive associated with container.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.additiveReference = None
        """ Additive associated with container.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(SpecimenContainer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenContainer, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("capacity", "capacity", quantity.Quantity, False, None, False, None), 
            ("specimenQuantity", "specimenQuantity", quantity.Quantity, False, None, False, None), 
            ("additiveCodeableConcept", "additiveCodeableConcept", codeableconcept.CodeableConcept, False, "additive", False, None), 
            ("additiveReference", "additiveReference", fhirreference.FHIRReference, False, "additive", False, None), 
        ])
        return js




class SpecimenProcessing(backboneelement.BackboneElement):
    """ Processing and processing step details.
    
    Details concerning processing and processing steps for the specimen.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Textual description of procedure.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.procedure = None
        """ Indicates the treatment step  applied to the specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.additive = None
        """ Material used in the processing step.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.timeDateTime = None
        """ Date and time of specimen processing.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.timePeriod = None
        """ Date and time of specimen processing.
        Type `Period` (represented as `dict` in JSON). """
        
        super(SpecimenProcessing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenProcessing, self).elementProperties()
        js.extend([
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("procedure", "procedure", codeableconcept.CodeableConcept, False, None, False, None), 
            ("additive", "additive", fhirreference.FHIRReference, True, None, False, None), 
            ("timeDateTime", "timeDateTime", fhirdatatypes.FHIRDateTime, False, "time", False, None), 
            ("timePeriod", "timePeriod", period.Period, False, "time", False, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import duration

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.models import quantity

from fhirclient.codesystems import specimenstatus

