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

class ClaimInformationCategoryCodes(object):
    """ This value set includes sample Information Category codes.
    URL: http://terminology.hl7.org/CodeSystem/claiminformationcategory
    ValueSet: http://hl7.org/fhir/ValueSet/claim-informationcategory
    """
    # Codes conveying additional situation and condition information.
    INFO = "info"
    # Discharge status and discharge to locations.
    DISCHARGE = "discharge"
    # Period, start or end dates of aspects of the Condition.
    ONSET = "onset"
    # Nature and date of the related event e.g. Last exam, service, X-ray etc.
    RELATED = "related"
    # Insurance policy exceptions.
    EXCEPTION = "exception"
    # Materials being forwarded, e.g. Models, molds, images, documents.
    MATERIAL = "material"
    # Materials attached such as images, documents and resources.
    ATTACHMENT = "attachment"
    # Teeth which are missing for any reason, for example: prior extraction, never developed.
    MISSINGTOOTH = "missingtooth"
    # The type of prosthesis and date of supply if a previously supplied prosthesis.
    PROSTHESIS = "prosthesis"
    # Other information identified by the type.system.
    OTHER = "other"
    # An indication that the patient was hospitalized, the period if known otherwise a Yes/No (boolean).
    HOSPITALIZED = "hospitalized"
    # An indication that the patient was unable to work, the period if known otherwise a Yes/No (boolean).
    EMPLOYMENTIMPACTED = "employmentimpacted"
    # The external cause of an illness or injury.
    EXTERNALCAUSE = "externalcause"
    # The reason for the patient visit.
    PATIENTREASONFORVISIT = "patientreasonforvisit"

    allowed_values = [INFO, DISCHARGE, ONSET, RELATED, EXCEPTION, MATERIAL, ATTACHMENT, MISSINGTOOTH, PROSTHESIS, OTHER, HOSPITALIZED, EMPLOYMENTIMPACTED, EXTERNALCAUSE, PATIENTREASONFORVISIT]