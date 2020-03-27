#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ValueSet)
#  2020, SMART Health IT.


from . import domainresource

class ValueSet(domainresource.DomainResource):
    """ A set of codes drawn from one or more code systems.
    
    A ValueSet resource instance specifies a set of codes drawn from one or
    more code systems, intended for use in a particular context. Value sets
    link between [CodeSystem](codesystem.html) definitions and their use in
    [coded elements](terminologies.html).
    """
    
    resource_type = "ValueSet"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this value set, represented as a URI
        (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the value set (business identifier).
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the value set.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this value set (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this value set (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Natural language description of the value set.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for value set (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.immutable = None
        """ Indicates whether or not any change to the content logical
        definition may occur.
        Type `bool`. """
        
        self.purpose = None
        """ Why this value set is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.compose = None
        """ Content logical definition of the value set (CLD).
        Type `ValueSetCompose` (represented as `dict` in JSON). """
        
        self.expansion = None
        """ Used when the value set is "expanded".
        Type `ValueSetExpansion` (represented as `dict` in JSON). """
        
        super(ValueSet, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSet, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("version", "version", fhirdatatypes.FHIRString, False, None, False),
            ("name", "name", fhirdatatypes.FHIRString, False, None, False),
            ("title", "title", fhirdatatypes.FHIRString, False, None, False),
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False),
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("immutable", "immutable", bool, False, None, False),
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("copyright", "copyright", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("compose", "compose", ValueSetCompose, False, None, False),
            ("expansion", "expansion", ValueSetExpansion, False, None, False),
        ])
        return js



from . import backboneelement

class ValueSetCompose(backboneelement.BackboneElement):
    """ Content logical definition of the value set (CLD).
    
    A set of criteria that define the contents of the value set by including or
    excluding codes selected from the specified code system(s) that the value
    set draws from. This is also known as the Content Logical Definition (CLD).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.lockedDate = None
        """ Fixed date for references with no specified version (transitive).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.inactive = None
        """ Whether inactive codes are in the value set.
        Type `bool`. """
        
        self.include = None
        """ Include one or more codes from a code system or other value set(s).
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """
        
        self.exclude = None
        """ Explicitly exclude codes from a code system or other value sets.
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """
        
        super(ValueSetCompose, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetCompose, self).elementProperties()
        js.extend([
            ("lockedDate", "lockedDate", fhirdatatypes.FHIRDate, False, None, False),
            ("inactive", "inactive", bool, False, None, False),
            ("include", "include", ValueSetComposeInclude, True, None, True),
            ("exclude", "exclude", ValueSetComposeInclude, True, None, False),
        ])
        return js




class ValueSetComposeInclude(backboneelement.BackboneElement):
    """ Include one or more codes from a code system or other value set(s).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.system = None
        """ The system the codes come from.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.version = None
        """ Specific version of the code system referred to.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.concept = None
        """ A concept defined in the system.
        List of `ValueSetComposeIncludeConcept` items (represented as `dict` in JSON). """
        
        self.filter = None
        """ Select codes/concepts by their properties (including relationships).
        List of `ValueSetComposeIncludeFilter` items (represented as `dict` in JSON). """
        
        self.valueSet = None
        """ Select the contents included in this value set.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        super(ValueSetComposeInclude, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetComposeInclude, self).elementProperties()
        js.extend([
            ("system", "system", fhirdatatypes.FHIRUri, False, None, False),
            ("version", "version", fhirdatatypes.FHIRString, False, None, False),
            ("concept", "concept", ValueSetComposeIncludeConcept, True, None, False),
            ("filter", "filter", ValueSetComposeIncludeFilter, True, None, False),
            ("valueSet", "valueSet", fhirdatatypes.FHIRCanonical, True, None, False),
        ])
        return js




class ValueSetComposeIncludeConcept(backboneelement.BackboneElement):
    """ A concept defined in the system.
    
    Specifies a concept to be included or excluded.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Code or expression from system.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.display = None
        """ Text to display for this code for this value set in this valueset.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.designation = None
        """ Additional representations for this concept.
        List of `ValueSetComposeIncludeConceptDesignation` items (represented as `dict` in JSON). """
        
        super(ValueSetComposeIncludeConcept, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetComposeIncludeConcept, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True),
            ("display", "display", fhirdatatypes.FHIRString, False, None, False),
            ("designation", "designation", ValueSetComposeIncludeConceptDesignation, True, None, False),
        ])
        return js




class ValueSetComposeIncludeConceptDesignation(backboneelement.BackboneElement):
    """ Additional representations for this concept.
    
    Additional representations for this concept when used in this value set -
    other languages, aliases, specialized purposes, used for particular
    purposes, etc.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        """ Human language of the designation.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.use = None
        """ Types of uses of designations.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ The text value for this designation.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(ValueSetComposeIncludeConceptDesignation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetComposeIncludeConceptDesignation, self).elementProperties()
        js.extend([
            ("language", "language", fhirdatatypes.FHIRCode, False, None, False),
            ("use", "use", coding.Coding, False, None, False),
            ("value", "value", fhirdatatypes.FHIRString, False, None, True),
        ])
        return js




class ValueSetComposeIncludeFilter(backboneelement.BackboneElement):
    """ Select codes/concepts by their properties (including relationships).
    
    Select concepts by specify a matching criterion based on the properties
    (including relationships) defined by the system, or on filters defined by
    the system. If multiple filters are specified, they SHALL all be true.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.property = None
        """ A property/filter defined by the code system.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.op = None
        """ = | is-a | descendent-of | is-not-a | regex | in | not-in |
        generalizes | exists.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.value = None
        """ Code from the system, or regex criteria, or boolean value for
        exists.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(ValueSetComposeIncludeFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetComposeIncludeFilter, self).elementProperties()
        js.extend([
            ("property", "property", fhirdatatypes.FHIRCode, False, None, True),
            ("op", "op", fhirdatatypes.FHIRCode, False, None, True),
            ("value", "value", fhirdatatypes.FHIRString, False, None, True),
        ])
        return js




class ValueSetExpansion(backboneelement.BackboneElement):
    """ Used when the value set is "expanded".
    
    A value set can also be "expanded", where the value set is turned into a
    simple collection of enumerated codes. This element holds the expansion, if
    it has been performed.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Identifies the value set expansion (business identifier).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.timestamp = None
        """ Time ValueSet expansion happened.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.total = None
        """ Total number of codes in the expansion.
        Type `int`. """
        
        self.offset = None
        """ Offset at which this resource starts.
        Type `int`. """
        
        self.parameter = None
        """ Parameter that controlled the expansion process.
        List of `ValueSetExpansionParameter` items (represented as `dict` in JSON). """
        
        self.contains = None
        """ Codes in the value set.
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """
        
        super(ValueSetExpansion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetExpansion, self).elementProperties()
        js.extend([
            ("identifier", "identifier", fhirdatatypes.FHIRUri, False, None, False),
            ("timestamp", "timestamp", fhirdatatypes.FHIRDateTime, False, None, True),
            ("total", "total", int, False, None, False),
            ("offset", "offset", int, False, None, False),
            ("parameter", "parameter", ValueSetExpansionParameter, True, None, False),
            ("contains", "contains", ValueSetExpansionContains, True, None, False),
        ])
        return js




class ValueSetExpansionContains(backboneelement.BackboneElement):
    """ Codes in the value set.
    
    The codes that are contained in the value set expansion.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.system = None
        """ System value for the code.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.abstract = None
        """ If user cannot select this entry.
        Type `bool`. """
        
        self.inactive = None
        """ If concept is inactive in the code system.
        Type `bool`. """
        
        self.version = None
        """ Version in which this code/display is defined.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.code = None
        """ Code - if blank, this is not a selectable code.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.display = None
        """ User display for the concept.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.designation = None
        """ Additional representations for this item.
        List of `ValueSetComposeIncludeConceptDesignation` items (represented as `dict` in JSON). """
        
        self.contains = None
        """ Codes contained under this entry.
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """
        
        super(ValueSetExpansionContains, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetExpansionContains, self).elementProperties()
        js.extend([
            ("system", "system", fhirdatatypes.FHIRUri, False, None, False),
            ("abstract", "abstract", bool, False, None, False),
            ("inactive", "inactive", bool, False, None, False),
            ("version", "version", fhirdatatypes.FHIRString, False, None, False),
            ("code", "code", fhirdatatypes.FHIRCode, False, None, False),
            ("display", "display", fhirdatatypes.FHIRString, False, None, False),
            ("designation", "designation", ValueSetComposeIncludeConceptDesignation, True, None, False),
            ("contains", "contains", ValueSetExpansionContains, True, None, False),
        ])
        return js




class ValueSetExpansionParameter(backboneelement.BackboneElement):
    """ Parameter that controlled the expansion process.
    
    A parameter that controlled the expansion process. These parameters may be
    used by users of expanded value sets to check whether the expansion is
    suitable for a particular purpose, or to pick the correct expansion.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name as assigned by the client or server.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueString = None
        """ Value of the named parameter.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueBoolean = None
        """ Value of the named parameter.
        Type `bool`. """
        
        self.valueInteger = None
        """ Value of the named parameter.
        Type `int`. """
        
        self.valueDecimal = None
        """ Value of the named parameter.
        Type `float`. """
        
        self.valueUri = None
        """ Value of the named parameter.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.valueCode = None
        """ Value of the named parameter.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ Value of the named parameter.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        super(ValueSetExpansionParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetExpansionParameter, self).elementProperties()
        js.extend([
            ("name", "name", fhirdatatypes.FHIRString, False, None, True),
            ("valueString", "valueString", fhirdatatypes.FHIRString, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("valueUri", "valueUri", fhirdatatypes.FHIRUri, False, "value", False),
            ("valueCode", "valueCode", fhirdatatypes.FHIRCode, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdatatypes.FHIRDateTime, False, "value", False),
        ])
        return js



import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']

try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']

try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']

try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']

try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']

