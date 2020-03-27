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

class EventTiming(object):
    """ Real world event relating to the schedule.
    URL: http://hl7.org/fhir/event-timing
    """
    # Event occurs during the morning. The exact time is unspecified and established by institution convention or
	/// patient interpretation.
    MORN = "MORN"
    # Event occurs during the early morning. The exact time is unspecified and established by institution convention
	/// or patient interpretation.
    mORNEarly = "MORN.early"
    # Event occurs during the late morning. The exact time is unspecified and established by institution convention or
	/// patient interpretation.
    mORNLate = "MORN.late"
    # Event occurs around 12:00pm. The exact time is unspecified and established by institution convention or patient
	/// interpretation.
    NOON = "NOON"
    # Event occurs during the afternoon. The exact time is unspecified and established by institution convention or
	/// patient interpretation.
    AFT = "AFT"
    # Event occurs during the early afternoon. The exact time is unspecified and established by institution convention
	/// or patient interpretation.
    aFTEarly = "AFT.early"
    # Event occurs during the late afternoon. The exact time is unspecified and established by institution convention
	/// or patient interpretation.
    aFTLate = "AFT.late"
    # Event occurs during the evening. The exact time is unspecified and established by institution convention or
	/// patient interpretation.
    EVE = "EVE"
    # Event occurs during the early evening. The exact time is unspecified and established by institution convention
	/// or patient interpretation.
    eVEEarly = "EVE.early"
    # Event occurs during the late evening. The exact time is unspecified and established by institution convention or
	/// patient interpretation.
    eVELate = "EVE.late"
    # Event occurs during the night. The exact time is unspecified and established by institution convention or
	/// patient interpretation.
    NIGHT = "NIGHT"
    # Event occurs [offset] after subject goes to sleep. The exact time is unspecified and established by institution
	/// convention or patient interpretation.
    PHS = "PHS"