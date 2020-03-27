#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/VisionPrescription)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class VisionPrescription(domainresource.DomainResource):
    """ Prescription for vision correction products for a patient.
    
    An authorization for the provision of glasses and/or contact lenses to a
    patient.
    """
    
    resource_type = "VisionPrescription"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier for vision prescription.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.created = None
        """ Response creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.patient = None
        """ Who prescription is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Created during encounter / admission / stay.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.dateWritten = None
        """ When prescription was authorized.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.prescriber = None
        """ Who authorized the vision prescription.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.lensSpecification = None
        """ Vision lens authorization.
        List of `VisionPrescriptionLensSpecification` items (represented as `dict` in JSON). """
        
        super(VisionPrescription, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VisionPrescription, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, financialresourcestatuscodes.FinancialResourceStatusCodes), 
            ("created", "created", fhirdatatypes.FHIRDateTime, False, None, True, None), 
            ("patient", "patient", fhirreference.FHIRReference, False, None, True, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("dateWritten", "dateWritten", fhirdatatypes.FHIRDateTime, False, None, True, None), 
            ("prescriber", "prescriber", fhirreference.FHIRReference, False, None, True, None), 
            ("lensSpecification", "lensSpecification", VisionPrescriptionLensSpecification, True, None, True, None), 
        ])
        return js



from fhirclient.models import backboneelement

class VisionPrescriptionLensSpecification(backboneelement.BackboneElement):
    """ Vision lens authorization.
    
    Contain the details of  the individual lens specifications and serves as
    the authorization for the fullfillment by certified professionals.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.product = None
        """ Product to be supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.eye = None
        """ right | left.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.sphere = None
        """ Power of the lens.
        Type `float`. """
        
        self.cylinder = None
        """ Lens power for astigmatism.
        Type `float`. """
        
        self.axis = None
        """ Lens meridian which contain no power for astigmatism.
        Type `int`. """
        
        self.prism = None
        """ Eye alignment compensation.
        List of `VisionPrescriptionLensSpecificationPrism` items (represented as `dict` in JSON). """
        
        self.add = None
        """ Added power for multifocal levels.
        Type `float`. """
        
        self.power = None
        """ Contact lens power.
        Type `float`. """
        
        self.backCurve = None
        """ Contact lens back curvature.
        Type `float`. """
        
        self.diameter = None
        """ Contact lens diameter.
        Type `float`. """
        
        self.duration = None
        """ Lens wear duration.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.color = None
        """ Color required.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.brand = None
        """ Brand required.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.note = None
        """ Notes for coatings.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        super(VisionPrescriptionLensSpecification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VisionPrescriptionLensSpecification, self).elementProperties()
        js.extend([
            ("product", "product", codeableconcept.CodeableConcept, False, None, True, None), 
            ("eye", "eye", fhirdatatypes.FHIRCode, False, None, True, visioneyes.VisionEyes), 
            ("sphere", "sphere", float, False, None, False, None), 
            ("cylinder", "cylinder", float, False, None, False, None), 
            ("axis", "axis", int, False, None, False, None), 
            ("prism", "prism", VisionPrescriptionLensSpecificationPrism, True, None, False, None), 
            ("add", "add", float, False, None, False, None), 
            ("power", "power", float, False, None, False, None), 
            ("backCurve", "backCurve", float, False, None, False, None), 
            ("diameter", "diameter", float, False, None, False, None), 
            ("duration", "duration", quantity.Quantity, False, None, False, None), 
            ("color", "color", fhirdatatypes.FHIRString, False, None, False, None), 
            ("brand", "brand", fhirdatatypes.FHIRString, False, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
        ])
        return js




class VisionPrescriptionLensSpecificationPrism(backboneelement.BackboneElement):
    """ Eye alignment compensation.
    
    Allows for adjustment on two axis.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Amount of adjustment.
        Type `float`. """
        
        self.base = None
        """ up | down | in | out.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(VisionPrescriptionLensSpecificationPrism, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VisionPrescriptionLensSpecificationPrism, self).elementProperties()
        js.extend([
            ("amount", "amount", float, False, None, True, None), 
            ("base", "base", fhirdatatypes.FHIRCode, False, None, True, visionbase.VisionBase), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.codesystems import financialresourcestatuscodes

from fhirclient.models import identifier

from fhirclient.models import quantity

from fhirclient.codesystems import visionbase

from fhirclient.codesystems import visioneyes

