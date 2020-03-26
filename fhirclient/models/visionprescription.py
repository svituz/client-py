#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/VisionPrescription) on 2020-03-26.
#  2020, SMART Health IT.


from . import domainresource

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
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True),
            ("created", "created", fhirdatatypes.FHIRDateTime, False, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("dateWritten", "dateWritten", fhirdatatypes.FHIRDateTime, False, None, True),
            ("prescriber", "prescriber", fhirreference.FHIRReference, False, None, True),
            ("lensSpecification", "lensSpecification", VisionPrescriptionLensSpecification, True, None, True),
        ])
        return js



from . import backboneelement

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
            ("product", "product", codeableconcept.CodeableConcept, False, None, True),
            ("eye", "eye", fhirdatatypes.FHIRCode, False, None, True),
            ("sphere", "sphere", float, False, None, False),
            ("cylinder", "cylinder", float, False, None, False),
            ("axis", "axis", int, False, None, False),
            ("prism", "prism", VisionPrescriptionLensSpecificationPrism, True, None, False),
            ("add", "add", float, False, None, False),
            ("power", "power", float, False, None, False),
            ("backCurve", "backCurve", float, False, None, False),
            ("diameter", "diameter", float, False, None, False),
            ("duration", "duration", quantity.Quantity, False, None, False),
            ("color", "color", fhirdatatypes.FHIRString, False, None, False),
            ("brand", "brand", fhirdatatypes.FHIRString, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
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
            ("amount", "amount", float, False, None, True),
            ("base", "base", fhirdatatypes.FHIRCode, False, None, True),
        ])
        return js



import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']

try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']

try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']

try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']

try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']

