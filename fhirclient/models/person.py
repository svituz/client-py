#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Person)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Person(domainresource.DomainResource):
    """ A generic person record.
    
    Demographics and administrative information about a person independent of a
    specific health-related context.
    """
    
    resource_type = "Person"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ A human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ A name associated with the person.
        List of `HumanName` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.birthDate = None
        """ The date on which the person was born.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.address = None
        """ One or more addresses for the person.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.photo = None
        """ Image of the person.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ The organization that is the custodian of the person record.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.active = None
        """ This person's record is in active use.
        Type `bool`. """
        
        self.link = None
        """ Link to a resource that concerns the same actual person.
        List of `PersonLink` items (represented as `dict` in JSON). """
        
        super(Person, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Person, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("name", "name", humanname.HumanName, True, None, False, None), 
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False, None), 
            ("gender", "gender", fhirdatatypes.FHIRCode, False, None, False, administrativegender.AdministrativeGender), 
            ("birthDate", "birthDate", fhirdatatypes.FHIRDate, False, None, False, None), 
            ("address", "address", address.Address, True, None, False, None), 
            ("photo", "photo", attachment.Attachment, False, None, False, None), 
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False, None), 
            ("active", "active", bool, False, None, False, None), 
            ("link", "link", PersonLink, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class PersonLink(backboneelement.BackboneElement):
    """ Link to a resource that concerns the same actual person.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.target = None
        """ The resource to which this actual person is associated.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.assurance = None
        """ level1 | level2 | level3 | level4.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(PersonLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PersonLink, self).elementProperties()
        js.extend([
            ("target", "target", fhirreference.FHIRReference, False, None, True, None), 
            ("assurance", "assurance", fhirdatatypes.FHIRCode, False, None, False, identityassurancelevel.IdentityAssuranceLevel), 
        ])
        return js



from fhirclient.models import address

from fhirclient.codesystems import administrativegender

from fhirclient.models import attachment

from fhirclient.models import contactpoint

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import humanname

from fhirclient.models import identifier

from fhirclient.codesystems import identityassurancelevel

