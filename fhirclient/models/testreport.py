#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/TestReport)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class TestReport(domainresource.DomainResource):
    """ Describes the results of a TestScript execution.
    
    A summary of information based on the results of executing a TestScript.
    """
    
    resource_type = "TestReport"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.name = None
        """ Informal name of the executed TestScript.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.status = None
        """ completed | in-progress | waiting | stopped | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.testScript = None
        """ Reference to the  version-specific TestScript that was executed to
        produce this TestReport.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.result = None
        """ pass | fail | pending.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.score = None
        """ The final score (percentage of tests passed) resulting from the
        execution of the TestScript.
        Type `float`. """
        
        self.tester = None
        """ Name of the tester producing this report (Organization or
        individual).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.issued = None
        """ When the TestScript was executed and this TestReport was generated.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.participant = None
        """ A participant in the test execution, either the execution engine, a
        client, or a server.
        List of `TestReportParticipant` items (represented as `dict` in JSON). """
        
        self.setup = None
        """ The results of the series of required setup operations before the
        tests were executed.
        Type `TestReportSetup` (represented as `dict` in JSON). """
        
        self.test = None
        """ A test executed from the test script.
        List of `TestReportTest` items (represented as `dict` in JSON). """
        
        self.teardown = None
        """ The results of running the series of required clean up steps.
        Type `TestReportTeardown` (represented as `dict` in JSON). """
        
        super(TestReport, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReport, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, testreportstatus.TestReportStatus), 
            ("testScript", "testScript", fhirreference.FHIRReference, False, None, True, None), 
            ("result", "result", fhirdatatypes.FHIRCode, False, None, True, testreportresult.TestReportResult), 
            ("score", "score", float, False, None, False, None), 
            ("tester", "tester", fhirdatatypes.FHIRString, False, None, False, None), 
            ("issued", "issued", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("participant", "participant", TestReportParticipant, True, None, False, None), 
            ("setup", "setup", TestReportSetup, False, None, False, None), 
            ("test", "test", TestReportTest, True, None, False, None), 
            ("teardown", "teardown", TestReportTeardown, False, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class TestReportParticipant(backboneelement.BackboneElement):
    """ A participant in the test execution, either the execution engine, a client,
    or a server.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ test-engine | client | server.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.uri = None
        """ The uri of the participant. An absolute URL is preferred.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.display = None
        """ The display name of the participant.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(TestReportParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportParticipant, self).elementProperties()
        js.extend([
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, testreportparticipanttype.TestReportParticipantType), 
            ("uri", "uri", fhirdatatypes.FHIRUri, False, None, True, None), 
            ("display", "display", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js




class TestReportSetup(backboneelement.BackboneElement):
    """ The results of the series of required setup operations before the tests
    were executed.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ A setup operation or assert that was executed.
        List of `TestReportSetupAction` items (represented as `dict` in JSON). """
        
        super(TestReportSetup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportSetup, self).elementProperties()
        js.extend([
            ("action", "action", TestReportSetupAction, True, None, True, None), 
        ])
        return js




class TestReportSetupAction(backboneelement.BackboneElement):
    """ A setup operation or assert that was executed.
    
    Action would contain either an operation or an assertion.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.operation = None
        """ The operation to perform.
        Type `TestReportSetupActionOperation` (represented as `dict` in JSON). """
        
        self.assert_fhir = None
        """ The assertion to perform.
        Type `TestReportSetupActionAssert` (represented as `dict` in JSON). """
        
        super(TestReportSetupAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportSetupAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestReportSetupActionOperation, False, None, False, None), 
            ("assert_fhir", "assert", TestReportSetupActionAssert, False, None, False, None), 
        ])
        return js




class TestReportSetupActionAssert(backboneelement.BackboneElement):
    """ The assertion to perform.
    
    The results of the assertion performed on the previous operations.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.result = None
        """ pass | skip | fail | warning | error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.message = None
        """ A message associated with the result.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.detail = None
        """ A link to further details on the result.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(TestReportSetupActionAssert, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportSetupActionAssert, self).elementProperties()
        js.extend([
            ("result", "result", fhirdatatypes.FHIRCode, False, None, True, testreportactionresult.TestReportActionResult), 
            ("message", "message", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("detail", "detail", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js




class TestReportSetupActionOperation(backboneelement.BackboneElement):
    """ The operation to perform.
    
    The operation performed.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.result = None
        """ pass | skip | fail | warning | error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.message = None
        """ A message associated with the result.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.detail = None
        """ A link to further details on the result.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        super(TestReportSetupActionOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportSetupActionOperation, self).elementProperties()
        js.extend([
            ("result", "result", fhirdatatypes.FHIRCode, False, None, True, testreportactionresult.TestReportActionResult), 
            ("message", "message", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("detail", "detail", fhirdatatypes.FHIRUri, False, None, False, None), 
        ])
        return js




class TestReportTeardown(backboneelement.BackboneElement):
    """ The results of running the series of required clean up steps.
    
    The results of the series of operations required to clean up after all the
    tests were executed (successfully or otherwise).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ One or more teardown operations performed.
        List of `TestReportTeardownAction` items (represented as `dict` in JSON). """
        
        super(TestReportTeardown, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportTeardown, self).elementProperties()
        js.extend([
            ("action", "action", TestReportTeardownAction, True, None, True, None), 
        ])
        return js




class TestReportTeardownAction(backboneelement.BackboneElement):
    """ One or more teardown operations performed.
    
    The teardown action will only contain an operation.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.operation = None
        """ The teardown operation performed.
        Type `TestReportSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestReportTeardownAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportTeardownAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestReportSetupActionOperation, False, None, True, None), 
        ])
        return js




class TestReportTest(backboneelement.BackboneElement):
    """ A test executed from the test script.
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
        """ A test operation or assert that was performed.
        List of `TestReportTestAction` items (represented as `dict` in JSON). """
        
        super(TestReportTest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportTest, self).elementProperties()
        js.extend([
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("action", "action", TestReportTestAction, True, None, True, None), 
        ])
        return js




class TestReportTestAction(backboneelement.BackboneElement):
    """ A test operation or assert that was performed.
    
    Action would contain either an operation or an assertion.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.operation = None
        """ The operation performed.
        Type `TestReportSetupActionOperation` (represented as `dict` in JSON). """
        
        self.assert_fhir = None
        """ The assertion performed.
        Type `TestReportSetupActionAssert` (represented as `dict` in JSON). """
        
        super(TestReportTestAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportTestAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestReportSetupActionOperation, False, None, False, None), 
            ("assert_fhir", "assert", TestReportSetupActionAssert, False, None, False, None), 
        ])
        return js



from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import testreportactionresult

from fhirclient.codesystems import testreportparticipanttype

from fhirclient.codesystems import testreportresult

from fhirclient.codesystems import testreportstatus

