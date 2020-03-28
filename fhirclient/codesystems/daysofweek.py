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

class DaysOfWeek(object):
    """ The days of the week.
    URL: http://hl7.org/fhir/days-of-week
    ValueSet: http://hl7.org/fhir/ValueSet/days-of-week
    """
    # Monday.
    MON = "mon"
    # Tuesday.
    TUE = "tue"
    # Wednesday.
    WED = "wed"
    # Thursday.
    THU = "thu"
    # Friday.
    FRI = "fri"
    # Saturday.
    SAT = "sat"
    # Sunday.
    SUN = "sun"

    allowed_values = [MON, TUE, WED, THU, FRI, SAT, SUN]