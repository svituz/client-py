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

class ConsentDataMeaning(object):
    """ How a resource reference is interpreted when testing consent restrictions.
    URL: http://hl7.org/fhir/consent-data-meaning
    ValueSet: http://hl7.org/fhir/ValueSet/consent-data-meaning
    """
    # The consent applies directly to the instance of the resource.
    instance = "instance"
    # The consent applies directly to the instance of the resource and instances it refers to.
    related = "related"
    # The consent applies directly to the instance of the resource and instances that refer to it.
    dependents = "dependents"
    # The consent applies to instances of resources that are authored by.
    authoredby = "authoredby"