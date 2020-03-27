#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Group)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Group(domainresource.DomainResource):
    """ Group of multiple entities.
    
    Represents a defined collection of entities that may be discussed or acted
    upon collectively but which are not expected to act collectively, and are
    not formally or legally recognized; i.e. a collection of entities that
    isn't an Organization.
    """
    
    resource_type = "Group"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Unique id.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.active = None
        """ Whether this group's record is in active use.
        Type `bool`. """
        
        self.type = None
        """ person | animal | practitioner | device | medication | substance.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.actual = None
        """ Descriptive or actual.
        Type `bool`. """
        
        self.code = None
        """ Kind of Group members.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.name = None
        """ Label for Group.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.quantity = None
        """ Number of members.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.managingEntity = None
        """ Entity that is the custodian of the Group's definition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.characteristic = None
        """ Include / Exclude group members by Trait.
        List of `GroupCharacteristic` items (represented as `dict` in JSON). """
        
        self.member = None
        """ Who or what is in group.
        List of `GroupMember` items (represented as `dict` in JSON). """
        
        super(Group, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Group, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("active", "active", bool, False, None, False, None), 
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, grouptype.GroupType), 
            ("actual", "actual", bool, False, None, True, None), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("quantity", "quantity", fhirdatatypes.FHIRUnsignedInt, False, None, False, None), 
            ("managingEntity", "managingEntity", fhirreference.FHIRReference, False, None, False, None), 
            ("characteristic", "characteristic", GroupCharacteristic, True, None, False, None), 
            ("member", "member", GroupMember, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class GroupCharacteristic(backboneelement.BackboneElement):
    """ Include / Exclude group members by Trait.
    
    Identifies traits whose presence r absence is shared by members of the
    group.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Kind of characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCodeableConcept = None
        """ Value held by characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueBoolean = None
        """ Value held by characteristic.
        Type `bool`. """
        
        self.valueQuantity = None
        """ Value held by characteristic.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Value held by characteristic.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Value held by characteristic.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.exclude = None
        """ Group includes or excludes.
        Type `bool`. """
        
        self.period = None
        """ Period over which characteristic is tested.
        Type `Period` (represented as `dict` in JSON). """
        
        super(GroupCharacteristic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GroupCharacteristic, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True, None), 
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True, None), 
            ("valueBoolean", "valueBoolean", bool, False, "value", True, None), 
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True, None), 
            ("valueRange", "valueRange", range.Range, False, "value", True, None), 
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True, None), 
            ("exclude", "exclude", bool, False, None, True, None), 
            ("period", "period", period.Period, False, None, False, None), 
        ])
        return js




class GroupMember(backboneelement.BackboneElement):
    """ Who or what is in group.
    
    Identifies the resource instances that are members of the group.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.entity = None
        """ Reference to the group member.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ Period member belonged to the group.
        Type `Period` (represented as `dict` in JSON). """
        
        self.inactive = None
        """ If member is no longer in group.
        Type `bool`. """
        
        super(GroupMember, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GroupMember, self).elementProperties()
        js.extend([
            ("entity", "entity", fhirreference.FHIRReference, False, None, True, None), 
            ("period", "period", period.Period, False, None, False, None), 
            ("inactive", "inactive", bool, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.codesystems import grouptype

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.models import quantity

from fhirclient.models import range

