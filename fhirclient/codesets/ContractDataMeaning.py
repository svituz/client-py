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

class ContractDataMeaning(object):
    """ How a resource reference is interpreted when evaluating contract offers.
    URL: http://terminology.hl7.org/CodeSystem/contract-data-meaning
    ValueSet: http://hl7.org/fhir/ValueSet/contract-data-meaning
    """
    # The consent applies directly to the instance of the resource.
    instance = "instance"
    # The consent applies directly to the instance of the resource and instances it refers to.
    related = "related"
    # The consent applies directly to the instance of the resource and instances that refer to it.
    dependents = "dependents"
    # The consent applies to instances of resources that are authored by.
    authoredby = "authoredby"