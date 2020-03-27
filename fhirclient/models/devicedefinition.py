#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DeviceDefinition)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class DeviceDefinition(domainresource.DomainResource):
    """ An instance of a medical-related component of a medical device.
    
    The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """
    
    resource_type = "DeviceDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Instance identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.udiDeviceIdentifier = None
        """ Unique Device Identifier (UDI) Barcode string.
        List of `DeviceDefinitionUdiDeviceIdentifier` items (represented as `dict` in JSON). """
        
        self.manufacturerString = None
        """ Name of device manufacturer.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.manufacturerReference = None
        """ Name of device manufacturer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.deviceName = None
        """ A name given to the device to identify it.
        List of `DeviceDefinitionDeviceName` items (represented as `dict` in JSON). """
        
        self.modelNumber = None
        """ The model number for the device.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.type = None
        """ What kind of device or device system this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.specialization = None
        """ The capabilities supported on a  device, the standards to which the
        device conforms for a particular purpose, and used for the
        communication.
        List of `DeviceDefinitionSpecialization` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Available versions.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.safety = None
        """ Safety characteristics of the device.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.shelfLifeStorage = None
        """ Shelf Life and storage information.
        List of `ProductShelfLife` items (represented as `dict` in JSON). """
        
        self.physicalCharacteristics = None
        """ Dimensions, color etc..
        Type `ProdCharacteristic` (represented as `dict` in JSON). """
        
        self.languageCode = None
        """ Language code for the human-readable text strings produced by the
        device (all supported).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.capability = None
        """ Device capabilities.
        List of `DeviceDefinitionCapability` items (represented as `dict` in JSON). """
        
        self.property = None
        """ The actual configuration settings of a device as it actually
        operates, e.g., regulation status, time properties.
        List of `DeviceDefinitionProperty` items (represented as `dict` in JSON). """
        
        self.owner = None
        """ Organization responsible for device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.contact = None
        """ Details for human/organization for support.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.url = None
        """ Network address to contact device.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.onlineInformation = None
        """ Access to on-line information.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.note = None
        """ Device notes and comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.quantity = None
        """ The quantity of the device present in the packaging (e.g. the
        number of devices present in a pack, or the number of devices in
        the same package of the medicinal product).
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.parentDevice = None
        """ The parent device it can be part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.material = None
        """ A substance used to create the material(s) of which the device is
        made.
        List of `DeviceDefinitionMaterial` items (represented as `dict` in JSON). """
        
        super(DeviceDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinition, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("udiDeviceIdentifier", "udiDeviceIdentifier", DeviceDefinitionUdiDeviceIdentifier, True, None, False, None), 
            ("manufacturerString", "manufacturerString", fhirdatatypes.FHIRString, False, "manufacturer", False, None), 
            ("manufacturerReference", "manufacturerReference", fhirreference.FHIRReference, False, "manufacturer", False, None), 
            ("deviceName", "deviceName", DeviceDefinitionDeviceName, True, None, False, None), 
            ("modelNumber", "modelNumber", fhirdatatypes.FHIRString, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("specialization", "specialization", DeviceDefinitionSpecialization, True, None, False, None), 
            ("version", "version", fhirdatatypes.FHIRString, True, None, False, None), 
            ("safety", "safety", codeableconcept.CodeableConcept, True, None, False, None), 
            ("shelfLifeStorage", "shelfLifeStorage", productshelflife.ProductShelfLife, True, None, False, None), 
            ("physicalCharacteristics", "physicalCharacteristics", prodcharacteristic.ProdCharacteristic, False, None, False, None), 
            ("languageCode", "languageCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("capability", "capability", DeviceDefinitionCapability, True, None, False, None), 
            ("property", "property", DeviceDefinitionProperty, True, None, False, None), 
            ("owner", "owner", fhirreference.FHIRReference, False, None, False, None), 
            ("contact", "contact", contactpoint.ContactPoint, True, None, False, None), 
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("onlineInformation", "onlineInformation", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("quantity", "quantity", quantity.Quantity, False, None, False, None), 
            ("parentDevice", "parentDevice", fhirreference.FHIRReference, False, None, False, None), 
            ("material", "material", DeviceDefinitionMaterial, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class DeviceDefinitionCapability(backboneelement.BackboneElement):
    """ Device capabilities.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Type of capability.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ Description of capability.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(DeviceDefinitionCapability, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionCapability, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
            ("description", "description", codeableconcept.CodeableConcept, True, None, False, None), 
        ])
        return js




class DeviceDefinitionDeviceName(backboneelement.BackboneElement):
    """ A name given to the device to identify it.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ The name of the device.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.type = None
        """ udi-label-name | user-friendly-name | patient-reported-name |
        manufacturer-name | model-name | other.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(DeviceDefinitionDeviceName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionDeviceName, self).elementProperties()
        js.extend([
            ("name", "name", fhirdatatypes.FHIRString, False, None, True, None), 
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, devicenametype.DeviceNameType), 
        ])
        return js




class DeviceDefinitionMaterial(backboneelement.BackboneElement):
    """ A substance used to create the material(s) of which the device is made.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.substance = None
        """ The substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.alternate = None
        """ Indicates an alternative material of the device.
        Type `bool`. """
        
        self.allergenicIndicator = None
        """ Whether the substance is a known or suspected allergen.
        Type `bool`. """
        
        super(DeviceDefinitionMaterial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionMaterial, self).elementProperties()
        js.extend([
            ("substance", "substance", codeableconcept.CodeableConcept, False, None, True, None), 
            ("alternate", "alternate", bool, False, None, False, None), 
            ("allergenicIndicator", "allergenicIndicator", bool, False, None, False, None), 
        ])
        return js




class DeviceDefinitionProperty(backboneelement.BackboneElement):
    """ The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Code that specifies the property DeviceDefinitionPropetyCode
        (Extensible).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Property value as a quantity.
        List of `Quantity` items (represented as `dict` in JSON). """
        
        self.valueCode = None
        """ Property value as a code, e.g., NTP4 (synced to NTP).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(DeviceDefinitionProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
            ("valueQuantity", "valueQuantity", quantity.Quantity, True, None, False, None), 
            ("valueCode", "valueCode", codeableconcept.CodeableConcept, True, None, False, None), 
        ])
        return js




class DeviceDefinitionSpecialization(backboneelement.BackboneElement):
    """ The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.systemType = None
        """ The standard that is used to operate and communicate.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.version = None
        """ The version of the standard that is used to operate and communicate.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(DeviceDefinitionSpecialization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionSpecialization, self).elementProperties()
        js.extend([
            ("systemType", "systemType", fhirdatatypes.FHIRString, False, None, True, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js




class DeviceDefinitionUdiDeviceIdentifier(backboneelement.BackboneElement):
    """ Unique Device Identifier (UDI) Barcode string.
    
    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.deviceIdentifier = None
        """ The identifier that is to be associated with every Device that
        references this DeviceDefintiion for the issuer and jurisdication
        porvided in the DeviceDefinition.udiDeviceIdentifier.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.issuer = None
        """ The organization that assigns the identifier algorithm.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.jurisdiction = None
        """ The jurisdiction to which the deviceIdentifier applies.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        super(DeviceDefinitionUdiDeviceIdentifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionUdiDeviceIdentifier, self).elementProperties()
        js.extend([
            ("deviceIdentifier", "deviceIdentifier", fhirdatatypes.FHIRString, False, None, True, None), 
            ("issuer", "issuer", fhirdatatypes.FHIRUri, False, None, True, None), 
            ("jurisdiction", "jurisdiction", fhirdatatypes.FHIRUri, False, None, True, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import contactpoint

from fhirclient.codesystems import devicenametype

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import prodcharacteristic

from fhirclient.models import productshelflife

from fhirclient.models import quantity

