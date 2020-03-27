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

class NoteType(object):
    """ The presentation types of notes.
    URL: http://hl7.org/fhir/note-type
    ValueSet: http://hl7.org/fhir/ValueSet/note-type
    """
    # Display the note.
    display = "display"
    # Print the note on the form.
    print = "print"
    # Print the note for the operator.
    printoper = "printoper"