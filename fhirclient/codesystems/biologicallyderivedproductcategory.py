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

class BiologicallyDerivedProductCategory(object):
    """ Biologically Derived Product Category.
    URL: http://hl7.org/fhir/product-category
    ValueSet: http://hl7.org/fhir/ValueSet/product-category
    """
    """A collection of tissues joined in a structural unit to serve a common function."""
    ORGAN = "organ"
    """An ensemble of similar cells and their extracellular matrix from the same origin that together carry out a
	/// specific function."""
    TISSUE = "tissue"
    """Body fluid."""
    FLUID = "fluid"
    """Collection of cells."""
    CELLS = "cells"
    """Biological agent of unspecified type."""
    BIOLOGICALAGENT = "biologicalAgent"
    allowed_values = ['ORGAN', 'TISSUE', 'FLUID', 'CELLS', 'BIOLOGICALAGENT']