#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ProdCharacteristic) on 2020-03-26.
#  2020, SMART Health IT.


from . import backboneelement

class ProdCharacteristic(backboneelement.BackboneElement):
    """ The marketing status describes the date when a medicinal product is
    actually put on the market or the date as of which it is no longer
    available.
    """
    
    resource_type = "ProdCharacteristic"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.color = None
        """ Where applicable, the color can be specified An appropriate
        controlled vocabulary shall be used The term and the term
        identifier shall be used.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.depth = None
        """ Where applicable, the depth can be specified using a numerical
        value and its unit of measurement The unit of measurement shall be
        specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.externalDiameter = None
        """ Where applicable, the external diameter can be specified using a
        numerical value and its unit of measurement The unit of measurement
        shall be specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.height = None
        """ Where applicable, the height can be specified using a numerical
        value and its unit of measurement The unit of measurement shall be
        specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.image = None
        """ Where applicable, the image can be provided The format of the image
        attachment shall be specified by regional implementations.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.imprint = None
        """ Where applicable, the imprint can be specified as text.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.nominalVolume = None
        """ Where applicable, the nominal volume can be specified using a
        numerical value and its unit of measurement The unit of measurement
        shall be specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.scoring = None
        """ Where applicable, the scoring can be specified An appropriate
        controlled vocabulary shall be used The term and the term
        identifier shall be used.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.shape = None
        """ Where applicable, the shape can be specified An appropriate
        controlled vocabulary shall be used The term and the term
        identifier shall be used.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.weight = None
        """ Where applicable, the weight can be specified using a numerical
        value and its unit of measurement The unit of measurement shall be
        specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.width = None
        """ Where applicable, the width can be specified using a numerical
        value and its unit of measurement The unit of measurement shall be
        specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(ProdCharacteristic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProdCharacteristic, self).elementProperties()
        js.extend([
            ("color", "color", fhirdatatypes.FHIRString, True, None, False),
            ("depth", "depth", quantity.Quantity, False, None, False),
            ("externalDiameter", "externalDiameter", quantity.Quantity, False, None, False),
            ("height", "height", quantity.Quantity, False, None, False),
            ("image", "image", attachment.Attachment, True, None, False),
            ("imprint", "imprint", fhirdatatypes.FHIRString, True, None, False),
            ("nominalVolume", "nominalVolume", quantity.Quantity, False, None, False),
            ("scoring", "scoring", codeableconcept.CodeableConcept, False, None, False),
            ("shape", "shape", fhirdatatypes.FHIRString, False, None, False),
            ("weight", "weight", quantity.Quantity, False, None, False),
            ("width", "width", quantity.Quantity, False, None, False),
        ])
        return js



import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']

try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']

try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']

