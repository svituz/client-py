#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Timing)
#  2020, SMART Health IT.


from fhirclient.models import backboneelement

class Timing(backboneelement.BackboneElement):
    """ A timing schedule that specifies an event that may occur multiple times.
    
    Specifies an event that may occur multiple times. Timing schedules are used
    to record when things are planned, expected or requested to occur. The most
    common usage is in dosage instructions for medications. They are also used
    when planning care of various kinds, and may be used for reporting the
    schedule to which past regular activities were carried out.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.event = None
        """ When the event occurs.
        List of `FHIRDateTime` items (represented as `str` in JSON). """
        
        self.repeat = None
        """ When the event is to occur.
        Type `TimingRepeat` (represented as `dict` in JSON). """
        
        self.code = None
        """ BID | TID | QID | AM | PM | QD | QOD | +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Timing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Timing, self).elementProperties()
        js.extend([
            ("event", "event", fhirdatatypes.FHIRDateTime, True, None, False, None), 
            ("repeat", "repeat", TimingRepeat, False, None, False, None), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
        ])
        return js



from fhirclient.models import element

class TimingRepeat(element.Element):
    """ When the event is to occur.
    
    A set of rules that describe when the event is scheduled.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.boundsDuration = None
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.boundsRange = None
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Range` (represented as `dict` in JSON). """
        
        self.boundsPeriod = None
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Period` (represented as `dict` in JSON). """
        
        self.count = None
        """ Number of times to repeat.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.countMax = None
        """ Maximum number of times to repeat.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.duration = None
        """ How long when it happens.
        Type `float`. """
        
        self.durationMax = None
        """ How long when it happens (Max).
        Type `float`. """
        
        self.durationUnit = None
        """ s | min | h | d | wk | mo | a - unit of time (UCUM).
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.frequency = None
        """ Event occurs frequency times per period.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.frequencyMax = None
        """ Event occurs up to frequencyMax times per period.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.period = None
        """ Event occurs frequency times per period.
        Type `float`. """
        
        self.periodMax = None
        """ Upper limit of period (3-4 hours).
        Type `float`. """
        
        self.periodUnit = None
        """ s | min | h | d | wk | mo | a - unit of time (UCUM).
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.dayOfWeek = None
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.timeOfDay = None
        """ Time of day for action.
        List of `FHIRTime` items (represented as `str` in JSON). """
        
        self.when = None
        """ Code for time period of occurrence.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.offset = None
        """ Minutes from event (before or after).
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        super(TimingRepeat, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TimingRepeat, self).elementProperties()
        js.extend([
            ("boundsDuration", "boundsDuration", duration.Duration, False, "bounds", False, None), 
            ("boundsRange", "boundsRange", range.Range, False, "bounds", False, None), 
            ("boundsPeriod", "boundsPeriod", period.Period, False, "bounds", False, None), 
            ("count", "count", fhirdatatypes.FHIRPositiveInt, False, None, False, None), 
            ("countMax", "countMax", fhirdatatypes.FHIRPositiveInt, False, None, False, None), 
            ("duration", "duration", float, False, None, False, None), 
            ("durationMax", "durationMax", float, False, None, False, None), 
            ("durationUnit", "durationUnit", fhirdatatypes.FHIRCode, False, None, False, None), 
            ("frequency", "frequency", fhirdatatypes.FHIRPositiveInt, False, None, False, None), 
            ("frequencyMax", "frequencyMax", fhirdatatypes.FHIRPositiveInt, False, None, False, None), 
            ("period", "period", float, False, None, False, None), 
            ("periodMax", "periodMax", float, False, None, False, None), 
            ("periodUnit", "periodUnit", fhirdatatypes.FHIRCode, False, None, False, None), 
            ("dayOfWeek", "dayOfWeek", fhirdatatypes.FHIRCode, True, None, False, daysofweek.DaysOfWeek), 
            ("timeOfDay", "timeOfDay", fhirdatatypes.FHIRTime, True, None, False, None), 
            ("when", "when", fhirdatatypes.FHIRCode, True, None, False, None), 
            ("offset", "offset", fhirdatatypes.FHIRUnsignedInt, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.codesystems import daysofweek

from fhirclient.models import duration

from fhirclient.models import fhirdatatypes

from fhirclient.models import period

from fhirclient.models import range

