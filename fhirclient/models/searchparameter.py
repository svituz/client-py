#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SearchParameter) on 2020-03-26.
#  2020, SMART Health IT.


from . import domainresource

class SearchParameter(domainresource.DomainResource):
    """ Search parameter for a resource.
    
    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """
    
    resource_type = "SearchParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.base = None
        """ The resource type(s) this search parameter applies to.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.chain = None
        """ Chained names supported.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.code = None
        """ Code used in URL.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.comparator = None
        """ eq | ne | gt | lt | ge | le | sa | eb | ap.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.component = None
        """ For Composite resources to define the parts.
        List of `SearchParameterComponent` items (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.derivedFrom = None
        """ Original definition for the search parameter.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the search parameter.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.expression = None
        """ FHIRPath expression that extracts the values.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for search parameter (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.modifier = None
        """ missing | exact | contains | not | text | in | not-in | below |
        above | type | identifier | ofType.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.multipleAnd = None
        """ Allow multiple parameters (and).
        Type `bool`. """
        
        self.multipleOr = None
        """ Allow multiple values per parameter (or).
        Type `bool`. """
        
        self.name = None
        """ Name for this search parameter (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.purpose = None
        """ Why this search parameter is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.target = None
        """ Types of resource (if a resource reference).
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.type = None
        """ number | date | string | token | reference | composite | quantity |
        uri | special.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.url = None
        """ Canonical identifier for this search parameter, represented as a
        URI (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the search parameter.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.xpath = None
        """ XPath that extracts the values.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.xpathUsage = None
        """ normal | phonetic | nearby | distance | other.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(SearchParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SearchParameter, self).elementProperties()
        js.extend([
            ("base", "base", fhirdatatypes.FHIRCode, True, None, True),
            ("chain", "chain", fhirdatatypes.FHIRString, True, None, False),
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True),
            ("comparator", "comparator", fhirdatatypes.FHIRCode, True, None, False),
            ("component", "component", SearchParameterComponent, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False),
            ("derivedFrom", "derivedFrom", fhirdatatypes.FHIRCanonical, False, None, False),
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("expression", "expression", fhirdatatypes.FHIRString, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("modifier", "modifier", fhirdatatypes.FHIRCode, True, None, False),
            ("multipleAnd", "multipleAnd", bool, False, None, False),
            ("multipleOr", "multipleOr", bool, False, None, False),
            ("name", "name", fhirdatatypes.FHIRString, False, None, True),
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False),
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True),
            ("target", "target", fhirdatatypes.FHIRCode, True, None, False),
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True),
            ("url", "url", fhirdatatypes.FHIRUri, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", fhirdatatypes.FHIRString, False, None, False),
            ("xpath", "xpath", fhirdatatypes.FHIRString, False, None, False),
            ("xpathUsage", "xpathUsage", fhirdatatypes.FHIRCode, False, None, False),
        ])
        return js



from . import backboneelement

class SearchParameterComponent(backboneelement.BackboneElement):
    """ For Composite resources to define the parts.
    
    Used to define the parts of a composite search parameter.
    """
    
    resource_type = "SearchParameterComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        """ Defines how the part works.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.expression = None
        """ Subexpression relative to main expression.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(SearchParameterComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SearchParameterComponent, self).elementProperties()
        js.extend([
            ("definition", "definition", fhirdatatypes.FHIRCanonical, False, None, True),
            ("expression", "expression", fhirdatatypes.FHIRString, False, None, True),
        ])
        return js



import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']

try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']

try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']

