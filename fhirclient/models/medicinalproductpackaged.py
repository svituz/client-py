#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductPackaged)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class MedicinalProductPackaged(domainresource.DomainResource):
    """ A medicinal product in a container or package.
    """
    
    resource_type = "MedicinalProductPackaged"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ The product with this is a pack for.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Textual description.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.legalStatusOfSupply = None
        """ The legal status of supply of the medicinal product as classified
        by the regulator.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.marketingStatus = None
        """ Marketing information.
        List of `MarketingStatus` items (represented as `dict` in JSON). """
        
        self.marketingAuthorization = None
        """ Manufacturer of this Package Item.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.manufacturer = None
        """ Manufacturer of this Package Item.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.batchIdentifier = None
        """ Batch numbering.
        List of `MedicinalProductPackagedBatchIdentifier` items (represented as `dict` in JSON). """
        
        self.packageItem = None
        """ A packaging item, as a contained for medicine, possibly with other
        packaging items within.
        List of `MedicinalProductPackagedPackageItem` items (represented as `dict` in JSON). """
        
        super(MedicinalProductPackaged, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPackaged, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("legalStatusOfSupply", "legalStatusOfSupply", codeableconcept.CodeableConcept, False, None, False, None), 
            ("marketingStatus", "marketingStatus", marketingstatus.MarketingStatus, True, None, False, None), 
            ("marketingAuthorization", "marketingAuthorization", fhirreference.FHIRReference, False, None, False, None), 
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False, None), 
            ("batchIdentifier", "batchIdentifier", MedicinalProductPackagedBatchIdentifier, True, None, False, None), 
            ("packageItem", "packageItem", MedicinalProductPackagedPackageItem, True, None, True, None), 
        ])
        return js



from fhirclient.models import backboneelement

class MedicinalProductPackagedBatchIdentifier(backboneelement.BackboneElement):
    """ Batch numbering.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.outerPackaging = None
        """ A number appearing on the outer packaging of a specific batch.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.immediatePackaging = None
        """ A number appearing on the immediate packaging (and not the outer
        packaging).
        Type `Identifier` (represented as `dict` in JSON). """
        
        super(MedicinalProductPackagedBatchIdentifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPackagedBatchIdentifier, self).elementProperties()
        js.extend([
            ("outerPackaging", "outerPackaging", identifier.Identifier, False, None, True, None), 
            ("immediatePackaging", "immediatePackaging", identifier.Identifier, False, None, False, None), 
        ])
        return js




class MedicinalProductPackagedPackageItem(backboneelement.BackboneElement):
    """ A packaging item, as a contained for medicine, possibly with other
    packaging items within.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Including possibly Data Carrier Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.type = None
        """ The physical type of the container of the medicine.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ The quantity of this package in the medicinal product, at the
        current level of packaging. The outermost is always 1.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.material = None
        """ Material type of the package item.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.alternateMaterial = None
        """ A possible alternate material for the packaging.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.device = None
        """ A device accompanying a medicinal product.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.manufacturedItem = None
        """ The manufactured item as contained in the packaged medicinal
        product.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.packageItem = None
        """ Allows containers within containers.
        List of `MedicinalProductPackagedPackageItem` items (represented as `dict` in JSON). """
        
        self.physicalCharacteristics = None
        """ Dimensions, color etc..
        Type `ProdCharacteristic` (represented as `dict` in JSON). """
        
        self.otherCharacteristics = None
        """ Other codeable characteristics.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.shelfLifeStorage = None
        """ Shelf Life and storage information.
        List of `ProductShelfLife` items (represented as `dict` in JSON). """
        
        self.manufacturer = None
        """ Manufacturer of this Package Item.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(MedicinalProductPackagedPackageItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPackagedPackageItem, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
            ("quantity", "quantity", quantity.Quantity, False, None, True, None), 
            ("material", "material", codeableconcept.CodeableConcept, True, None, False, None), 
            ("alternateMaterial", "alternateMaterial", codeableconcept.CodeableConcept, True, None, False, None), 
            ("device", "device", fhirreference.FHIRReference, True, None, False, None), 
            ("manufacturedItem", "manufacturedItem", fhirreference.FHIRReference, True, None, False, None), 
            ("packageItem", "packageItem", MedicinalProductPackagedPackageItem, True, None, False, None), 
            ("physicalCharacteristics", "physicalCharacteristics", prodcharacteristic.ProdCharacteristic, False, None, False, None), 
            ("otherCharacteristics", "otherCharacteristics", codeableconcept.CodeableConcept, True, None, False, None), 
            ("shelfLifeStorage", "shelfLifeStorage", productshelflife.ProductShelfLife, True, None, False, None), 
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import marketingstatus

from fhirclient.models import prodcharacteristic

from fhirclient.models import productshelflife

from fhirclient.models import quantity

