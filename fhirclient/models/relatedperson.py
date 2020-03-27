#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/RelatedPerson)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class RelatedPerson(domainresource.DomainResource):
    """ A person that is related to a patient, but who is not a direct target of
    care.
    
    Information about a person that is involved in the care for a patient, but
    who is not the target of healthcare, nor has a formal responsibility in the
    care process.
    """
    
    resource_type = "RelatedPerson"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ A human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.active = None
        """ Whether this related person's record is in active use.
        Type `bool`. """
        
        self.patient = None
        """ The patient this person is related to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ The nature of the relationship.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        """ The date on which the related person was born.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.address = None
        """ Address where the related person can be contacted or visited.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.photo = None
        """ Image of the person.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.period = None
        """ Period of time that this relationship is considered valid.
        Type `Period` (represented as `dict` in JSON). """
        
        self.communication = None
        """ A language which may be used to communicate with about the
        patient's health.
        List of `RelatedPersonCommunication` items (represented as `dict` in JSON). """
        
        super(RelatedPerson, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RelatedPerson, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("active", "active", bool, False, None, False, None), 
            ("patient", "patient", fhirreference.FHIRReference, False, None, True, None), 
            ("relationship", "relationship", codeableconcept.CodeableConcept, True, None, False, None), 
            ("name", "name", humanname.HumanName, True, None, False, None), 
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False, None), 
            ("gender", "gender", fhirdatatypes.FHIRCode, False, None, False, administrativegender.AdministrativeGender), 
            ("birthDate", "birthDate", fhirdatatypes.FHIRDate, False, None, False, None), 
            ("address", "address", address.Address, True, None, False, None), 
            ("photo", "photo", attachment.Attachment, True, None, False, None), 
            ("period", "period", period.Period, False, None, False, None), 
            ("communication", "communication", RelatedPersonCommunication, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class RelatedPersonCommunication(backboneelement.BackboneElement):
    """ A language which may be used to communicate with about the patient's health.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        """ The language which can be used to communicate with the patient
        about his or her health.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.preferred = None
        """ Language preference indicator.
        Type `bool`. """
        
        super(RelatedPersonCommunication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RelatedPersonCommunication, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, True, None), 
            ("preferred", "preferred", bool, False, None, False, None), 
        ])
        return js



from fhirclient.models import address

from fhirclient.codesystems import administrativegender

from fhirclient.models import attachment

from fhirclient.models import codeableconcept

from fhirclient.models import contactpoint

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import humanname

from fhirclient.models import identifier

from fhirclient.models import period

