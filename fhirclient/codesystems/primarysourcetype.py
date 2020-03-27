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

class PrimarySourceType(object):
    """ Type of the validation primary source
    URL: http://terminology.hl7.org/CodeSystem/primary-source-type
    ValueSet: http://hl7.org/fhir/ValueSet/verificationresult-primary-source-type
    """
    """licBoard"""
    LICBOARD = "lic-board"
    """prim"""
    PRIM = "prim"
    """contEd"""
    CONTED = "cont-ed"
    """postServ"""
    POSTSERV = "post-serv"
    """relOwn"""
    RELOWN = "rel-own"
    """regAuth"""
    REGAUTH = "reg-auth"
    """legal"""
    LEGAL = "legal"
    """issuer"""
    ISSUER = "issuer"
    """authSource"""
    AUTHSOURCE = "auth-source"
    allowed_values = ['LICBOARD', 'PRIM', 'CONTED', 'POSTSERV', 'RELOWN', 'REGAUTH', 'LEGAL', 'ISSUER', 'AUTHSOURCE']