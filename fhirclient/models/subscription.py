#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Subscription)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Subscription(domainresource.DomainResource):
    """ Server push subscription criteria.
    
    The subscription resource is used to define a push-based subscription from
    a server to another system. Once a subscription is registered with the
    server, the server checks every resource that is created or updated, and if
    the resource matches the given criteria, it sends a message on the defined
    "channel" so that another system can take an appropriate action.
    """
    
    resource_type = "Subscription"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.status = None
        """ requested | active | error | off.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.contact = None
        """ Contact details for source (e.g. troubleshooting).
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.end = None
        """ When to automatically delete the subscription.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.reason = None
        """ Description of why this subscription was created.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.criteria = None
        """ Rule for server push.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.error = None
        """ Latest error note.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.channel = None
        """ The channel on which to report matches to the criteria.
        Type `SubscriptionChannel` (represented as `dict` in JSON). """
        
        super(Subscription, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Subscription, self).elementProperties()
        js.extend([
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, subscriptionstatus.SubscriptionStatus), 
            ("contact", "contact", contactpoint.ContactPoint, True, None, False, None), 
            ("end", "end", fhirdatatypes.FHIRInstant, False, None, False, None), 
            ("reason", "reason", fhirdatatypes.FHIRString, False, None, True, None), 
            ("criteria", "criteria", fhirdatatypes.FHIRString, False, None, True, None), 
            ("error", "error", fhirdatatypes.FHIRString, False, None, False, None), 
            ("channel", "channel", SubscriptionChannel, False, None, True, None), 
        ])
        return js



from fhirclient.models import backboneelement

class SubscriptionChannel(backboneelement.BackboneElement):
    """ The channel on which to report matches to the criteria.
    
    Details where to send notifications when resources are received that meet
    the criteria.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ rest-hook | websocket | email | sms | message.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.endpoint = None
        """ Where the channel points to.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        self.payload = None
        """ MIME type to send, or omit for no payload.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.header = None
        """ Usage depends on the channel type.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        super(SubscriptionChannel, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubscriptionChannel, self).elementProperties()
        js.extend([
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, subscriptionchanneltype.SubscriptionChannelType), 
            ("endpoint", "endpoint", fhirdatatypes.FHIRUrl, False, None, False, None), 
            ("payload", "payload", fhirdatatypes.FHIRCode, False, None, False, None), 
            ("header", "header", fhirdatatypes.FHIRString, True, None, False, None), 
        ])
        return js



from fhirclient.models import contactpoint

from fhirclient.models import fhirdatatypes

from fhirclient.codesystems import subscriptionchanneltype

from fhirclient.codesystems import subscriptionstatus

