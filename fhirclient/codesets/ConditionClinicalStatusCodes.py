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

class ConditionClinicalStatusCodes(object):
    """ Preferred value set for Condition Clinical Status.
    URL: http://terminology.hl7.org/CodeSystem/condition-clinical
    ValueSet: http://hl7.org/fhir/ValueSet/condition-clinical
    """
    # The subject is currently experiencing the symptoms of the condition or there is evidence of the condition.
    active = "active"
    # The subject is experiencing a re-occurence or repeating of a previously resolved condition, e.g. urinary tract
	/// infection, pancreatitis, cholangitis, conjunctivitis.
    recurrence = "recurrence"
    # The subject is experiencing a return of a condition, or signs and symptoms after a period of improvement or
	/// remission, e.g. relapse of cancer, multiple sclerosis, rheumatoid arthritis, systemic lupus erythematosus,
	/// bipolar disorder, [psychotic relapse of] schizophrenia, etc.
    relapse = "relapse"
    # The subject is no longer experiencing the symptoms of the condition or there is no longer evidence of the
	/// condition.
    inactive = "inactive"
    # The subject is no longer experiencing the symptoms of the condition, but there is a risk of the symptoms
	/// returning.
    remission = "remission"
    # The subject is no longer experiencing the symptoms of the condition and there is a negligible perceived risk of
	/// the symptoms returning.
    resolved = "resolved"