#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Organization)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Organization(domainresource.DomainResource):
    """ A grouping of people or organizations with a common purpose.
    
    A formally or informally recognized grouping of people or organizations
    formed for the purpose of achieving some form of collective action.
    Includes companies, institutions, corporations, departments, community
    groups, healthcare practice groups, payer/insurer, etc.
    """
    
    resource_type = "Organization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Identifies this organization  across multiple systems.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.active = None
        """ Whether the organization's record is still in active use.
        Type `bool`. """
        
        self.type = None
        """ Kind of organization.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name used for the organization.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.alias = None
        """ A list of alternate names that the organization is known as, or was
        known as in the past.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.telecom = None
        """ A contact detail for the organization.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.address = None
        """ An address for the organization.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ The organization of which this organization forms a part.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact for the organization for a certain purpose.
        List of `OrganizationContact` items (represented as `dict` in JSON). """
        
        self.endpoint = None
        """ Technical endpoints providing access to services operated for the
        organization.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(Organization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Organization, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("active", "active", bool, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, True, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("alias", "alias", fhirdatatypes.FHIRString, True, None, False, None), 
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False, None), 
            ("address", "address", address.Address, True, None, False, None), 
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False, None), 
            ("contact", "contact", OrganizationContact, True, None, False, None), 
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class OrganizationContact(backboneelement.BackboneElement):
    """ Contact for the organization for a certain purpose.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.purpose = None
        """ The type of contact.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.name = None
        """ A name associated with the contact.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ Contact details (telephone, email, etc.)  for a contact.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.address = None
        """ Visiting or postal addresses for the contact.
        Type `Address` (represented as `dict` in JSON). """
        
        super(OrganizationContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OrganizationContact, self).elementProperties()
        js.extend([
            ("purpose", "purpose", codeableconcept.CodeableConcept, False, None, False, None), 
            ("name", "name", humanname.HumanName, False, None, False, None), 
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False, None), 
            ("address", "address", address.Address, False, None, False, None), 
        ])
        return js



from fhirclient.models import address

from fhirclient.models import codeableconcept

from fhirclient.models import contactpoint

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import humanname

from fhirclient.models import identifier

