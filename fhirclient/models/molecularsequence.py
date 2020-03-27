#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MolecularSequence)
#  2020, SMART Health IT.


from . import domainresource

class MolecularSequence(domainresource.DomainResource):
    """ Information about a biological sequence.
    
    Raw data describing a biological sequence.
    """
    
    resource_type = "MolecularSequence"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Unique ID for this particular sequence. This is a FHIR-defined id.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.type = None
        """ aa | dna | rna.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.coordinateSystem = None
        """ Base number of coordinate system (0 for 0-based numbering or
        coordinates, inclusive start, exclusive end, 1 for 1-based
        numbering, inclusive start, inclusive end).
        Type `int`. """
        
        self.patient = None
        """ Who and/or what this is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.specimen = None
        """ Specimen used for sequencing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.device = None
        """ The method for sequencing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who should be responsible for test result.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ The number of copies of the sequence of interest.  (RNASeq).
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.referenceSeq = None
        """ A sequence used as reference.
        Type `MolecularSequenceReferenceSeq` (represented as `dict` in JSON). """
        
        self.variant = None
        """ Variant in sequence.
        List of `MolecularSequenceVariant` items (represented as `dict` in JSON). """
        
        self.observedSeq = None
        """ Sequence that was observed.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.quality = None
        """ An set of value as quality of sequence.
        List of `MolecularSequenceQuality` items (represented as `dict` in JSON). """
        
        self.readCoverage = None
        """ Average number of reads representing a given nucleotide in the
        reconstructed sequence.
        Type `int`. """
        
        self.repository = None
        """ External repository which contains detailed report related with
        observedSeq in this resource.
        List of `MolecularSequenceRepository` items (represented as `dict` in JSON). """
        
        self.pointer = None
        """ Pointer to next atomic sequence.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.structureVariant = None
        """ Structural variant.
        List of `MolecularSequenceStructureVariant` items (represented as `dict` in JSON). """
        
        super(MolecularSequence, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequence, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("type", "type", fhirdatatypes.FHIRCode, False, None, False),
            ("coordinateSystem", "coordinateSystem", int, False, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, False, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("referenceSeq", "referenceSeq", MolecularSequenceReferenceSeq, False, None, False),
            ("variant", "variant", MolecularSequenceVariant, True, None, False),
            ("observedSeq", "observedSeq", fhirdatatypes.FHIRString, False, None, False),
            ("quality", "quality", MolecularSequenceQuality, True, None, False),
            ("readCoverage", "readCoverage", int, False, None, False),
            ("repository", "repository", MolecularSequenceRepository, True, None, False),
            ("pointer", "pointer", fhirreference.FHIRReference, True, None, False),
            ("structureVariant", "structureVariant", MolecularSequenceStructureVariant, True, None, False),
        ])
        return js



from . import backboneelement

class MolecularSequenceQuality(backboneelement.BackboneElement):
    """ An set of value as quality of sequence.
    
    An experimental feature attribute that defines the quality of the feature
    in a quantitative way, such as a phred quality score ([SO:0001686](http://w
    ww.sequenceontology.org/browser/current_svn/term/SO:0001686)).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ indel | snp | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.standardSequence = None
        """ Standard sequence for comparison.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.start = None
        """ Start position of the sequence.
        Type `int`. """
        
        self.end = None
        """ End position of the sequence.
        Type `int`. """
        
        self.score = None
        """ Quality score for the comparison.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.method = None
        """ Method to get quality.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.truthTP = None
        """ True positives from the perspective of the truth data.
        Type `float`. """
        
        self.queryTP = None
        """ True positives from the perspective of the query data.
        Type `float`. """
        
        self.truthFN = None
        """ False negatives.
        Type `float`. """
        
        self.queryFP = None
        """ False positives.
        Type `float`. """
        
        self.gtFP = None
        """ False positives where the non-REF alleles in the Truth and Query
        Call Sets match.
        Type `float`. """
        
        self.precision = None
        """ Precision of comparison.
        Type `float`. """
        
        self.recall = None
        """ Recall of comparison.
        Type `float`. """
        
        self.fScore = None
        """ F-score.
        Type `float`. """
        
        self.roc = None
        """ Receiver Operator Characteristic (ROC) Curve.
        Type `MolecularSequenceQualityRoc` (represented as `dict` in JSON). """
        
        super(MolecularSequenceQuality, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceQuality, self).elementProperties()
        js.extend([
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True),
            ("standardSequence", "standardSequence", codeableconcept.CodeableConcept, False, None, False),
            ("start", "start", int, False, None, False),
            ("end", "end", int, False, None, False),
            ("score", "score", quantity.Quantity, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("truthTP", "truthTP", float, False, None, False),
            ("queryTP", "queryTP", float, False, None, False),
            ("truthFN", "truthFN", float, False, None, False),
            ("queryFP", "queryFP", float, False, None, False),
            ("gtFP", "gtFP", float, False, None, False),
            ("precision", "precision", float, False, None, False),
            ("recall", "recall", float, False, None, False),
            ("fScore", "fScore", float, False, None, False),
            ("roc", "roc", MolecularSequenceQualityRoc, False, None, False),
        ])
        return js




class MolecularSequenceQualityRoc(backboneelement.BackboneElement):
    """ Receiver Operator Characteristic (ROC) Curve.
    
    Receiver Operator Characteristic (ROC) Curve  to give
    sensitivity/specificity tradeoff.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.score = None
        """ Genotype quality score.
        List of `int` items. """
        
        self.numTP = None
        """ Roc score true positive numbers.
        List of `int` items. """
        
        self.numFP = None
        """ Roc score false positive numbers.
        List of `int` items. """
        
        self.numFN = None
        """ Roc score false negative numbers.
        List of `int` items. """
        
        self.precision = None
        """ Precision of the GQ score.
        List of `float` items. """
        
        self.sensitivity = None
        """ Sensitivity of the GQ score.
        List of `float` items. """
        
        self.fMeasure = None
        """ FScore of the GQ score.
        List of `float` items. """
        
        super(MolecularSequenceQualityRoc, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceQualityRoc, self).elementProperties()
        js.extend([
            ("score", "score", int, True, None, False),
            ("numTP", "numTP", int, True, None, False),
            ("numFP", "numFP", int, True, None, False),
            ("numFN", "numFN", int, True, None, False),
            ("precision", "precision", float, True, None, False),
            ("sensitivity", "sensitivity", float, True, None, False),
            ("fMeasure", "fMeasure", float, True, None, False),
        ])
        return js




class MolecularSequenceReferenceSeq(backboneelement.BackboneElement):
    """ A sequence used as reference.
    
    A sequence that is used as a reference to describe variants that are
    present in a sequence analyzed.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.chromosome = None
        """ Chromosome containing genetic finding.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.genomeBuild = None
        """ The Genome Build used for reference, following GRCh build versions
        e.g. 'GRCh 37'.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.orientation = None
        """ sense | antisense.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.referenceSeqId = None
        """ Reference identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.referenceSeqPointer = None
        """ A pointer to another MolecularSequence entity as reference sequence.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referenceSeqString = None
        """ A string to represent reference sequence.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.strand = None
        """ watson | crick.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.windowStart = None
        """ Start position of the window on the  reference sequence.
        Type `int`. """
        
        self.windowEnd = None
        """ End position of the window on the reference sequence.
        Type `int`. """
        
        super(MolecularSequenceReferenceSeq, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceReferenceSeq, self).elementProperties()
        js.extend([
            ("chromosome", "chromosome", codeableconcept.CodeableConcept, False, None, False),
            ("genomeBuild", "genomeBuild", fhirdatatypes.FHIRString, False, None, False),
            ("orientation", "orientation", fhirdatatypes.FHIRCode, False, None, False),
            ("referenceSeqId", "referenceSeqId", codeableconcept.CodeableConcept, False, None, False),
            ("referenceSeqPointer", "referenceSeqPointer", fhirreference.FHIRReference, False, None, False),
            ("referenceSeqString", "referenceSeqString", fhirdatatypes.FHIRString, False, None, False),
            ("strand", "strand", fhirdatatypes.FHIRCode, False, None, False),
            ("windowStart", "windowStart", int, False, None, False),
            ("windowEnd", "windowEnd", int, False, None, False),
        ])
        return js




class MolecularSequenceRepository(backboneelement.BackboneElement):
    """ External repository which contains detailed report related with observedSeq
    in this resource.
    
    Configurations of the external repository. The repository shall store
    target's observedSeq or records related with target's observedSeq.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ directlink | openapi | login | oauth | other.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.url = None
        """ URI of the repository.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.name = None
        """ Repository's name.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.datasetId = None
        """ Id of the dataset that used to call for dataset in repository.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.variantsetId = None
        """ Id of the variantset that used to call for variantset in repository.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.readsetId = None
        """ Id of the read.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(MolecularSequenceRepository, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceRepository, self).elementProperties()
        js.extend([
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True),
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False),
            ("name", "name", fhirdatatypes.FHIRString, False, None, False),
            ("datasetId", "datasetId", fhirdatatypes.FHIRString, False, None, False),
            ("variantsetId", "variantsetId", fhirdatatypes.FHIRString, False, None, False),
            ("readsetId", "readsetId", fhirdatatypes.FHIRString, False, None, False),
        ])
        return js




class MolecularSequenceStructureVariant(backboneelement.BackboneElement):
    """ Structural variant.
    
    Information about chromosome structure variation.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.variantType = None
        """ Structural variant change type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.exact = None
        """ Does the structural variant have base pair resolution breakpoints?.
        Type `bool`. """
        
        self.length = None
        """ Structural variant length.
        Type `int`. """
        
        self.outer = None
        """ Structural variant outer.
        Type `MolecularSequenceStructureVariantOuter` (represented as `dict` in JSON). """
        
        self.inner = None
        """ Structural variant inner.
        Type `MolecularSequenceStructureVariantInner` (represented as `dict` in JSON). """
        
        super(MolecularSequenceStructureVariant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceStructureVariant, self).elementProperties()
        js.extend([
            ("variantType", "variantType", codeableconcept.CodeableConcept, False, None, False),
            ("exact", "exact", bool, False, None, False),
            ("length", "length", int, False, None, False),
            ("outer", "outer", MolecularSequenceStructureVariantOuter, False, None, False),
            ("inner", "inner", MolecularSequenceStructureVariantInner, False, None, False),
        ])
        return js




class MolecularSequenceStructureVariantInner(backboneelement.BackboneElement):
    """ Structural variant inner.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.start = None
        """ Structural variant inner start.
        Type `int`. """
        
        self.end = None
        """ Structural variant inner end.
        Type `int`. """
        
        super(MolecularSequenceStructureVariantInner, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceStructureVariantInner, self).elementProperties()
        js.extend([
            ("start", "start", int, False, None, False),
            ("end", "end", int, False, None, False),
        ])
        return js




class MolecularSequenceStructureVariantOuter(backboneelement.BackboneElement):
    """ Structural variant outer.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.start = None
        """ Structural variant outer start.
        Type `int`. """
        
        self.end = None
        """ Structural variant outer end.
        Type `int`. """
        
        super(MolecularSequenceStructureVariantOuter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceStructureVariantOuter, self).elementProperties()
        js.extend([
            ("start", "start", int, False, None, False),
            ("end", "end", int, False, None, False),
        ])
        return js




class MolecularSequenceVariant(backboneelement.BackboneElement):
    """ Variant in sequence.
    
    The definition of variant here originates from Sequence ontology ([variant_
    of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)).
    This element can represent amino acid or nucleic sequence change(including
    insertion,deletion,SNP,etc.)  It can represent some complex mutation or
    segment variation with the assist of CIGAR string.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.start = None
        """ Start position of the variant on the  reference sequence.
        Type `int`. """
        
        self.end = None
        """ End position of the variant on the reference sequence.
        Type `int`. """
        
        self.observedAllele = None
        """ Allele that was observed.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.referenceAllele = None
        """ Allele in the reference sequence.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.cigar = None
        """ Extended CIGAR string for aligning the sequence with reference
        bases.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.variantPointer = None
        """ Pointer to observed variant information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MolecularSequenceVariant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceVariant, self).elementProperties()
        js.extend([
            ("start", "start", int, False, None, False),
            ("end", "end", int, False, None, False),
            ("observedAllele", "observedAllele", fhirdatatypes.FHIRString, False, None, False),
            ("referenceAllele", "referenceAllele", fhirdatatypes.FHIRString, False, None, False),
            ("cigar", "cigar", fhirdatatypes.FHIRString, False, None, False),
            ("variantPointer", "variantPointer", fhirreference.FHIRReference, False, None, False),
        ])
        return js



import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']

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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']

