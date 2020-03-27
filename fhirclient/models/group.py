#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Group)
#  2020, SMART Health IT.


from . import domainresource

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
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("active", "active", bool, False, None, False),
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True),
            ("actual", "actual", bool, False, None, True),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("name", "name", fhirdatatypes.FHIRString, False, None, False),
            ("quantity", "quantity", fhirdatatypes.FHIRUnsignedInt, False, None, False),
            ("managingEntity", "managingEntity", fhirreference.FHIRReference, False, None, False),
            ("characteristic", "characteristic", GroupCharacteristic, True, None, False),
            ("member", "member", GroupMember, True, None, False),
        ])
        return js



from . import backboneelement

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
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("exclude", "exclude", bool, False, None, True),
            ("period", "period", period.Period, False, None, False),
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
            ("entity", "entity", fhirreference.FHIRReference, False, None, True),
            ("period", "period", period.Period, False, None, False),
            ("inactive", "inactive", bool, False, None, False),
        ])
        return js



import sys
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']

try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']

try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']

