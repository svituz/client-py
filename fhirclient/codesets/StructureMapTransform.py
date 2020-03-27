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

class StructureMapTransform(object):
    """ How data is copied/created.
    URL: http://hl7.org/fhir/map-transform
    ValueSet: http://hl7.org/fhir/ValueSet/map-transform
    """
    # create(type : string) - type is passed through to the application on the standard API, and must be known by it.
    create = "create"
    # copy(source).
    copy = "copy"
    # truncate(source, length) - source must be stringy type.
    truncate = "truncate"
    # escape(source, fmt1, fmt2) - change source from one kind of escaping to another (plain, java, xml, json). note
	/// that this is for when the string itself is escaped.
    escape = "escape"
    # cast(source, type?) - case source from one type to another. target type can be left as implicit if there is one
	/// and only one target type known.
    cast = "cast"
    # append(source...) - source is element or string.
    append = "append"
    # translate(source, uri_of_map) - use the translate operation.
    translate = "translate"
    # reference(source : object) - return a string that references the provided tree properly.
    reference = "reference"
    # Perform a date operation. *Parameters to be documented*.
    dateOp = "dateOp"
    # Generate a random UUID (in lowercase). No Parameters.
    uuid = "uuid"
    # Return the appropriate string to put in a reference that refers to the resource provided as a parameter.
    pointer = "pointer"
    # Execute the supplied FHIRPath expression and use the value returned by that.
    evaluate = "evaluate"
    # Create a CodeableConcept. Parameters = (text) or (system. Code[, display]).
    cc = "cc"
    # Create a Coding. Parameters = (system. Code[, display]).
    C = "c"
    # Create a quantity. Parameters = (text) or (value, unit, [system, code]) where text is the natural representation
	/// e.g. [comparator]value[space]unit.
    qty = "qty"
    # Create an identifier. Parameters = (system, value[, type]) where type is a code from the identifier type value
	/// set.
    id = "id"
    # Create a contact details. Parameters = (value) or (system, value). If no system is provided, the system should
	/// be inferred from the content of the value.
    cp = "cp"