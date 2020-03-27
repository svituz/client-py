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

class AddressUse(object):
    """ The use of an address.
    URL: http://hl7.org/fhir/address-use
    ValueSet: http://hl7.org/fhir/ValueSet/address-use
    """
    # A communication address at a home.
    home = "home"
    # An office address. First choice for business related contacts during business hours.
    work = "work"
    # A temporary address. The period can provide more detailed information.
    temp = "temp"
    # This address is no longer in use (or was never correct but retained for records).
    old = "old"
    # An address to be used to send bills, invoices, receipts etc.
    billing = "billing"