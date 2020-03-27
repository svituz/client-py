#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Patient)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Patient(domainresource.DomainResource):
    """ Information about an individual or animal receiving health care services.
    
    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """
    
    resource_type = "Patient"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ An identifier for this patient.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.active = None
        """ Whether this patient's record is in active use.
        Type `bool`. """
        
        self.name = None
        """ A name associated with the patient.
        List of `HumanName` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the individual.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.birthDate = None
        """ The date of birth for the individual.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deceasedBoolean = None
        """ Indicates if the individual is deceased or not.
        Type `bool`. """
        
        self.deceasedDateTime = None
        """ Indicates if the individual is deceased or not.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.address = None
        """ An address for the individual.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.maritalStatus = None
        """ Marital (civil) status of a patient.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.multipleBirthBoolean = None
        """ Whether patient is part of a multiple birth.
        Type `bool`. """
        
        self.multipleBirthInteger = None
        """ Whether patient is part of a multiple birth.
        Type `int`. """
        
        self.photo = None
        """ Image of the patient.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.contact = None
        """ A contact party (e.g. guardian, partner, friend) for the patient.
        List of `PatientContact` items (represented as `dict` in JSON). """
        
        self.communication = None
        """ A language which may be used to communicate with the patient about
        his or her health.
        List of `PatientCommunication` items (represented as `dict` in JSON). """
        
        self.generalPractitioner = None
        """ Patient's nominated primary care provider.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ Organization that is the custodian of the patient record.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.link = None
        """ Link to another patient resource that concerns the same actual
        person.
        List of `PatientLink` items (represented as `dict` in JSON). """
        
        super(Patient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Patient, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("active", "active", bool, False, None, False, None), 
            ("name", "name", humanname.HumanName, True, None, False, None), 
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False, None), 
            ("gender", "gender", fhirdatatypes.FHIRCode, False, None, False, administrativegender.AdministrativeGender), 
            ("birthDate", "birthDate", fhirdatatypes.FHIRDate, False, None, False, None), 
            ("deceasedBoolean", "deceasedBoolean", bool, False, "deceased", False, None), 
            ("deceasedDateTime", "deceasedDateTime", fhirdatatypes.FHIRDateTime, False, "deceased", False, None), 
            ("address", "address", address.Address, True, None, False, None), 
            ("maritalStatus", "maritalStatus", codeableconcept.CodeableConcept, False, None, False, None), 
            ("multipleBirthBoolean", "multipleBirthBoolean", bool, False, "multipleBirth", False, None), 
            ("multipleBirthInteger", "multipleBirthInteger", int, False, "multipleBirth", False, None), 
            ("photo", "photo", attachment.Attachment, True, None, False, None), 
            ("contact", "contact", PatientContact, True, None, False, None), 
            ("communication", "communication", PatientCommunication, True, None, False, None), 
            ("generalPractitioner", "generalPractitioner", fhirreference.FHIRReference, True, None, False, None), 
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False, None), 
            ("link", "link", PatientLink, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class PatientCommunication(backboneelement.BackboneElement):
    """ A language which may be used to communicate with the patient about his or
    her health.
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
        
        super(PatientCommunication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PatientCommunication, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, True, None), 
            ("preferred", "preferred", bool, False, None, False, None), 
        ])
        return js




class PatientContact(backboneelement.BackboneElement):
    """ A contact party (e.g. guardian, partner, friend) for the patient.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.relationship = None
        """ The kind of relationship.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        """ A name associated with the contact person.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.address = None
        """ Address for the contact person.
        Type `Address` (represented as `dict` in JSON). """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.organization = None
        """ Organization that is associated with the contact.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ The period during which this contact person or organization is
        valid to be contacted relating to this patient.
        Type `Period` (represented as `dict` in JSON). """
        
        super(PatientContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PatientContact, self).elementProperties()
        js.extend([
            ("relationship", "relationship", codeableconcept.CodeableConcept, True, None, False, None), 
            ("name", "name", humanname.HumanName, False, None, False, None), 
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False, None), 
            ("address", "address", address.Address, False, None, False, None), 
            ("gender", "gender", fhirdatatypes.FHIRCode, False, None, False, administrativegender.AdministrativeGender), 
            ("organization", "organization", fhirreference.FHIRReference, False, None, False, None), 
            ("period", "period", period.Period, False, None, False, None), 
        ])
        return js




class PatientLink(backboneelement.BackboneElement):
    """ Link to another patient resource that concerns the same actual person.
    
    Link to another patient resource that concerns the same actual patient.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.other = None
        """ The other patient or related person resource that the link refers
        to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ replaced-by | replaces | refer | seealso.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(PatientLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PatientLink, self).elementProperties()
        js.extend([
            ("other", "other", fhirreference.FHIRReference, False, None, True, None), 
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, linktype.LinkType), 
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

from fhirclient.codesystems import linktype

from fhirclient.models import period

