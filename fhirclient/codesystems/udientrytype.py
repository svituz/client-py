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

class UDIEntryType(object):
    """ Codes to identify how UDI data was entered.
    URL: http://hl7.org/fhir/udi-entry-type
    ValueSet: http://hl7.org/fhir/ValueSet/udi-entry-type
    """
    """a barcodescanner captured the data from the device label."""
    BARCODE = "barcode"
    """An RFID chip reader captured the data from the device label."""
    RFID = "rfid"
    """The data was read from the label by a person and manually entered. (e.g.  via a keyboard)."""
    MANUAL = "manual"
    """The data originated from a patient's implant card and was read by an operator."""
    CARD = "card"
    """The data originated from a patient source and was not directly scanned or read from a label or card."""
    SELFREPORTED = "self-reported"
    """The method of data capture has not been determined."""
    UNKNOWN = "unknown"
    allowed_values = ['BARCODE', 'RFID', 'MANUAL', 'CARD', 'SELFREPORTED', 'UNKNOWN']