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

class SequenceType(object):
    """ Type if a sequence -- DNA, RNA, or amino acid sequence.
    URL: http://hl7.org/fhir/sequence-type
    ValueSet: http://hl7.org/fhir/ValueSet/sequence-type
    """
    # Amino acid sequence.
    AA = "aa"
    # DNA Sequence.
    DNA = "dna"
    # RNA Sequence.
    RNA = "rna"

    allowed_values = [AA, DNA, RNA]