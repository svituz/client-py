#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SpecimenDefinition)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class SpecimenDefinition(domainresource.DomainResource):
    """ Kind of specimen.
    
    A kind of specimen with associated set of requirements.
    """
    
    resource_type = "SpecimenDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business identifier of a kind of specimen.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.typeCollected = None
        """ Kind of material to collect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patientPreparation = None
        """ Patient preparation for collection.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.timeAspect = None
        """ Time aspect for collection.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.collection = None
        """ Specimen collection procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.typeTested = None
        """ Specimen in container intended for testing by lab.
        List of `SpecimenDefinitionTypeTested` items (represented as `dict` in JSON). """
        
        super(SpecimenDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinition, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False, None), 
            ("typeCollected", "typeCollected", codeableconcept.CodeableConcept, False, None, False, None), 
            ("patientPreparation", "patientPreparation", codeableconcept.CodeableConcept, True, None, False, None), 
            ("timeAspect", "timeAspect", fhirdatatypes.FHIRString, False, None, False, None), 
            ("collection", "collection", codeableconcept.CodeableConcept, True, None, False, None), 
            ("typeTested", "typeTested", SpecimenDefinitionTypeTested, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class SpecimenDefinitionTypeTested(backboneelement.BackboneElement):
    """ Specimen in container intended for testing by lab.
    
    Specimen conditioned in a container as expected by the testing laboratory.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.isDerived = None
        """ Primary or secondary specimen.
        Type `bool`. """
        
        self.type = None
        """ Type of intended specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.preference = None
        """ preferred | alternate.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.container = None
        """ The specimen's container.
        Type `SpecimenDefinitionTypeTestedContainer` (represented as `dict` in JSON). """
        
        self.requirement = None
        """ Specimen requirements.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.retentionTime = None
        """ Specimen retention time.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.rejectionCriterion = None
        """ Rejection criterion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.handling = None
        """ Specimen handling before testing.
        List of `SpecimenDefinitionTypeTestedHandling` items (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionTypeTested, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTested, self).elementProperties()
        js.extend([
            ("isDerived", "isDerived", bool, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("preference", "preference", fhirdatatypes.FHIRCode, False, None, True, specimencontainedpreference.SpecimenContainedPreference), 
            ("container", "container", SpecimenDefinitionTypeTestedContainer, False, None, False, None), 
            ("requirement", "requirement", fhirdatatypes.FHIRString, False, None, False, None), 
            ("retentionTime", "retentionTime", duration.Duration, False, None, False, None), 
            ("rejectionCriterion", "rejectionCriterion", codeableconcept.CodeableConcept, True, None, False, None), 
            ("handling", "handling", SpecimenDefinitionTypeTestedHandling, True, None, False, None), 
        ])
        return js




class SpecimenDefinitionTypeTestedContainer(backboneelement.BackboneElement):
    """ The specimen's container.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.material = None
        """ Container material.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ Kind of container associated with the kind of specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.cap = None
        """ Color of container cap.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ Container description.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.capacity = None
        """ Container capacity.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.minimumVolumeQuantity = None
        """ Minimum volume.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.minimumVolumeString = None
        """ Minimum volume.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.additive = None
        """ Additive associated with container.
        List of `SpecimenDefinitionTypeTestedContainerAdditive` items (represented as `dict` in JSON). """
        
        self.preparation = None
        """ Specimen container preparation.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(SpecimenDefinitionTypeTestedContainer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedContainer, self).elementProperties()
        js.extend([
            ("material", "material", codeableconcept.CodeableConcept, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("cap", "cap", codeableconcept.CodeableConcept, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("capacity", "capacity", quantity.Quantity, False, None, False, None), 
            ("minimumVolumeQuantity", "minimumVolumeQuantity", quantity.Quantity, False, "minimumVolume", False, None), 
            ("minimumVolumeString", "minimumVolumeString", fhirdatatypes.FHIRString, False, "minimumVolume", False, None), 
            ("additive", "additive", SpecimenDefinitionTypeTestedContainerAdditive, True, None, False, None), 
            ("preparation", "preparation", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js




class SpecimenDefinitionTypeTestedContainerAdditive(backboneelement.BackboneElement):
    """ Additive associated with container.
    
    Substance introduced in the kind of container to preserve, maintain or
    enhance the specimen. Examples: Formalin, Citrate, EDTA.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additiveCodeableConcept = None
        """ Additive associated with container.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.additiveReference = None
        """ Additive associated with container.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionTypeTestedContainerAdditive, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedContainerAdditive, self).elementProperties()
        js.extend([
            ("additiveCodeableConcept", "additiveCodeableConcept", codeableconcept.CodeableConcept, False, "additive", True, None), 
            ("additiveReference", "additiveReference", fhirreference.FHIRReference, False, "additive", True, None), 
        ])
        return js




class SpecimenDefinitionTypeTestedHandling(backboneelement.BackboneElement):
    """ Specimen handling before testing.
    
    Set of instructions for preservation/transport of the specimen at a defined
    temperature interval, prior the testing process.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.temperatureQualifier = None
        """ Temperature qualifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.temperatureRange = None
        """ Temperature range.
        Type `Range` (represented as `dict` in JSON). """
        
        self.maxDuration = None
        """ Maximum preservation time.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.instruction = None
        """ Preservation instruction.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(SpecimenDefinitionTypeTestedHandling, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedHandling, self).elementProperties()
        js.extend([
            ("temperatureQualifier", "temperatureQualifier", codeableconcept.CodeableConcept, False, None, False, None), 
            ("temperatureRange", "temperatureRange", range.Range, False, None, False, None), 
            ("maxDuration", "maxDuration", duration.Duration, False, None, False, None), 
            ("instruction", "instruction", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import duration

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import quantity

from fhirclient.models import range

from fhirclient.codesystems import specimencontainedpreference

