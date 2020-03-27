#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SubstanceReferenceInformation)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class SubstanceReferenceInformation(domainresource.DomainResource):
    """ Todo.
    """
    
    resource_type = "SubstanceReferenceInformation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        """ Todo.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.gene = None
        """ Todo.
        List of `SubstanceReferenceInformationGene` items (represented as `dict` in JSON). """
        
        self.geneElement = None
        """ Todo.
        List of `SubstanceReferenceInformationGeneElement` items (represented as `dict` in JSON). """
        
        self.classification = None
        """ Todo.
        List of `SubstanceReferenceInformationClassification` items (represented as `dict` in JSON). """
        
        self.target = None
        """ Todo.
        List of `SubstanceReferenceInformationTarget` items (represented as `dict` in JSON). """
        
        super(SubstanceReferenceInformation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceReferenceInformation, self).elementProperties()
        js.extend([
            ("comment", "comment", fhirdatatypes.FHIRString, False, None, False, None), 
            ("gene", "gene", SubstanceReferenceInformationGene, True, None, False, None), 
            ("geneElement", "geneElement", SubstanceReferenceInformationGeneElement, True, None, False, None), 
            ("classification", "classification", SubstanceReferenceInformationClassification, True, None, False, None), 
            ("target", "target", SubstanceReferenceInformationTarget, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class SubstanceReferenceInformationClassification(backboneelement.BackboneElement):
    """ Todo.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.domain = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.classification = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subtype = None
        """ Todo.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.source = None
        """ Todo.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(SubstanceReferenceInformationClassification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceReferenceInformationClassification, self).elementProperties()
        js.extend([
            ("domain", "domain", codeableconcept.CodeableConcept, False, None, False, None), 
            ("classification", "classification", codeableconcept.CodeableConcept, False, None, False, None), 
            ("subtype", "subtype", codeableconcept.CodeableConcept, True, None, False, None), 
            ("source", "source", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js




class SubstanceReferenceInformationGene(backboneelement.BackboneElement):
    """ Todo.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.geneSequenceOrigin = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.gene = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.source = None
        """ Todo.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(SubstanceReferenceInformationGene, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceReferenceInformationGene, self).elementProperties()
        js.extend([
            ("geneSequenceOrigin", "geneSequenceOrigin", codeableconcept.CodeableConcept, False, None, False, None), 
            ("gene", "gene", codeableconcept.CodeableConcept, False, None, False, None), 
            ("source", "source", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js




class SubstanceReferenceInformationGeneElement(backboneelement.BackboneElement):
    """ Todo.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.element = None
        """ Todo.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.source = None
        """ Todo.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(SubstanceReferenceInformationGeneElement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceReferenceInformationGeneElement, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("element", "element", identifier.Identifier, False, None, False, None), 
            ("source", "source", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js




class SubstanceReferenceInformationTarget(backboneelement.BackboneElement):
    """ Todo.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.target = None
        """ Todo.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.interaction = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.organism = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.organismType = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.amountQuantity = None
        """ Todo.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.amountRange = None
        """ Todo.
        Type `Range` (represented as `dict` in JSON). """
        
        self.amountString = None
        """ Todo.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.amountType = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.source = None
        """ Todo.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(SubstanceReferenceInformationTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceReferenceInformationTarget, self).elementProperties()
        js.extend([
            ("target", "target", identifier.Identifier, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("interaction", "interaction", codeableconcept.CodeableConcept, False, None, False, None), 
            ("organism", "organism", codeableconcept.CodeableConcept, False, None, False, None), 
            ("organismType", "organismType", codeableconcept.CodeableConcept, False, None, False, None), 
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False, None), 
            ("amountRange", "amountRange", range.Range, False, "amount", False, None), 
            ("amountString", "amountString", fhirdatatypes.FHIRString, False, "amount", False, None), 
            ("amountType", "amountType", codeableconcept.CodeableConcept, False, None, False, None), 
            ("source", "source", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import quantity

from fhirclient.models import range

