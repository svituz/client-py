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

class ExampleCoverageFinancialExceptionCodes(object):
    """ This value set includes Example Coverage Financial Exception Codes.
    URL: http://terminology.hl7.org/CodeSystem/ex-coverage-financial-exception
    ValueSet: http://hl7.org/fhir/ValueSet/coverage-financial-exception
    """
    """Retired persons have all copays and deductibles reduced."""
    RETIRED = "retired"
    """Children in the foster care have all copays and deductibles waived."""
    FOSTER = "foster"
    allowed_values = ['RETIRED', 'FOSTER']