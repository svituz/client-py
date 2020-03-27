#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/TestScript)
#  2020, SMART Health IT.


from . import domainresource

class TestScript(domainresource.DomainResource):
    """ Describes a set of tests.
    
    A structured set of tests against a FHIR server or client implementation to
    determine compliance against the FHIR specification.
    """
    
    resource_type = "TestScript"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this test script, represented as a URI
        (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the test script.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the test script.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this test script (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this test script (human friendly).
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
        """ Natural language description of the test script.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for test script (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.purpose = None
        """ Why this test script is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.origin = None
        """ An abstract server representing a client or sender in a message
        exchange.
        List of `TestScriptOrigin` items (represented as `dict` in JSON). """
        
        self.destination = None
        """ An abstract server representing a destination or receiver in a
        message exchange.
        List of `TestScriptDestination` items (represented as `dict` in JSON). """
        
        self.metadata = None
        """ Required capability that is assumed to function correctly on the
        FHIR server being tested.
        Type `TestScriptMetadata` (represented as `dict` in JSON). """
        
        self.fixture = None
        """ Fixture in the test script - by reference (uri).
        List of `TestScriptFixture` items (represented as `dict` in JSON). """
        
        self.profile = None
        """ Reference of the validation profile.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.variable = None
        """ Placeholder for evaluated elements.
        List of `TestScriptVariable` items (represented as `dict` in JSON). """
        
        self.setup = None
        """ A series of required setup operations before tests are executed.
        Type `TestScriptSetup` (represented as `dict` in JSON). """
        
        self.test = None
        """ A test in this script.
        List of `TestScriptTest` items (represented as `dict` in JSON). """
        
        self.teardown = None
        """ A series of required clean up steps.
        Type `TestScriptTeardown` (represented as `dict` in JSON). """
        
        super(TestScript, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScript, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, True),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("version", "version", fhirdatatypes.FHIRString, False, None, False),
            ("name", "name", fhirdatatypes.FHIRString, False, None, True),
            ("title", "title", fhirdatatypes.FHIRString, False, None, False),
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False),
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("copyright", "copyright", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("origin", "origin", TestScriptOrigin, True, None, False),
            ("destination", "destination", TestScriptDestination, True, None, False),
            ("metadata", "metadata", TestScriptMetadata, False, None, False),
            ("fixture", "fixture", TestScriptFixture, True, None, False),
            ("profile", "profile", fhirreference.FHIRReference, True, None, False),
            ("variable", "variable", TestScriptVariable, True, None, False),
            ("setup", "setup", TestScriptSetup, False, None, False),
            ("test", "test", TestScriptTest, True, None, False),
            ("teardown", "teardown", TestScriptTeardown, False, None, False),
        ])
        return js



from . import backboneelement

class TestScriptDestination(backboneelement.BackboneElement):
    """ An abstract server representing a destination or receiver in a message
    exchange.
    
    An abstract server used in operations within this test script in the
    destination element.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.index = None
        """ The index of the abstract destination server starting at 1.
        Type `int`. """
        
        self.profile = None
        """ FHIR-Server | FHIR-SDC-FormManager | FHIR-SDC-FormReceiver | FHIR-
        SDC-FormProcessor.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(TestScriptDestination, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptDestination, self).elementProperties()
        js.extend([
            ("index", "index", int, False, None, True),
            ("profile", "profile", coding.Coding, False, None, True),
        ])
        return js




class TestScriptFixture(backboneelement.BackboneElement):
    """ Fixture in the test script - by reference (uri).
    
    Fixture in the test script - by reference (uri). All fixtures are required
    for the test script to execute.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.autocreate = None
        """ Whether or not to implicitly create the fixture during setup.
        Type `bool`. """
        
        self.autodelete = None
        """ Whether or not to implicitly delete the fixture during teardown.
        Type `bool`. """
        
        self.resource = None
        """ Reference of the resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(TestScriptFixture, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptFixture, self).elementProperties()
        js.extend([
            ("autocreate", "autocreate", bool, False, None, True),
            ("autodelete", "autodelete", bool, False, None, True),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
        ])
        return js




class TestScriptMetadata(backboneelement.BackboneElement):
    """ Required capability that is assumed to function correctly on the FHIR
    server being tested.
    
    The required capability must exist and are assumed to function correctly on
    the FHIR server being tested.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.link = None
        """ Links to the FHIR specification.
        List of `TestScriptMetadataLink` items (represented as `dict` in JSON). """
        
        self.capability = None
        """ Capabilities  that are assumed to function correctly on the FHIR
        server being tested.
        List of `TestScriptMetadataCapability` items (represented as `dict` in JSON). """
        
        super(TestScriptMetadata, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptMetadata, self).elementProperties()
        js.extend([
            ("link", "link", TestScriptMetadataLink, True, None, False),
            ("capability", "capability", TestScriptMetadataCapability, True, None, True),
        ])
        return js




class TestScriptMetadataCapability(backboneelement.BackboneElement):
    """ Capabilities  that are assumed to function correctly on the FHIR server
    being tested.
    
    Capabilities that must exist and are assumed to function correctly on the
    FHIR server being tested.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.required = None
        """ Are the capabilities required?.
        Type `bool`. """
        
        self.validated = None
        """ Are the capabilities validated?.
        Type `bool`. """
        
        self.description = None
        """ The expected capabilities of the server.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.origin = None
        """ Which origin server these requirements apply to.
        List of `int` items. """
        
        self.destination = None
        """ Which server these requirements apply to.
        Type `int`. """
        
        self.link = None
        """ Links to the FHIR specification.
        List of `FHIRUri` items (represented as `str` in JSON). """
        
        self.capabilities = None
        """ Required Capability Statement.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        super(TestScriptMetadataCapability, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptMetadataCapability, self).elementProperties()
        js.extend([
            ("required", "required", bool, False, None, True),
            ("validated", "validated", bool, False, None, True),
            ("description", "description", fhirdatatypes.FHIRString, False, None, False),
            ("origin", "origin", int, True, None, False),
            ("destination", "destination", int, False, None, False),
            ("link", "link", fhirdatatypes.FHIRUri, True, None, False),
            ("capabilities", "capabilities", fhirdatatypes.FHIRCanonical, False, None, True),
        ])
        return js




class TestScriptMetadataLink(backboneelement.BackboneElement):
    """ Links to the FHIR specification.
    
    A link to the FHIR specification that this test is covering.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ URL to the specification.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.description = None
        """ Short description.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(TestScriptMetadataLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptMetadataLink, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, True),
            ("description", "description", fhirdatatypes.FHIRString, False, None, False),
        ])
        return js




class TestScriptOrigin(backboneelement.BackboneElement):
    """ An abstract server representing a client or sender in a message exchange.
    
    An abstract server used in operations within this test script in the origin
    element.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.index = None
        """ The index of the abstract origin server starting at 1.
        Type `int`. """
        
        self.profile = None
        """ FHIR-Client | FHIR-SDC-FormFiller.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(TestScriptOrigin, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptOrigin, self).elementProperties()
        js.extend([
            ("index", "index", int, False, None, True),
            ("profile", "profile", coding.Coding, False, None, True),
        ])
        return js




class TestScriptSetup(backboneelement.BackboneElement):
    """ A series of required setup operations before tests are executed.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ A setup operation or assert to perform.
        List of `TestScriptSetupAction` items (represented as `dict` in JSON). """
        
        super(TestScriptSetup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetup, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptSetupAction, True, None, True),
        ])
        return js




class TestScriptSetupAction(backboneelement.BackboneElement):
    """ A setup operation or assert to perform.
    
    Action would contain either an operation or an assertion.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.operation = None
        """ The setup operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """
        
        self.assert_fhir = None
        """ The assertion to perform.
        Type `TestScriptSetupActionAssert` (represented as `dict` in JSON). """
        
        super(TestScriptSetupAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetupAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestScriptSetupActionOperation, False, None, False),
            ("assert_fhir", "assert", TestScriptSetupActionAssert, False, None, False),
        ])
        return js




class TestScriptSetupActionAssert(backboneelement.BackboneElement):
    """ The assertion to perform.
    
    Evaluates the results of previous operations to determine if the server
    under test behaves appropriately.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.label = None
        """ Tracking/logging assertion label.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ Tracking/reporting assertion description.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.direction = None
        """ response | request.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.compareToSourceId = None
        """ Id of the source fixture to be evaluated.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.compareToSourceExpression = None
        """ The FHIRPath expression to evaluate against the source fixture.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.compareToSourcePath = None
        """ XPath or JSONPath expression to evaluate against the source fixture.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.contentType = None
        """ Mime type to compare against the 'Content-Type' header.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.expression = None
        """ The FHIRPath expression to be evaluated.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.headerField = None
        """ HTTP header field name.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.minimumId = None
        """ Fixture Id of minimum content resource.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.navigationLinks = None
        """ Perform validation on navigation links?.
        Type `bool`. """
        
        self.operator = None
        """ equals | notEquals | in | notIn | greaterThan | lessThan | empty |
        notEmpty | contains | notContains | eval.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.path = None
        """ XPath or JSONPath expression.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.requestMethod = None
        """ delete | get | options | patch | post | put | head.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.requestURL = None
        """ Request URL comparison value.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.resource = None
        """ Resource type.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.response = None
        """ okay | created | noContent | notModified | bad | forbidden |
        notFound | methodNotAllowed | conflict | gone | preconditionFailed
        | unprocessable.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.responseCode = None
        """ HTTP response code to test.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.sourceId = None
        """ Fixture Id of source expression or headerField.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.validateProfileId = None
        """ Profile Id of validation profile reference.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.value = None
        """ The value to compare to.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.warningOnly = None
        """ Will this assert produce a warning only on error?.
        Type `bool`. """
        
        super(TestScriptSetupActionAssert, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetupActionAssert, self).elementProperties()
        js.extend([
            ("label", "label", fhirdatatypes.FHIRString, False, None, False),
            ("description", "description", fhirdatatypes.FHIRString, False, None, False),
            ("direction", "direction", fhirdatatypes.FHIRCode, False, None, False),
            ("compareToSourceId", "compareToSourceId", fhirdatatypes.FHIRString, False, None, False),
            ("compareToSourceExpression", "compareToSourceExpression", fhirdatatypes.FHIRString, False, None, False),
            ("compareToSourcePath", "compareToSourcePath", fhirdatatypes.FHIRString, False, None, False),
            ("contentType", "contentType", fhirdatatypes.FHIRCode, False, None, False),
            ("expression", "expression", fhirdatatypes.FHIRString, False, None, False),
            ("headerField", "headerField", fhirdatatypes.FHIRString, False, None, False),
            ("minimumId", "minimumId", fhirdatatypes.FHIRString, False, None, False),
            ("navigationLinks", "navigationLinks", bool, False, None, False),
            ("operator", "operator", fhirdatatypes.FHIRCode, False, None, False),
            ("path", "path", fhirdatatypes.FHIRString, False, None, False),
            ("requestMethod", "requestMethod", fhirdatatypes.FHIRCode, False, None, False),
            ("requestURL", "requestURL", fhirdatatypes.FHIRString, False, None, False),
            ("resource", "resource", fhirdatatypes.FHIRCode, False, None, False),
            ("response", "response", fhirdatatypes.FHIRCode, False, None, False),
            ("responseCode", "responseCode", fhirdatatypes.FHIRString, False, None, False),
            ("sourceId", "sourceId", fhirdatatypes.FHIRId, False, None, False),
            ("validateProfileId", "validateProfileId", fhirdatatypes.FHIRId, False, None, False),
            ("value", "value", fhirdatatypes.FHIRString, False, None, False),
            ("warningOnly", "warningOnly", bool, False, None, True),
        ])
        return js




class TestScriptSetupActionOperation(backboneelement.BackboneElement):
    """ The setup operation to perform.
    
    The operation to perform.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ The operation code type that will be executed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.resource = None
        """ Resource type.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.label = None
        """ Tracking/logging operation label.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ Tracking/reporting operation description.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.accept = None
        """ Mime type to accept in the payload of the response, with charset
        etc..
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.contentType = None
        """ Mime type of the request payload contents, with charset etc..
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.destination = None
        """ Server responding to the request.
        Type `int`. """
        
        self.encodeRequestUrl = None
        """ Whether or not to send the request url in encoded format.
        Type `bool`. """
        
        self.method = None
        """ delete | get | options | patch | post | put | head.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.origin = None
        """ Server initiating the request.
        Type `int`. """
        
        self.params = None
        """ Explicitly defined path parameters.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.requestHeader = None
        """ Each operation can have one or more header elements.
        List of `TestScriptSetupActionOperationRequestHeader` items (represented as `dict` in JSON). """
        
        self.requestId = None
        """ Fixture Id of mapped request.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.responseId = None
        """ Fixture Id of mapped response.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.sourceId = None
        """ Fixture Id of body for PUT and POST requests.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.targetId = None
        """ Id of fixture used for extracting the [id],  [type], and [vid] for
        GET requests.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.url = None
        """ Request URL.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(TestScriptSetupActionOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetupActionOperation, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, False, None, False),
            ("resource", "resource", fhirdatatypes.FHIRCode, False, None, False),
            ("label", "label", fhirdatatypes.FHIRString, False, None, False),
            ("description", "description", fhirdatatypes.FHIRString, False, None, False),
            ("accept", "accept", fhirdatatypes.FHIRCode, False, None, False),
            ("contentType", "contentType", fhirdatatypes.FHIRCode, False, None, False),
            ("destination", "destination", int, False, None, False),
            ("encodeRequestUrl", "encodeRequestUrl", bool, False, None, True),
            ("method", "method", fhirdatatypes.FHIRCode, False, None, False),
            ("origin", "origin", int, False, None, False),
            ("params", "params", fhirdatatypes.FHIRString, False, None, False),
            ("requestHeader", "requestHeader", TestScriptSetupActionOperationRequestHeader, True, None, False),
            ("requestId", "requestId", fhirdatatypes.FHIRId, False, None, False),
            ("responseId", "responseId", fhirdatatypes.FHIRId, False, None, False),
            ("sourceId", "sourceId", fhirdatatypes.FHIRId, False, None, False),
            ("targetId", "targetId", fhirdatatypes.FHIRId, False, None, False),
            ("url", "url", fhirdatatypes.FHIRString, False, None, False),
        ])
        return js




class TestScriptSetupActionOperationRequestHeader(backboneelement.BackboneElement):
    """ Each operation can have one or more header elements.
    
    Header elements would be used to set HTTP headers.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.field = None
        """ HTTP header field name.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.value = None
        """ HTTP headerfield value.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(TestScriptSetupActionOperationRequestHeader, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetupActionOperationRequestHeader, self).elementProperties()
        js.extend([
            ("field", "field", fhirdatatypes.FHIRString, False, None, True),
            ("value", "value", fhirdatatypes.FHIRString, False, None, True),
        ])
        return js




class TestScriptTeardown(backboneelement.BackboneElement):
    """ A series of required clean up steps.
    
    A series of operations required to clean up after all the tests are
    executed (successfully or otherwise).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ One or more teardown operations to perform.
        List of `TestScriptTeardownAction` items (represented as `dict` in JSON). """
        
        super(TestScriptTeardown, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptTeardown, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptTeardownAction, True, None, True),
        ])
        return js




class TestScriptTeardownAction(backboneelement.BackboneElement):
    """ One or more teardown operations to perform.
    
    The teardown action will only contain an operation.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.operation = None
        """ The teardown operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestScriptTeardownAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptTeardownAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestScriptSetupActionOperation, False, None, True),
        ])
        return js




class TestScriptTest(backboneelement.BackboneElement):
    """ A test in this script.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Tracking/logging name of this test.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ Tracking/reporting short description of the test.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.action = None
        """ A test operation or assert to perform.
        List of `TestScriptTestAction` items (represented as `dict` in JSON). """
        
        super(TestScriptTest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptTest, self).elementProperties()
        js.extend([
            ("name", "name", fhirdatatypes.FHIRString, False, None, False),
            ("description", "description", fhirdatatypes.FHIRString, False, None, False),
            ("action", "action", TestScriptTestAction, True, None, True),
        ])
        return js




class TestScriptTestAction(backboneelement.BackboneElement):
    """ A test operation or assert to perform.
    
    Action would contain either an operation or an assertion.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.operation = None
        """ The setup operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """
        
        self.assert_fhir = None
        """ The setup assertion to perform.
        Type `TestScriptSetupActionAssert` (represented as `dict` in JSON). """
        
        super(TestScriptTestAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptTestAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestScriptSetupActionOperation, False, None, False),
            ("assert_fhir", "assert", TestScriptSetupActionAssert, False, None, False),
        ])
        return js




class TestScriptVariable(backboneelement.BackboneElement):
    """ Placeholder for evaluated elements.
    
    Variable is set based either on element value in response body or on header
    field value in the response headers.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Descriptive name for this variable.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.defaultValue = None
        """ Default, hard-coded, or user-defined value for this variable.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the variable.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.expression = None
        """ The FHIRPath expression against the fixture body.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.headerField = None
        """ HTTP header field name for source.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.hint = None
        """ Hint help text for default value to enter.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.path = None
        """ XPath or JSONPath against the fixture body.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.sourceId = None
        """ Fixture Id of source expression or headerField within this variable.
        Type `FHIRId` (represented as `str` in JSON). """
        
        super(TestScriptVariable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptVariable, self).elementProperties()
        js.extend([
            ("name", "name", fhirdatatypes.FHIRString, False, None, True),
            ("defaultValue", "defaultValue", fhirdatatypes.FHIRString, False, None, False),
            ("description", "description", fhirdatatypes.FHIRString, False, None, False),
            ("expression", "expression", fhirdatatypes.FHIRString, False, None, False),
            ("headerField", "headerField", fhirdatatypes.FHIRString, False, None, False),
            ("hint", "hint", fhirdatatypes.FHIRString, False, None, False),
            ("path", "path", fhirdatatypes.FHIRString, False, None, False),
            ("sourceId", "sourceId", fhirdatatypes.FHIRId, False, None, False),
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
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']

try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']

