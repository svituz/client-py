#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DataRequirement)
#  2020, SMART Health IT.


from fhirclient.models import element

class DataRequirement(element.Element):
    """ Describes a required data item.
    
    Describes a required data item for evaluation in terms of the type of data,
    and optional code or date-based filters of the data.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ The type of the required data.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.profile = None
        """ The profile of the required data.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.subjectCodeableConcept = None
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.mustSupport = None
        """ Indicates specific structure elements that are referenced by the
        knowledge module.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.codeFilter = None
        """ What codes are expected.
        List of `DataRequirementCodeFilter` items (represented as `dict` in JSON). """
        
        self.dateFilter = None
        """ What dates/date ranges are expected.
        List of `DataRequirementDateFilter` items (represented as `dict` in JSON). """
        
        self.limit = None
        """ Number of results.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.sort = None
        """ Order of the results.
        List of `DataRequirementSort` items (represented as `dict` in JSON). """
        
        super(DataRequirement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirement, self).elementProperties()
        js.extend([
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, None), 
            ("profile", "profile", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False, None), 
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False, None), 
            ("mustSupport", "mustSupport", fhirdatatypes.FHIRString, True, None, False, None), 
            ("codeFilter", "codeFilter", DataRequirementCodeFilter, True, None, False, None), 
            ("dateFilter", "dateFilter", DataRequirementDateFilter, True, None, False, None), 
            ("limit", "limit", fhirdatatypes.FHIRPositiveInt, False, None, False, None), 
            ("sort", "sort", DataRequirementSort, True, None, False, None), 
        ])
        return js




class DataRequirementCodeFilter(element.Element):
    """ What codes are expected.
    
    Code filters specify additional constraints on the data, specifying the
    value set of interest for a particular element of the data. Each code
    filter defines an additional constraint on the data, i.e. code filters are
    AND'ed, not OR'ed.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.path = None
        """ A code-valued attribute to filter on.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.searchParam = None
        """ A coded (token) parameter to search on.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueSet = None
        """ Valueset for the filter.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.code = None
        """ What code is expected.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(DataRequirementCodeFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirementCodeFilter, self).elementProperties()
        js.extend([
            ("path", "path", fhirdatatypes.FHIRString, False, None, False, None), 
            ("searchParam", "searchParam", fhirdatatypes.FHIRString, False, None, False, None), 
            ("valueSet", "valueSet", fhirdatatypes.FHIRCanonical, False, None, False, None), 
            ("code", "code", coding.Coding, True, None, False, None), 
        ])
        return js




class DataRequirementDateFilter(element.Element):
    """ What dates/date ranges are expected.
    
    Date filters specify additional constraints on the data in terms of the
    applicable date range for specific elements. Each date filter specifies an
    additional constraint on the data, i.e. date filters are AND'ed, not OR'ed.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.path = None
        """ A date-valued attribute to filter on.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.searchParam = None
        """ A date valued parameter to search on.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ The value of the filter, as a Period, DateTime, or Duration value.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valuePeriod = None
        """ The value of the filter, as a Period, DateTime, or Duration value.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        """ The value of the filter, as a Period, DateTime, or Duration value.
        Type `Duration` (represented as `dict` in JSON). """
        
        super(DataRequirementDateFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirementDateFilter, self).elementProperties()
        js.extend([
            ("path", "path", fhirdatatypes.FHIRString, False, None, False, None), 
            ("searchParam", "searchParam", fhirdatatypes.FHIRString, False, None, False, None), 
            ("valueDateTime", "valueDateTime", fhirdatatypes.FHIRDateTime, False, "value", False, None), 
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False, None), 
            ("valueDuration", "valueDuration", duration.Duration, False, "value", False, None), 
        ])
        return js




class DataRequirementSort(element.Element):
    """ Order of the results.
    
    Specifies the order of the results to be returned.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.path = None
        """ The name of the attribute to perform the sort.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.direction = None
        """ ascending | descending.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(DataRequirementSort, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirementSort, self).elementProperties()
        js.extend([
            ("path", "path", fhirdatatypes.FHIRString, False, None, True, None), 
            ("direction", "direction", fhirdatatypes.FHIRCode, False, None, True, sortdirection.SortDirection), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import coding

from fhirclient.models import duration

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import period

from fhirclient.codesystems import sortdirection

