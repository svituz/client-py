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

class ProvenanceParticipantType(object):
    """ The type of participation a provenance participant.
    URL: http://terminology.hl7.org/CodeSystem/provenance-participant-type
    ValueSet: http://hl7.org/fhir/ValueSet/provenance-agent-type
    """
    # A person entering the data into the originating system
    ENTERER = "enterer"
    # A person, animal, organization or device that who actually and principally carries out the activity
    PERFORMER = "performer"
    # A party that originates the resource and therefore has responsibility for the information given in the resource
    # and ownership of this resource
    AUTHOR = "author"
    # A person who verifies the correctness and appropriateness of activity
    VERIFIER = "verifier"
    # The person authenticated the content and accepted legal responsibility for its content
    LEGAL = "legal"
    # A verifier who attests to the accuracy of the resource
    ATTESTER = "attester"
    # A person who reported information that contributed to the resource
    INFORMANT = "informant"
    # The entity that is accountable for maintaining a true an accurate copy of the original record
    CUSTODIAN = "custodian"
    # A device that operates independently of an author on custodian's algorithms for data extraction of existing
    # information for purpose of generating a new artifact.
    ASSEMBLER = "assembler"
    # A device used by an author to record new information, which may also be used by the author to select existing
    # information for aggregation with newly recorded information for the purpose of generating a new artifact.
    COMPOSER = "composer"

    allowed_values = [ENTERER, PERFORMER, AUTHOR, VERIFIER, LEGAL, ATTESTER, INFORMANT, CUSTODIAN, ASSEMBLER, COMPOSER]