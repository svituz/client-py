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

class MeasureType(object):
    """ The type of measure (includes codes from 2.16.840.1.113883.1.11.20368).
    URL: http://terminology.hl7.org/CodeSystem/measure-type
    ValueSet: http://hl7.org/fhir/ValueSet/measure-type
    """
    # A measure which focuses on a process which leads to a certain outcome, meaning that a scientific basis exists
    # for believing that the process, when executed well, will increase the probability of achieving a desired
    # outcome.
    PROCESS = "process"
    # A measure that indicates the result of the performance (or non-performance) of a function or process.
    OUTCOME = "outcome"
    # A measure that focuses on a health care provider's capacity, systems, and processes to provide high-quality
    # care.
    STRUCTURE = "structure"
    # A measure that focuses on patient-reported information such as patient engagement or patient experience
    # measures.
    PATIENTREPORTEDOUTCOME = "patient-reported-outcome"
    # A measure that combines multiple component measures in to a single quality measure.
    COMPOSITE = "composite"

    allowed_values = [PROCESS, OUTCOME, STRUCTURE, PATIENTREPORTEDOUTCOME, COMPOSITE]