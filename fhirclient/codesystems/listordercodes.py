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

class ListOrderCodes(object):
    """ Base values for the order of the items in a list resource.
    URL: http://terminology.hl7.org/CodeSystem/list-order
    ValueSet: http://hl7.org/fhir/ValueSet/list-order
    """
    """The list was sorted by a user. The criteria the user used are not specified."""
    USER = "user"
    """The list was sorted by the system. The criteria the user used are not specified; define additional codes to
	/// specify a particular order (or use other defined codes)."""
    SYSTEM = "system"
    """The list is sorted by the data of the event. This can be used when the list has items which are dates with past
	/// or future events."""
    EVENTDATE = "event-date"
    """The list is sorted by the date the item was added to the list. Note that the date added to the list is not
	/// explicit in the list itself."""
    ENTRYDATE = "entry-date"
    """The list is sorted by priority. The exact method in which priority has been determined is not specified."""
    PRIORITY = "priority"
    """The list is sorted alphabetically by an unspecified property of the items in the list."""
    ALPHABETIC = "alphabetic"
    """The list is sorted categorically by an unspecified property of the items in the list."""
    CATEGORY = "category"
    """The list is sorted by patient, with items for each patient grouped together."""
    PATIENT = "patient"
    allowed_values = ['USER', 'SYSTEM', 'EVENTDATE', 'ENTRYDATE', 'PRIORITY', 'ALPHABETIC', 'CATEGORY', 'PATIENT']