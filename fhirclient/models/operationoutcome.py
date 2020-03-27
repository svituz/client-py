#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/OperationOutcome)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class OperationOutcome(domainresource.DomainResource):
    """ Information about the success/failure of an action.
    
    A collection of error, warning, or information messages that result from a
    system action.
    """
    
    resource_type = "OperationOutcome"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.issue = None
        """ A single issue associated with the action.
        List of `OperationOutcomeIssue` items (represented as `dict` in JSON). """
        
        super(OperationOutcome, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationOutcome, self).elementProperties()
        js.extend([
            ("issue", "issue", OperationOutcomeIssue, True, None, True, None), 
        ])
        return js



from fhirclient.models import backboneelement

class OperationOutcomeIssue(backboneelement.BackboneElement):
    """ A single issue associated with the action.
    
    An error, warning, or information message that results from a system
    action.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.severity = None
        """ fatal | error | warning | information.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.code = None
        """ Error or warning code.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.details = None
        """ Additional details about the error.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.diagnostics = None
        """ Additional diagnostic information about the issue.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.location = None
        """ Deprecated: Path of element(s) related to issue.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.expression = None
        """ FHIRPath of element(s) related to issue.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        super(OperationOutcomeIssue, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationOutcomeIssue, self).elementProperties()
        js.extend([
            ("severity", "severity", fhirdatatypes.FHIRCode, False, None, True, issueseverity.IssueSeverity), 
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True, issuetype.IssueType), 
            ("details", "details", codeableconcept.CodeableConcept, False, None, False, None), 
            ("diagnostics", "diagnostics", fhirdatatypes.FHIRString, False, None, False, None), 
            ("location", "location", fhirdatatypes.FHIRString, True, None, False, None), 
            ("expression", "expression", fhirdatatypes.FHIRString, True, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.codesystems import issueseverity

from fhirclient.codesystems import issuetype

