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
    # licBoard
    licBoard = "lic-board"
    # prim
    prim = "prim"
    # contEd
    contEd = "cont-ed"
    # postServ
    postServ = "post-serv"
    # relOwn
    relOwn = "rel-own"
    # regAuth
    regAuth = "reg-auth"
    # legal
    legal = "legal"
    # issuer
    issuer = "issuer"
    # authSource
    authSource = "auth-source"