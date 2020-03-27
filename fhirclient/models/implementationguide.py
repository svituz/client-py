#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ImplementationGuide)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class ImplementationGuide(domainresource.DomainResource):
    """ A set of rules about how FHIR is used.
    
    A set of rules of how a particular interoperability or standards problem is
    solved - typically through the use of FHIR resources. This resource is used
    to gather all the parts of an implementation guide into a logical whole and
    to publish a computable definition of all the parts.
    """
    
    resource_type = "ImplementationGuide"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this implementation guide, represented as
        a URI (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.version = None
        """ Business version of the implementation guide.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this implementation guide (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this implementation guide (human friendly).
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
        """ Natural language description of the implementation guide.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for implementation guide (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.packageId = None
        """ NPM Package name for IG.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.license = None
        """ SPDX license code for this IG (or not-open-source).
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.fhirVersion = None
        """ FHIR Version(s) this Implementation Guide targets.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.dependsOn = None
        """ Another Implementation guide this depends on.
        List of `ImplementationGuideDependsOn` items (represented as `dict` in JSON). """
        
        self.global_fhir = None
        """ Profiles that apply globally.
        List of `ImplementationGuideGlobal` items (represented as `dict` in JSON). """
        
        self.definition = None
        """ Information needed to build the IG.
        Type `ImplementationGuideDefinition` (represented as `dict` in JSON). """
        
        self.manifest = None
        """ Information about an assembled IG.
        Type `ImplementationGuideManifest` (represented as `dict` in JSON). """
        
        super(ImplementationGuide, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuide, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, True, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, True, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, publicationstatus.PublicationStatus), 
            ("experimental", "experimental", bool, False, None, False, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False, None), 
            ("contact", "contact", contactdetail.ContactDetail, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False, None), 
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False, None), 
            ("copyright", "copyright", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("packageId", "packageId", fhirdatatypes.FHIRId, False, None, True, None), 
            ("license", "license", fhirdatatypes.FHIRCode, False, None, False, None), 
            ("fhirVersion", "fhirVersion", fhirdatatypes.FHIRCode, True, None, True, None), 
            ("dependsOn", "dependsOn", ImplementationGuideDependsOn, True, None, False, None), 
            ("global_fhir", "global", ImplementationGuideGlobal, True, None, False, None), 
            ("definition", "definition", ImplementationGuideDefinition, False, None, False, None), 
            ("manifest", "manifest", ImplementationGuideManifest, False, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class ImplementationGuideDefinition(backboneelement.BackboneElement):
    """ Information needed to build the IG.
    
    The information needed by an IG publisher tool to publish the whole
    implementation guide.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.grouping = None
        """ Grouping used to present related resources in the IG.
        List of `ImplementationGuideDefinitionGrouping` items (represented as `dict` in JSON). """
        
        self.resource = None
        """ Resource in the implementation guide.
        List of `ImplementationGuideDefinitionResource` items (represented as `dict` in JSON). """
        
        self.page = None
        """ Page/Section in the Guide.
        Type `ImplementationGuideDefinitionPage` (represented as `dict` in JSON). """
        
        self.parameter = None
        """ Defines how IG is built by tools.
        List of `ImplementationGuideDefinitionParameter` items (represented as `dict` in JSON). """
        
        self.template = None
        """ A template for building resources.
        List of `ImplementationGuideDefinitionTemplate` items (represented as `dict` in JSON). """
        
        super(ImplementationGuideDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinition, self).elementProperties()
        js.extend([
            ("grouping", "grouping", ImplementationGuideDefinitionGrouping, True, None, False, None), 
            ("resource", "resource", ImplementationGuideDefinitionResource, True, None, True, None), 
            ("page", "page", ImplementationGuideDefinitionPage, False, None, False, None), 
            ("parameter", "parameter", ImplementationGuideDefinitionParameter, True, None, False, None), 
            ("template", "template", ImplementationGuideDefinitionTemplate, True, None, False, None), 
        ])
        return js




class ImplementationGuideDefinitionGrouping(backboneelement.BackboneElement):
    """ Grouping used to present related resources in the IG.
    
    A logical group of resources. Logical groups can be used when building
    pages.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Descriptive name for the package.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ Human readable text describing the package.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(ImplementationGuideDefinitionGrouping, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinitionGrouping, self).elementProperties()
        js.extend([
            ("name", "name", fhirdatatypes.FHIRString, False, None, True, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js




class ImplementationGuideDefinitionPage(backboneelement.BackboneElement):
    """ Page/Section in the Guide.
    
    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.nameUrl = None
        """ Where to find that page.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        self.nameReference = None
        """ Where to find that page.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.title = None
        """ Short title shown for navigational assistance.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.generation = None
        """ html | markdown | xml | generated.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.page = None
        """ Nested Pages / Sections.
        List of `ImplementationGuideDefinitionPage` items (represented as `dict` in JSON). """
        
        super(ImplementationGuideDefinitionPage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinitionPage, self).elementProperties()
        js.extend([
            ("nameUrl", "nameUrl", fhirdatatypes.FHIRUrl, False, "name", True, None), 
            ("nameReference", "nameReference", fhirreference.FHIRReference, False, "name", True, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, True, None), 
            ("generation", "generation", fhirdatatypes.FHIRCode, False, None, True, guidepagegeneration.GuidePageGeneration), 
            ("page", "page", ImplementationGuideDefinitionPage, True, None, False, None), 
        ])
        return js




class ImplementationGuideDefinitionParameter(backboneelement.BackboneElement):
    """ Defines how IG is built by tools.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ apply | path-resource | path-pages | path-tx-cache | expansion-
        parameter | rule-broken-links | generate-xml | generate-json |
        generate-turtle | html-template.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.value = None
        """ Value for named type.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(ImplementationGuideDefinitionParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinitionParameter, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True, guideparametercode.GuideParameterCode), 
            ("value", "value", fhirdatatypes.FHIRString, False, None, True, None), 
        ])
        return js




class ImplementationGuideDefinitionResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.
    
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ Location of the resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.fhirVersion = None
        """ Versions this applies to (if different to IG).
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.name = None
        """ Human Name for the resource.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ Reason why included in guide.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.exampleBoolean = None
        """ Is an example/What is this an example of?.
        Type `bool`. """
        
        self.exampleCanonical = None
        """ Is an example/What is this an example of?.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.groupingId = None
        """ Grouping this is part of.
        Type `FHIRId` (represented as `str` in JSON). """
        
        super(ImplementationGuideDefinitionResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinitionResource, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, False, None, True, None), 
            ("fhirVersion", "fhirVersion", fhirdatatypes.FHIRCode, True, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("exampleBoolean", "exampleBoolean", bool, False, "example", False, None), 
            ("exampleCanonical", "exampleCanonical", fhirdatatypes.FHIRCanonical, False, "example", False, None), 
            ("groupingId", "groupingId", fhirdatatypes.FHIRId, False, None, False, None), 
        ])
        return js




class ImplementationGuideDefinitionTemplate(backboneelement.BackboneElement):
    """ A template for building resources.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Type of template specified.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.source = None
        """ The source location for the template.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.scope = None
        """ The scope in which the template applies.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(ImplementationGuideDefinitionTemplate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinitionTemplate, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True, None), 
            ("source", "source", fhirdatatypes.FHIRString, False, None, True, None), 
            ("scope", "scope", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js




class ImplementationGuideDependsOn(backboneelement.BackboneElement):
    """ Another Implementation guide this depends on.
    
    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.uri = None
        """ Identity of the IG that this depends on.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.packageId = None
        """ NPM Package name for IG this depends on.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.version = None
        """ Version of the IG.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(ImplementationGuideDependsOn, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDependsOn, self).elementProperties()
        js.extend([
            ("uri", "uri", fhirdatatypes.FHIRCanonical, False, None, True, None), 
            ("packageId", "packageId", fhirdatatypes.FHIRId, False, None, False, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js




class ImplementationGuideGlobal(backboneelement.BackboneElement):
    """ Profiles that apply globally.
    
    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Type this profile applies to.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.profile = None
        """ Profile that all resources must conform to.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        super(ImplementationGuideGlobal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideGlobal, self).elementProperties()
        js.extend([
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, resourcetype.ResourceType), 
            ("profile", "profile", fhirdatatypes.FHIRCanonical, False, None, True, None), 
        ])
        return js




class ImplementationGuideManifest(backboneelement.BackboneElement):
    """ Information about an assembled IG.
    
    Information about an assembled implementation guide, created by the
    publication tooling.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.rendering = None
        """ Location of rendered implementation guide.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        self.resource = None
        """ Resource in the implementation guide.
        List of `ImplementationGuideManifestResource` items (represented as `dict` in JSON). """
        
        self.page = None
        """ HTML page within the parent IG.
        List of `ImplementationGuideManifestPage` items (represented as `dict` in JSON). """
        
        self.image = None
        """ Image within the IG.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.other = None
        """ Additional linkable file in IG.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        super(ImplementationGuideManifest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideManifest, self).elementProperties()
        js.extend([
            ("rendering", "rendering", fhirdatatypes.FHIRUrl, False, None, False, None), 
            ("resource", "resource", ImplementationGuideManifestResource, True, None, True, None), 
            ("page", "page", ImplementationGuideManifestPage, True, None, False, None), 
            ("image", "image", fhirdatatypes.FHIRString, True, None, False, None), 
            ("other", "other", fhirdatatypes.FHIRString, True, None, False, None), 
        ])
        return js




class ImplementationGuideManifestPage(backboneelement.BackboneElement):
    """ HTML page within the parent IG.
    
    Information about a page within the IG.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ HTML page name.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Title of the page, for references.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.anchor = None
        """ Anchor available on the page.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        super(ImplementationGuideManifestPage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideManifestPage, self).elementProperties()
        js.extend([
            ("name", "name", fhirdatatypes.FHIRString, False, None, True, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("anchor", "anchor", fhirdatatypes.FHIRString, True, None, False, None), 
        ])
        return js




class ImplementationGuideManifestResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.
    
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ Location of the resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.exampleBoolean = None
        """ Is an example/What is this an example of?.
        Type `bool`. """
        
        self.exampleCanonical = None
        """ Is an example/What is this an example of?.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.relativePath = None
        """ Relative path for page in IG.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        super(ImplementationGuideManifestResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideManifestResource, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, False, None, True, None), 
            ("exampleBoolean", "exampleBoolean", bool, False, "example", False, None), 
            ("exampleCanonical", "exampleCanonical", fhirdatatypes.FHIRCanonical, False, "example", False, None), 
            ("relativePath", "relativePath", fhirdatatypes.FHIRUrl, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import contactdetail

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.codesystems import guidepagegeneration

from fhirclient.codesystems import guideparametercode

from fhirclient.codesystems import publicationstatus

from fhirclient.codesystems import resourcetype

from fhirclient.models import usagecontext

