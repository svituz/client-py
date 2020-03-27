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

class PropertyType(object):
    """ The type of a property value.
    URL: http://hl7.org/fhir/concept-property-type
    ValueSet: http://hl7.org/fhir/ValueSet/concept-property-type
    """
    # The property value is a code that identifies a concept defined in the code system.
    code = "code"
    # The property  value is a code defined in an external code system. This may be used for translations, but is not
	/// the intent.
    coding = "Coding"
    # The property value is a string.
    string = "string"
    # The property value is a string (often used to assign ranking values to concepts for supporting score
	/// assessments).
    integer = "integer"
    # The property value is a boolean true | false.
    boolean = "boolean"
    # The property is a date or a date + time.
    dateTime = "dateTime"
    # The property value is a decimal number.
    decimal = "decimal"