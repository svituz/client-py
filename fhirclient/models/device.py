#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Device)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Device(domainresource.DomainResource):
    """ Item used in healthcare.
    
    A type of a manufactured item that is used in the provision of healthcare
    without being substantially changed through that activity. The device may
    be a medical or non-medical device.
    """
    
    resource_type = "Device"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Instance identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.definition = None
        """ The reference to the definition for the device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.udiCarrier = None
        """ Unique Device Identifier (UDI) Barcode string.
        List of `DeviceUdiCarrier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | inactive | entered-in-error | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.statusReason = None
        """ online | paused | standby | offline | not-ready | transduc-discon |
        hw-discon | off.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.distinctIdentifier = None
        """ The distinct identification string.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.manufacturer = None
        """ Name of device manufacturer.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.manufactureDate = None
        """ Date when the device was made.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.expirationDate = None
        """ Date and time of expiry of this device (if applicable).
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.lotNumber = None
        """ Lot number of manufacture.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.serialNumber = None
        """ Serial number assigned by the manufacturer.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.deviceName = None
        """ The name of the device as given by the manufacturer.
        List of `DeviceDeviceName` items (represented as `dict` in JSON). """
        
        self.modelNumber = None
        """ The model number for the device.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.partNumber = None
        """ The part number of the device.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.type = None
        """ The kind or type of device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.specialization = None
        """ The capabilities supported on a  device, the standards to which the
        device conforms for a particular purpose, and used for the
        communication.
        List of `DeviceSpecialization` items (represented as `dict` in JSON). """
        
        self.version = None
        """ The actual design of the device or software version running on the
        device.
        List of `DeviceVersion` items (represented as `dict` in JSON). """
        
        self.property = None
        """ The actual configuration settings of a device as it actually
        operates, e.g., regulation status, time properties.
        List of `DeviceProperty` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Patient to whom Device is affixed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.owner = None
        """ Organization responsible for device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.contact = None
        """ Details for human/organization for support.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where the device is found.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.url = None
        """ Network address to contact device.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.note = None
        """ Device notes and comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.safety = None
        """ Safety Characteristics of Device.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.parent = None
        """ The parent device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(Device, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Device, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("definition", "definition", fhirreference.FHIRReference, False, None, False, None), 
            ("udiCarrier", "udiCarrier", DeviceUdiCarrier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, False, fhirdevicestatus.FHIRDeviceStatus), 
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, True, None, False, None), 
            ("distinctIdentifier", "distinctIdentifier", fhirdatatypes.FHIRString, False, None, False, None), 
            ("manufacturer", "manufacturer", fhirdatatypes.FHIRString, False, None, False, None), 
            ("manufactureDate", "manufactureDate", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("expirationDate", "expirationDate", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("lotNumber", "lotNumber", fhirdatatypes.FHIRString, False, None, False, None), 
            ("serialNumber", "serialNumber", fhirdatatypes.FHIRString, False, None, False, None), 
            ("deviceName", "deviceName", DeviceDeviceName, True, None, False, None), 
            ("modelNumber", "modelNumber", fhirdatatypes.FHIRString, False, None, False, None), 
            ("partNumber", "partNumber", fhirdatatypes.FHIRString, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("specialization", "specialization", DeviceSpecialization, True, None, False, None), 
            ("version", "version", DeviceVersion, True, None, False, None), 
            ("property", "property", DeviceProperty, True, None, False, None), 
            ("patient", "patient", fhirreference.FHIRReference, False, None, False, None), 
            ("owner", "owner", fhirreference.FHIRReference, False, None, False, None), 
            ("contact", "contact", contactpoint.ContactPoint, True, None, False, None), 
            ("location", "location", fhirreference.FHIRReference, False, None, False, None), 
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("safety", "safety", codeableconcept.CodeableConcept, True, None, False, None), 
            ("parent", "parent", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class DeviceDeviceName(backboneelement.BackboneElement):
    """ The name of the device as given by the manufacturer.
    
    This represents the manufacturer's name of the device as provided by the
    device, from a UDI label, or by a person describing the Device.  This
    typically would be used when a person provides the name(s) or when the
    device represents one of the names available from DeviceDefinition.
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
        
        super(DeviceDeviceName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDeviceName, self).elementProperties()
        js.extend([
            ("name", "name", fhirdatatypes.FHIRString, False, None, True, None), 
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, devicenametype.DeviceNameType), 
        ])
        return js




class DeviceProperty(backboneelement.BackboneElement):
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
        
        super(DeviceProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
            ("valueQuantity", "valueQuantity", quantity.Quantity, True, None, False, None), 
            ("valueCode", "valueCode", codeableconcept.CodeableConcept, True, None, False, None), 
        ])
        return js




class DeviceSpecialization(backboneelement.BackboneElement):
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.version = None
        """ The version of the standard that is used to operate and communicate.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(DeviceSpecialization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceSpecialization, self).elementProperties()
        js.extend([
            ("systemType", "systemType", codeableconcept.CodeableConcept, False, None, True, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js




class DeviceUdiCarrier(backboneelement.BackboneElement):
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
        """ Mandatory fixed portion of UDI.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.issuer = None
        """ UDI Issuing Organization.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.jurisdiction = None
        """ Regional UDI authority.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.carrierAIDC = None
        """ UDI Machine Readable Barcode String.
        Type `FHIRBase64Binary` (represented as `str` in JSON). """
        
        self.carrierHRF = None
        """ UDI Human Readable Barcode String.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.entryType = None
        """ barcode | rfid | manual +.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(DeviceUdiCarrier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceUdiCarrier, self).elementProperties()
        js.extend([
            ("deviceIdentifier", "deviceIdentifier", fhirdatatypes.FHIRString, False, None, False, None), 
            ("issuer", "issuer", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("jurisdiction", "jurisdiction", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("carrierAIDC", "carrierAIDC", fhirdatatypes.FHIRBase64Binary, False, None, False, None), 
            ("carrierHRF", "carrierHRF", fhirdatatypes.FHIRString, False, None, False, None), 
            ("entryType", "entryType", fhirdatatypes.FHIRCode, False, None, False, udientrytype.UDIEntryType), 
        ])
        return js




class DeviceVersion(backboneelement.BackboneElement):
    """ The actual design of the device or software version running on the device.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ The type of the device version.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.component = None
        """ A single component of the device version.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.value = None
        """ The version text.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(DeviceVersion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceVersion, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("component", "component", identifier.Identifier, False, None, False, None), 
            ("value", "value", fhirdatatypes.FHIRString, False, None, True, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import contactpoint

from fhirclient.codesystems import devicenametype

from fhirclient.models import fhirdatatypes

from fhirclient.codesystems import fhirdevicestatus

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import quantity

from fhirclient.codesystems import udientrytype

