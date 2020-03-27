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

class NetworkTypeCodes(object):
    """ This value set includes a smattering of Network type codes.
    URL: http://terminology.hl7.org/CodeSystem/benefit-network
    ValueSet: http://hl7.org/fhir/ValueSet/benefit-network
    """
    # Services rendered by a Network provider
    in = "in"
    # Services rendered by a provider who is not in the Network
    out = "out"