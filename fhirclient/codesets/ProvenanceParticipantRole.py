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

class ProvenanceParticipantRole(object):
    """ The role that a provenance participant played
    URL: http://hl7.org/fhir/provenance-participant-role
    ValueSet: http://hl7.org/fhir/ValueSet/provenance-agent-role
    """
    # A person entering the data into the originating system
    enterer = "enterer"
    # A person, animal, organization or device that who actually and principally carries out the activity
    performer = "performer"
    # A party that originates the resource and therefore has responsibility for the information given in the resource
	/// and ownership of this resource
    author = "author"
    # A person who verifies the correctness and appropriateness of activity
    verifier = "verifier"
    # The person authenticated the content and accepted legal responsibility for its content
    legal = "legal"
    # A verifier who attests to the accuracy of the resource
    attester = "attester"
    # A person who reported information that contributed to the resource
    informant = "informant"
    # The entity that is accountable for maintaining a true an accurate copy of the original record
    custodian = "custodian"
    # A device that operates independently of an author on custodian's algorithms for data extraction of existing
	/// information for purpose of generating a new artifact.
    assembler = "assembler"
    # A device used by an author to record new information, which may also be used by the author to select existing
	/// information for aggregation with newly recorded information for the purpose of generating a new artifact.
    composer = "composer"