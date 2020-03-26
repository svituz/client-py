#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/OperationDefinition) on 2020-03-26.
#  2020, SMART Health IT.


from . import domainresource

class OperationDefinition(domainresource.DomainResource):
    """ Definition of an operation or a named query.
    
    A formal computable definition of an operation (on the RESTful interface)
    or a named query (using the search interaction).
    """
    
    resource_type = "OperationDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.affectsState = None
        """ Whether content is changed by the operation.
        Type `bool`. """
        
        self.base = None
        """ Marks this as a profile of the base.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.code = None
        """ Name used to invoke the operation.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.comment = None
        """ Additional information about use.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the operation definition.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.inputProfile = None
        """ Validation information for in parameters.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.instance = None
        """ Invoke on an instance?.
        Type `bool`. """
        
        self.jurisdiction = None
        """ Intended jurisdiction for operation definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.kind = None
        """ operation | query.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this operation definition (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.outputProfile = None
        """ Validation information for out parameters.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.overload = None
        """ Define overloaded variants for when  generating code.
        List of `OperationDefinitionOverload` items (represented as `dict` in JSON). """
        
        self.parameter = None
        """ Parameters for the operation/query.
        List of `OperationDefinitionParameter` items (represented as `dict` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.purpose = None
        """ Why this operation definition is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.resource = None
        """ Types this operation applies to.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.system = None
        """ Invoke at the system level?.
        Type `bool`. """
        
        self.title = None
        """ Name for this operation definition (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.type = None
        """ Invoke at the type level?.
        Type `bool`. """
        
        self.url = None
        """ Canonical identifier for this operation definition, represented as
        a URI (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the operation definition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(OperationDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinition, self).elementProperties()
        js.extend([
            ("affectsState", "affectsState", bool, False, None, False),
            ("base", "base", fhirdatatypes.FHIRCanonical, False, None, False),
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True),
            ("comment", "comment", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False),
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("inputProfile", "inputProfile", fhirdatatypes.FHIRCanonical, False, None, False),
            ("instance", "instance", bool, False, None, True),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("kind", "kind", fhirdatatypes.FHIRCode, False, None, True),
            ("name", "name", fhirdatatypes.FHIRString, False, None, True),
            ("outputProfile", "outputProfile", fhirdatatypes.FHIRCanonical, False, None, False),
            ("overload", "overload", OperationDefinitionOverload, True, None, False),
            ("parameter", "parameter", OperationDefinitionParameter, True, None, False),
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False),
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("resource", "resource", fhirdatatypes.FHIRCode, True, None, False),
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True),
            ("system", "system", bool, False, None, True),
            ("title", "title", fhirdatatypes.FHIRString, False, None, False),
            ("type", "type", bool, False, None, True),
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", fhirdatatypes.FHIRString, False, None, False),
        ])
        return js



from . import backboneelement

class OperationDefinitionOverload(backboneelement.BackboneElement):
    """ Define overloaded variants for when  generating code.
    
    Defines an appropriate combination of parameters to use when invoking this
    operation, to help code generators when generating overloaded parameter
    sets for this operation.
    """
    
    resource_type = "OperationDefinitionOverload"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        """ Comments to go on overload.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.parameterName = None
        """ Name of parameter to include in overload.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        super(OperationDefinitionOverload, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionOverload, self).elementProperties()
        js.extend([
            ("comment", "comment", fhirdatatypes.FHIRString, False, None, False),
            ("parameterName", "parameterName", fhirdatatypes.FHIRString, True, None, False),
        ])
        return js




class OperationDefinitionParameter(backboneelement.BackboneElement):
    """ Parameters for the operation/query.
    
    The parameters for the operation/query.
    """
    
    resource_type = "OperationDefinitionParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.binding = None
        """ ValueSet details if this is coded.
        Type `OperationDefinitionParameterBinding` (represented as `dict` in JSON). """
        
        self.documentation = None
        """ Description of meaning/use.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.max = None
        """ Maximum Cardinality (a number or *).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.min = None
        """ Minimum Cardinality.
        Type `int`. """
        
        self.name = None
        """ Name in Parameters.parameter.name or in URL.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.part = None
        """ Parts of a nested Parameter.
        List of `OperationDefinitionParameter` items (represented as `dict` in JSON). """
        
        self.referencedFrom = None
        """ References to this parameter.
        List of `OperationDefinitionParameterReferencedFrom` items (represented as `dict` in JSON). """
        
        self.searchType = None
        """ number | date | string | token | reference | composite | quantity |
        uri | special.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.targetProfile = None
        """ If type is Reference | canonical, allowed targets.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.type = None
        """ What type this parameter has.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.use = None
        """ in | out.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(OperationDefinitionParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionParameter, self).elementProperties()
        js.extend([
            ("binding", "binding", OperationDefinitionParameterBinding, False, None, False),
            ("documentation", "documentation", fhirdatatypes.FHIRString, False, None, False),
            ("max", "max", fhirdatatypes.FHIRString, False, None, True),
            ("min", "min", int, False, None, True),
            ("name", "name", fhirdatatypes.FHIRCode, False, None, True),
            ("part", "part", OperationDefinitionParameter, True, None, False),
            ("referencedFrom", "referencedFrom", OperationDefinitionParameterReferencedFrom, True, None, False),
            ("searchType", "searchType", fhirdatatypes.FHIRCode, False, None, False),
            ("targetProfile", "targetProfile", fhirdatatypes.FHIRCanonical, True, None, False),
            ("type", "type", fhirdatatypes.FHIRCode, False, None, False),
            ("use", "use", fhirdatatypes.FHIRCode, False, None, True),
        ])
        return js




class OperationDefinitionParameterBinding(backboneelement.BackboneElement):
    """ ValueSet details if this is coded.
    
    Binds to a value set if this parameter is coded (code, Coding,
    CodeableConcept).
    """
    
    resource_type = "OperationDefinitionParameterBinding"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.strength = None
        """ required | extensible | preferred | example.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.valueSet = None
        """ Source of value set.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        super(OperationDefinitionParameterBinding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionParameterBinding, self).elementProperties()
        js.extend([
            ("strength", "strength", fhirdatatypes.FHIRCode, False, None, True),
            ("valueSet", "valueSet", fhirdatatypes.FHIRCanonical, False, None, True),
        ])
        return js




class OperationDefinitionParameterReferencedFrom(backboneelement.BackboneElement):
    """ References to this parameter.
    
    Identifies other resource parameters within the operation invocation that
    are expected to resolve to this resource.
    """
    
    resource_type = "OperationDefinitionParameterReferencedFrom"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.source = None
        """ Referencing parameter.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.sourceId = None
        """ Element id of reference.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(OperationDefinitionParameterReferencedFrom, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionParameterReferencedFrom, self).elementProperties()
        js.extend([
            ("source", "source", fhirdatatypes.FHIRString, False, None, True),
            ("sourceId", "sourceId", fhirdatatypes.FHIRString, False, None, False),
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

