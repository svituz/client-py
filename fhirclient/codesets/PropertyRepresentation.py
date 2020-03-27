#
#  CodeSystems.py
#  client-py
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.
#
#  THIS HAS BEEN ADAPTED FROM Swift Enums WITHOUT EVER BEING IMPLEMENTED IN
#  Python, FOR DEMONSTRATION PURPOSES ONLY.
#

class PropertyRepresentation(object):
    """ How a property is represented when serialized.
    URL: http://hl7.org/fhir/property-representation
    ValueSet: http://hl7.org/fhir/ValueSet/property-representation
    """
    # In XML, this property is represented as an attribute not an element.
    xmlAttr = "xmlAttr"
    # This element is represented using the XML text attribute (primitives only).
    xmlText = "xmlText"
    # The type of this element is indicated using xsi:type.
    typeAttr = "typeAttr"
    # Use CDA narrative instead of XHTML.
    cdaText = "cdaText"
    # The property is represented using XHTML.
    xhtml = "xhtml"