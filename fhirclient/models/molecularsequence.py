#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MolecularSequence)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

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
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("type", "type", fhirdatatypes.FHIRCode, False, None, False, sequencetype.SequenceType), 
            ("coordinateSystem", "coordinateSystem", int, False, None, True, None), 
            ("patient", "patient", fhirreference.FHIRReference, False, None, False, None), 
            ("specimen", "specimen", fhirreference.FHIRReference, False, None, False, None), 
            ("device", "device", fhirreference.FHIRReference, False, None, False, None), 
            ("performer", "performer", fhirreference.FHIRReference, False, None, False, None), 
            ("quantity", "quantity", quantity.Quantity, False, None, False, None), 
            ("referenceSeq", "referenceSeq", MolecularSequenceReferenceSeq, False, None, False, None), 
            ("variant", "variant", MolecularSequenceVariant, True, None, False, None), 
            ("observedSeq", "observedSeq", fhirdatatypes.FHIRString, False, None, False, None), 
            ("quality", "quality", MolecularSequenceQuality, True, None, False, None), 
            ("readCoverage", "readCoverage", int, False, None, False, None), 
            ("repository", "repository", MolecularSequenceRepository, True, None, False, None), 
            ("pointer", "pointer", fhirreference.FHIRReference, True, None, False, None), 
            ("structureVariant", "structureVariant", MolecularSequenceStructureVariant, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

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
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, qualitytype.QualityType), 
            ("standardSequence", "standardSequence", codeableconcept.CodeableConcept, False, None, False, None), 
            ("start", "start", int, False, None, False, None), 
            ("end", "end", int, False, None, False, None), 
            ("score", "score", quantity.Quantity, False, None, False, None), 
            ("method", "method", codeableconcept.CodeableConcept, False, None, False, None), 
            ("truthTP", "truthTP", float, False, None, False, None), 
            ("queryTP", "queryTP", float, False, None, False, None), 
            ("truthFN", "truthFN", float, False, None, False, None), 
            ("queryFP", "queryFP", float, False, None, False, None), 
            ("gtFP", "gtFP", float, False, None, False, None), 
            ("precision", "precision", float, False, None, False, None), 
            ("recall", "recall", float, False, None, False, None), 
            ("fScore", "fScore", float, False, None, False, None), 
            ("roc", "roc", MolecularSequenceQualityRoc, False, None, False, None), 
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
            ("score", "score", int, True, None, False, None), 
            ("numTP", "numTP", int, True, None, False, None), 
            ("numFP", "numFP", int, True, None, False, None), 
            ("numFN", "numFN", int, True, None, False, None), 
            ("precision", "precision", float, True, None, False, None), 
            ("sensitivity", "sensitivity", float, True, None, False, None), 
            ("fMeasure", "fMeasure", float, True, None, False, None), 
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
            ("chromosome", "chromosome", codeableconcept.CodeableConcept, False, None, False, None), 
            ("genomeBuild", "genomeBuild", fhirdatatypes.FHIRString, False, None, False, None), 
            ("orientation", "orientation", fhirdatatypes.FHIRCode, False, None, False, orientationtype.OrientationType), 
            ("referenceSeqId", "referenceSeqId", codeableconcept.CodeableConcept, False, None, False, None), 
            ("referenceSeqPointer", "referenceSeqPointer", fhirreference.FHIRReference, False, None, False, None), 
            ("referenceSeqString", "referenceSeqString", fhirdatatypes.FHIRString, False, None, False, None), 
            ("strand", "strand", fhirdatatypes.FHIRCode, False, None, False, strandtype.StrandType), 
            ("windowStart", "windowStart", int, False, None, False, None), 
            ("windowEnd", "windowEnd", int, False, None, False, None), 
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
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, repositorytype.RepositoryType), 
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("datasetId", "datasetId", fhirdatatypes.FHIRString, False, None, False, None), 
            ("variantsetId", "variantsetId", fhirdatatypes.FHIRString, False, None, False, None), 
            ("readsetId", "readsetId", fhirdatatypes.FHIRString, False, None, False, None), 
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
            ("variantType", "variantType", codeableconcept.CodeableConcept, False, None, False, None), 
            ("exact", "exact", bool, False, None, False, None), 
            ("length", "length", int, False, None, False, None), 
            ("outer", "outer", MolecularSequenceStructureVariantOuter, False, None, False, None), 
            ("inner", "inner", MolecularSequenceStructureVariantInner, False, None, False, None), 
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
            ("start", "start", int, False, None, False, None), 
            ("end", "end", int, False, None, False, None), 
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
            ("start", "start", int, False, None, False, None), 
            ("end", "end", int, False, None, False, None), 
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
            ("start", "start", int, False, None, False, None), 
            ("end", "end", int, False, None, False, None), 
            ("observedAllele", "observedAllele", fhirdatatypes.FHIRString, False, None, False, None), 
            ("referenceAllele", "referenceAllele", fhirdatatypes.FHIRString, False, None, False, None), 
            ("cigar", "cigar", fhirdatatypes.FHIRString, False, None, False, None), 
            ("variantPointer", "variantPointer", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import orientationtype

from fhirclient.codesystems import qualitytype

from fhirclient.models import quantity

from fhirclient.codesystems import repositorytype

from fhirclient.codesystems import sequencetype

from fhirclient.codesystems import strandtype

