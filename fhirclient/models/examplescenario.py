#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ExampleScenario)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class ExampleScenario(domainresource.DomainResource):
    """ Example of workflow instance.
    """
    
    resource_type = "ExampleScenario"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this example scenario, represented as a
        URI (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the example scenario.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the example scenario.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this example scenario (computer friendly).
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
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for example scenario (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.purpose = None
        """ The purpose of the example, e.g. to illustrate a scenario.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.actor = None
        """ Actor participating in the resource.
        List of `ExampleScenarioActor` items (represented as `dict` in JSON). """
        
        self.instance = None
        """ Each resource and each version that is present in the workflow.
        List of `ExampleScenarioInstance` items (represented as `dict` in JSON). """
        
        self.process = None
        """ Each major process - a group of operations.
        List of `ExampleScenarioProcess` items (represented as `dict` in JSON). """
        
        self.workflow = None
        """ Another nested workflow.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        super(ExampleScenario, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenario, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, publicationstatus.PublicationStatus), 
            ("experimental", "experimental", bool, False, None, False, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False, None), 
            ("contact", "contact", contactdetail.ContactDetail, True, None, False, None), 
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False, None), 
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False, None), 
            ("copyright", "copyright", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("actor", "actor", ExampleScenarioActor, True, None, False, None), 
            ("instance", "instance", ExampleScenarioInstance, True, None, False, None), 
            ("process", "process", ExampleScenarioProcess, True, None, False, None), 
            ("workflow", "workflow", fhirdatatypes.FHIRCanonical, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class ExampleScenarioActor(backboneelement.BackboneElement):
    """ Actor participating in the resource.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actorId = None
        """ ID or acronym of the actor.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.type = None
        """ person | entity.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.name = None
        """ The name of the actor as shown in the page.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ The description of the actor.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        super(ExampleScenarioActor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioActor, self).elementProperties()
        js.extend([
            ("actorId", "actorId", fhirdatatypes.FHIRString, False, None, True, None), 
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, examplescenarioactortype.ExampleScenarioActorType), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
        ])
        return js




class ExampleScenarioInstance(backboneelement.BackboneElement):
    """ Each resource and each version that is present in the workflow.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.resourceId = None
        """ The id of the resource for referencing.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.resourceType = None
        """ The type of the resource.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.name = None
        """ A short name for the resource instance.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ Human-friendly description of the resource instance.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.version = None
        """ A specific version of the resource.
        List of `ExampleScenarioInstanceVersion` items (represented as `dict` in JSON). """
        
        self.containedInstance = None
        """ Resources contained in the instance.
        List of `ExampleScenarioInstanceContainedInstance` items (represented as `dict` in JSON). """
        
        super(ExampleScenarioInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioInstance, self).elementProperties()
        js.extend([
            ("resourceId", "resourceId", fhirdatatypes.FHIRString, False, None, True, None), 
            ("resourceType", "resourceType", fhirdatatypes.FHIRCode, False, None, True, resourcetype.ResourceType), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("version", "version", ExampleScenarioInstanceVersion, True, None, False, None), 
            ("containedInstance", "containedInstance", ExampleScenarioInstanceContainedInstance, True, None, False, None), 
        ])
        return js




class ExampleScenarioInstanceContainedInstance(backboneelement.BackboneElement):
    """ Resources contained in the instance.
    
    Resources contained in the instance (e.g. the observations contained in a
    bundle).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.resourceId = None
        """ Each resource contained in the instance.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.versionId = None
        """ A specific version of a resource contained in the instance.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(ExampleScenarioInstanceContainedInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioInstanceContainedInstance, self).elementProperties()
        js.extend([
            ("resourceId", "resourceId", fhirdatatypes.FHIRString, False, None, True, None), 
            ("versionId", "versionId", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js




class ExampleScenarioInstanceVersion(backboneelement.BackboneElement):
    """ A specific version of the resource.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.versionId = None
        """ The identifier of a specific version of a resource.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ The description of the resource version.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        super(ExampleScenarioInstanceVersion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioInstanceVersion, self).elementProperties()
        js.extend([
            ("versionId", "versionId", fhirdatatypes.FHIRString, False, None, True, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, True, None), 
        ])
        return js




class ExampleScenarioProcess(backboneelement.BackboneElement):
    """ Each major process - a group of operations.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.title = None
        """ The diagram title of the group of operations.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ A longer description of the group of operations.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.preConditions = None
        """ Description of initial status before the process starts.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.postConditions = None
        """ Description of final status after the process ends.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.step = None
        """ Each step of the process.
        List of `ExampleScenarioProcessStep` items (represented as `dict` in JSON). """
        
        super(ExampleScenarioProcess, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioProcess, self).elementProperties()
        js.extend([
            ("title", "title", fhirdatatypes.FHIRString, False, None, True, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("preConditions", "preConditions", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("postConditions", "postConditions", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("step", "step", ExampleScenarioProcessStep, True, None, False, None), 
        ])
        return js




class ExampleScenarioProcessStep(backboneelement.BackboneElement):
    """ Each step of the process.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.process = None
        """ Nested process.
        List of `ExampleScenarioProcess` items (represented as `dict` in JSON). """
        
        self.pause = None
        """ If there is a pause in the flow.
        Type `bool`. """
        
        self.operation = None
        """ Each interaction or action.
        Type `ExampleScenarioProcessStepOperation` (represented as `dict` in JSON). """
        
        self.alternative = None
        """ Alternate non-typical step action.
        List of `ExampleScenarioProcessStepAlternative` items (represented as `dict` in JSON). """
        
        super(ExampleScenarioProcessStep, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioProcessStep, self).elementProperties()
        js.extend([
            ("process", "process", ExampleScenarioProcess, True, None, False, None), 
            ("pause", "pause", bool, False, None, False, None), 
            ("operation", "operation", ExampleScenarioProcessStepOperation, False, None, False, None), 
            ("alternative", "alternative", ExampleScenarioProcessStepAlternative, True, None, False, None), 
        ])
        return js




class ExampleScenarioProcessStepAlternative(backboneelement.BackboneElement):
    """ Alternate non-typical step action.
    
    Indicates an alternative step that can be taken instead of the operations
    on the base step in exceptional/atypical circumstances.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.title = None
        """ Label for alternative.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ A human-readable description of each option.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.step = None
        """ What happens in each alternative option.
        List of `ExampleScenarioProcessStep` items (represented as `dict` in JSON). """
        
        super(ExampleScenarioProcessStepAlternative, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioProcessStepAlternative, self).elementProperties()
        js.extend([
            ("title", "title", fhirdatatypes.FHIRString, False, None, True, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("step", "step", ExampleScenarioProcessStep, True, None, False, None), 
        ])
        return js




class ExampleScenarioProcessStepOperation(backboneelement.BackboneElement):
    """ Each interaction or action.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.number = None
        """ The sequential number of the interaction.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.type = None
        """ The type of operation - CRUD.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ The human-friendly name of the interaction.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.initiator = None
        """ Who starts the transaction.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.receiver = None
        """ Who receives the transaction.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ A comment to be inserted in the diagram.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.initiatorActive = None
        """ Whether the initiator is deactivated right after the transaction.
        Type `bool`. """
        
        self.receiverActive = None
        """ Whether the receiver is deactivated right after the transaction.
        Type `bool`. """
        
        self.request = None
        """ Each resource instance used by the initiator.
        Type `ExampleScenarioInstanceContainedInstance` (represented as `dict` in JSON). """
        
        self.response = None
        """ Each resource instance used by the responder.
        Type `ExampleScenarioInstanceContainedInstance` (represented as `dict` in JSON). """
        
        super(ExampleScenarioProcessStepOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioProcessStepOperation, self).elementProperties()
        js.extend([
            ("number", "number", fhirdatatypes.FHIRString, False, None, True, None), 
            ("type", "type", fhirdatatypes.FHIRString, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("initiator", "initiator", fhirdatatypes.FHIRString, False, None, False, None), 
            ("receiver", "receiver", fhirdatatypes.FHIRString, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("initiatorActive", "initiatorActive", bool, False, None, False, None), 
            ("receiverActive", "receiverActive", bool, False, None, False, None), 
            ("request", "request", ExampleScenarioInstanceContainedInstance, False, None, False, None), 
            ("response", "response", ExampleScenarioInstanceContainedInstance, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import contactdetail

from fhirclient.codesystems import examplescenarioactortype

from fhirclient.models import fhirdatatypes

from fhirclient.models import identifier

from fhirclient.codesystems import publicationstatus

from fhirclient.codesystems import resourcetype

from fhirclient.models import usagecontext

