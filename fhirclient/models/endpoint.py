#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Endpoint)
#  2020, SMART Health IT.


from . import domainresource

class Endpoint(domainresource.DomainResource):
    """ The technical details of an endpoint that can be used for electronic
    services.
    
    The technical details of an endpoint that can be used for electronic
    services, such as for web services providing XDS.b or a REST endpoint for
    another FHIR server. This may include any security context information.
    """
    
    resource_type = "Endpoint"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Identifies this endpoint across multiple systems.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | suspended | error | off | entered-in-error | test.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.connectionType = None
        """ Protocol/Profile/Standard to be used with this endpoint connection.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.name = None
        """ A name that this endpoint can be identified by.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.managingOrganization = None
        """ Organization that manages this endpoint (might not be the
        organization that exposes the endpoint).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact details for source (e.g. troubleshooting).
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.period = None
        """ Interval the endpoint is expected to be operational.
        Type `Period` (represented as `dict` in JSON). """
        
        self.payloadType = None
        """ The type of content that may be used at this endpoint (e.g. XDS
        Discharge summaries).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.payloadMimeType = None
        """ Mimetype to send. If not specified, the content could be anything
        (including no payload, if the connectionType defined this).
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.address = None
        """ The technical base address for connecting to this endpoint.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        self.header = None
        """ Usage depends on the channel type.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        super(Endpoint, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Endpoint, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True),
            ("connectionType", "connectionType", coding.Coding, False, None, True),
            ("name", "name", fhirdatatypes.FHIRString, False, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("payloadType", "payloadType", codeableconcept.CodeableConcept, True, None, True),
            ("payloadMimeType", "payloadMimeType", fhirdatatypes.FHIRCode, True, None, False),
            ("address", "address", fhirdatatypes.FHIRUrl, False, None, True),
            ("header", "header", fhirdatatypes.FHIRString, True, None, False),
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
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']

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
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']

