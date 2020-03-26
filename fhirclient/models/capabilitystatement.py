#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CapabilityStatement) on 2020-03-26.
#  2020, SMART Health IT.


from . import domainresource

class CapabilityStatement(domainresource.DomainResource):
    """ A statement of system capabilities.
    
    A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server for a particular version of FHIR that may be used as a
    statement of actual server functionality or a statement of required or
    desired server implementation.
    """
    
    resource_type = "CapabilityStatement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the capability statement.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.document = None
        """ Document definition.
        List of `CapabilityStatementDocument` items (represented as `dict` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.fhirVersion = None
        """ FHIR Version the system supports.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.format = None
        """ formats supported (xml | json | ttl | mime type).
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.implementation = None
        """ If this describes a specific instance.
        Type `CapabilityStatementImplementation` (represented as `dict` in JSON). """
        
        self.implementationGuide = None
        """ Implementation guides supported.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.imports = None
        """ Canonical URL of another capability statement this adds to.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.instantiates = None
        """ Canonical URL of another capability statement this implements.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for capability statement (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.kind = None
        """ instance | capability | requirements.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.messaging = None
        """ If messaging is supported.
        List of `CapabilityStatementMessaging` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name for this capability statement (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.patchFormat = None
        """ Patch formats supported.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.purpose = None
        """ Why this capability statement is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.rest = None
        """ If the endpoint is a RESTful one.
        List of `CapabilityStatementRest` items (represented as `dict` in JSON). """
        
        self.software = None
        """ Software that is covered by this capability statement.
        Type `CapabilityStatementSoftware` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this capability statement (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.url = None
        """ Canonical identifier for this capability statement, represented as
        a URI (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the capability statement.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(CapabilityStatement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatement, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, True),
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("document", "document", CapabilityStatementDocument, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("fhirVersion", "fhirVersion", fhirdatatypes.FHIRCode, False, None, True),
            ("format", "format", fhirdatatypes.FHIRCode, True, None, True),
            ("implementation", "implementation", CapabilityStatementImplementation, False, None, False),
            ("implementationGuide", "implementationGuide", fhirdatatypes.FHIRCanonical, True, None, False),
            ("imports", "imports", fhirdatatypes.FHIRCanonical, True, None, False),
            ("instantiates", "instantiates", fhirdatatypes.FHIRCanonical, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("kind", "kind", fhirdatatypes.FHIRCode, False, None, True),
            ("messaging", "messaging", CapabilityStatementMessaging, True, None, False),
            ("name", "name", fhirdatatypes.FHIRString, False, None, False),
            ("patchFormat", "patchFormat", fhirdatatypes.FHIRCode, True, None, False),
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False),
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("rest", "rest", CapabilityStatementRest, True, None, False),
            ("software", "software", CapabilityStatementSoftware, False, None, False),
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True),
            ("title", "title", fhirdatatypes.FHIRString, False, None, False),
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", fhirdatatypes.FHIRString, False, None, False),
        ])
        return js



from . import backboneelement

class CapabilityStatementDocument(backboneelement.BackboneElement):
    """ Document definition.
    
    A document definition.
    """
    
    resource_type = "CapabilityStatementDocument"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        """ Description of document support.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.mode = None
        """ producer | consumer.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.profile = None
        """ Constraint on the resources used in the document.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        super(CapabilityStatementDocument, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementDocument, self).elementProperties()
        js.extend([
            ("documentation", "documentation", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("mode", "mode", fhirdatatypes.FHIRCode, False, None, True),
            ("profile", "profile", fhirdatatypes.FHIRCanonical, False, None, True),
        ])
        return js




class CapabilityStatementImplementation(backboneelement.BackboneElement):
    """ If this describes a specific instance.
    
    Identifies a specific implementation instance that is described by the
    capability statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """
    
    resource_type = "CapabilityStatementImplementation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.custodian = None
        """ Organization that manages the data.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.description = None
        """ Describes this specific instance.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.url = None
        """ Base URL for the installation.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        super(CapabilityStatementImplementation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementImplementation, self).elementProperties()
        js.extend([
            ("custodian", "custodian", fhirreference.FHIRReference, False, None, False),
            ("description", "description", fhirdatatypes.FHIRString, False, None, True),
            ("url", "url", fhirdatatypes.FHIRUrl, False, None, False),
        ])
        return js




class CapabilityStatementMessaging(backboneelement.BackboneElement):
    """ If messaging is supported.
    
    A description of the messaging capabilities of the solution.
    """
    
    resource_type = "CapabilityStatementMessaging"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        """ Messaging interface behavior details.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.endpoint = None
        """ Where messages should be sent.
        List of `CapabilityStatementMessagingEndpoint` items (represented as `dict` in JSON). """
        
        self.reliableCache = None
        """ Reliable Message Cache Length (min).
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.supportedMessage = None
        """ Messages supported by this system.
        List of `CapabilityStatementMessagingSupportedMessage` items (represented as `dict` in JSON). """
        
        super(CapabilityStatementMessaging, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementMessaging, self).elementProperties()
        js.extend([
            ("documentation", "documentation", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("endpoint", "endpoint", CapabilityStatementMessagingEndpoint, True, None, False),
            ("reliableCache", "reliableCache", fhirdatatypes.FHIRUnsignedInt, False, None, False),
            ("supportedMessage", "supportedMessage", CapabilityStatementMessagingSupportedMessage, True, None, False),
        ])
        return js




class CapabilityStatementMessagingEndpoint(backboneelement.BackboneElement):
    """ Where messages should be sent.
    
    An endpoint (network accessible address) to which messages and/or replies
    are to be sent.
    """
    
    resource_type = "CapabilityStatementMessagingEndpoint"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ Network address or identifier of the end-point.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        self.protocol = None
        """ http | ftp | mllp +.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(CapabilityStatementMessagingEndpoint, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementMessagingEndpoint, self).elementProperties()
        js.extend([
            ("address", "address", fhirdatatypes.FHIRUrl, False, None, True),
            ("protocol", "protocol", coding.Coding, False, None, True),
        ])
        return js




class CapabilityStatementMessagingSupportedMessage(backboneelement.BackboneElement):
    """ Messages supported by this system.
    
    References to message definitions for messages this system can send or
    receive.
    """
    
    resource_type = "CapabilityStatementMessagingSupportedMessage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        """ Message supported by this system.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.mode = None
        """ sender | receiver.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(CapabilityStatementMessagingSupportedMessage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementMessagingSupportedMessage, self).elementProperties()
        js.extend([
            ("definition", "definition", fhirdatatypes.FHIRCanonical, False, None, True),
            ("mode", "mode", fhirdatatypes.FHIRCode, False, None, True),
        ])
        return js




class CapabilityStatementRest(backboneelement.BackboneElement):
    """ If the endpoint is a RESTful one.
    
    A definition of the restful capabilities of the solution, if any.
    """
    
    resource_type = "CapabilityStatementRest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.compartment = None
        """ Compartments served/used by system.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.documentation = None
        """ General description of implementation.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.interaction = None
        """ What operations are supported?.
        List of `CapabilityStatementRestInteraction` items (represented as `dict` in JSON). """
        
        self.mode = None
        """ client | server.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.operation = None
        """ Definition of a system level operation.
        List of `CapabilityStatementRestResourceOperation` items (represented as `dict` in JSON). """
        
        self.resource = None
        """ Resource served on the REST interface.
        List of `CapabilityStatementRestResource` items (represented as `dict` in JSON). """
        
        self.searchParam = None
        """ Search parameters for searching all resources.
        List of `CapabilityStatementRestResourceSearchParam` items (represented as `dict` in JSON). """
        
        self.security = None
        """ Information about security of implementation.
        Type `CapabilityStatementRestSecurity` (represented as `dict` in JSON). """
        
        super(CapabilityStatementRest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRest, self).elementProperties()
        js.extend([
            ("compartment", "compartment", fhirdatatypes.FHIRCanonical, True, None, False),
            ("documentation", "documentation", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("interaction", "interaction", CapabilityStatementRestInteraction, True, None, False),
            ("mode", "mode", fhirdatatypes.FHIRCode, False, None, True),
            ("operation", "operation", CapabilityStatementRestResourceOperation, True, None, False),
            ("resource", "resource", CapabilityStatementRestResource, True, None, False),
            ("searchParam", "searchParam", CapabilityStatementRestResourceSearchParam, True, None, False),
            ("security", "security", CapabilityStatementRestSecurity, False, None, False),
        ])
        return js




class CapabilityStatementRestInteraction(backboneelement.BackboneElement):
    """ What operations are supported?.
    
    A specification of restful operations supported by the system.
    """
    
    resource_type = "CapabilityStatementRestInteraction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ transaction | batch | search-system | history-system.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.documentation = None
        """ Anything special about operation behavior.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        super(CapabilityStatementRestInteraction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestInteraction, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True),
            ("documentation", "documentation", fhirdatatypes.FHIRMarkdown, False, None, False),
        ])
        return js




class CapabilityStatementRestResource(backboneelement.BackboneElement):
    """ Resource served on the REST interface.
    
    A specification of the restful capabilities of the solution for a specific
    resource type.
    """
    
    resource_type = "CapabilityStatementRestResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.conditionalCreate = None
        """ If allows/uses conditional create.
        Type `bool`. """
        
        self.conditionalDelete = None
        """ not-supported | single | multiple - how conditional delete is
        supported.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.conditionalRead = None
        """ not-supported | modified-since | not-match | full-support.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.conditionalUpdate = None
        """ If allows/uses conditional update.
        Type `bool`. """
        
        self.documentation = None
        """ Additional information about the use of the resource type.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.interaction = None
        """ What operations are supported?.
        List of `CapabilityStatementRestResourceInteraction` items (represented as `dict` in JSON). """
        
        self.operation = None
        """ Definition of a resource operation.
        List of `CapabilityStatementRestResourceOperation` items (represented as `dict` in JSON). """
        
        self.profile = None
        """ Base System profile for all uses of resource.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.readHistory = None
        """ Whether vRead can return past versions.
        Type `bool`. """
        
        self.referencePolicy = None
        """ literal | logical | resolves | enforced | local.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.searchInclude = None
        """ _include values supported by the server.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.searchParam = None
        """ Search parameters supported by implementation.
        List of `CapabilityStatementRestResourceSearchParam` items (represented as `dict` in JSON). """
        
        self.searchRevInclude = None
        """ _revinclude values supported by the server.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.supportedProfile = None
        """ Profiles for use cases supported.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.type = None
        """ A resource type that is supported.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.updateCreate = None
        """ If update can commit to a new identity.
        Type `bool`. """
        
        self.versioning = None
        """ no-version | versioned | versioned-update.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(CapabilityStatementRestResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestResource, self).elementProperties()
        js.extend([
            ("conditionalCreate", "conditionalCreate", bool, False, None, False),
            ("conditionalDelete", "conditionalDelete", fhirdatatypes.FHIRCode, False, None, False),
            ("conditionalRead", "conditionalRead", fhirdatatypes.FHIRCode, False, None, False),
            ("conditionalUpdate", "conditionalUpdate", bool, False, None, False),
            ("documentation", "documentation", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("interaction", "interaction", CapabilityStatementRestResourceInteraction, True, None, False),
            ("operation", "operation", CapabilityStatementRestResourceOperation, True, None, False),
            ("profile", "profile", fhirdatatypes.FHIRCanonical, False, None, False),
            ("readHistory", "readHistory", bool, False, None, False),
            ("referencePolicy", "referencePolicy", fhirdatatypes.FHIRCode, True, None, False),
            ("searchInclude", "searchInclude", fhirdatatypes.FHIRString, True, None, False),
            ("searchParam", "searchParam", CapabilityStatementRestResourceSearchParam, True, None, False),
            ("searchRevInclude", "searchRevInclude", fhirdatatypes.FHIRString, True, None, False),
            ("supportedProfile", "supportedProfile", fhirdatatypes.FHIRCanonical, True, None, False),
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True),
            ("updateCreate", "updateCreate", bool, False, None, False),
            ("versioning", "versioning", fhirdatatypes.FHIRCode, False, None, False),
        ])
        return js




class CapabilityStatementRestResourceInteraction(backboneelement.BackboneElement):
    """ What operations are supported?.
    
    Identifies a restful operation supported by the solution.
    """
    
    resource_type = "CapabilityStatementRestResourceInteraction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ read | vread | update | patch | delete | history-instance |
        history-type | create | search-type.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.documentation = None
        """ Anything special about operation behavior.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        super(CapabilityStatementRestResourceInteraction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestResourceInteraction, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True),
            ("documentation", "documentation", fhirdatatypes.FHIRMarkdown, False, None, False),
        ])
        return js




class CapabilityStatementRestResourceOperation(backboneelement.BackboneElement):
    """ Definition of a resource operation.
    
    Definition of an operation or a named query together with its parameters
    and their meaning and type. Consult the definition of the operation for
    details about how to invoke the operation, and the parameters.
    """
    
    resource_type = "CapabilityStatementRestResourceOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        """ The defined operation/query.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.documentation = None
        """ Specific details about operation behavior.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.name = None
        """ Name by which the operation/query is invoked.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(CapabilityStatementRestResourceOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestResourceOperation, self).elementProperties()
        js.extend([
            ("definition", "definition", fhirdatatypes.FHIRCanonical, False, None, True),
            ("documentation", "documentation", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("name", "name", fhirdatatypes.FHIRString, False, None, True),
        ])
        return js




class CapabilityStatementRestResourceSearchParam(backboneelement.BackboneElement):
    """ Search parameters supported by implementation.
    
    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """
    
    resource_type = "CapabilityStatementRestResourceSearchParam"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        """ Source of definition for parameter.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.documentation = None
        """ Server-specific usage.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.name = None
        """ Name of search parameter.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.type = None
        """ number | date | string | token | reference | composite | quantity |
        uri | special.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(CapabilityStatementRestResourceSearchParam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestResourceSearchParam, self).elementProperties()
        js.extend([
            ("definition", "definition", fhirdatatypes.FHIRCanonical, False, None, False),
            ("documentation", "documentation", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("name", "name", fhirdatatypes.FHIRString, False, None, True),
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True),
        ])
        return js




class CapabilityStatementRestSecurity(backboneelement.BackboneElement):
    """ Information about security of implementation.
    
    Information about security implementation from an interface perspective -
    what a client needs to know.
    """
    
    resource_type = "CapabilityStatementRestSecurity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cors = None
        """ Adds CORS Headers (http://enable-cors.org/).
        Type `bool`. """
        
        self.description = None
        """ General description of how security works.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.service = None
        """ OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(CapabilityStatementRestSecurity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestSecurity, self).elementProperties()
        js.extend([
            ("cors", "cors", bool, False, None, False),
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("service", "service", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js




class CapabilityStatementSoftware(backboneelement.BackboneElement):
    """ Software that is covered by this capability statement.
    
    Software that is covered by this capability statement.  It is used when the
    capability statement describes the capabilities of a particular software
    version, independent of an installation.
    """
    
    resource_type = "CapabilityStatementSoftware"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ A name the software is known by.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.releaseDate = None
        """ Date this version was released.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.version = None
        """ Version covered by this statement.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(CapabilityStatementSoftware, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementSoftware, self).elementProperties()
        js.extend([
            ("name", "name", fhirdatatypes.FHIRString, False, None, True),
            ("releaseDate", "releaseDate", fhirdatatypes.FHIRDateTime, False, None, False),
            ("version", "version", fhirdatatypes.FHIRString, False, None, False),
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
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']

try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']

