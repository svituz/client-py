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

class RelatedArtifactType(object):
    """ The type of relationship to the related artifact.
    URL: http://hl7.org/fhir/related-artifact-type
    ValueSet: http://hl7.org/fhir/ValueSet/related-artifact-type
    """
    # Additional documentation for the knowledge resource. This would include additional instructions on usage as well
	/// as additional information on clinical context or appropriateness.
    documentation = "documentation"
    # A summary of the justification for the knowledge resource including supporting evidence, relevant guidelines, or
	/// other clinically important information. This information is intended to provide a way to make the justification
	/// for the knowledge resource available to the consumer of interventions or results produced by the knowledge
	/// resource.
    justification = "justification"
    # Bibliographic citation for papers, references, or other relevant material for the knowledge resource. This is
	/// intended to allow for citation of related material, but that was not necessarily specifically prepared in
	/// connection with this knowledge resource.
    citation = "citation"
    # The previous version of the knowledge resource.
    predecessor = "predecessor"
    # The next version of the knowledge resource.
    successor = "successor"
    # The knowledge resource is derived from the related artifact. This is intended to capture the relationship in
	/// which a particular knowledge resource is based on the content of another artifact, but is modified to capture
	/// either a different set of overall requirements, or a more specific set of requirements such as those involved in
	/// a particular institution or clinical setting.
    derivedFrom = "derived-from"
    # The knowledge resource depends on the given related artifact.
    dependsOn = "depends-on"
    # The knowledge resource is composed of the given related artifact.
    composedOf = "composed-of"