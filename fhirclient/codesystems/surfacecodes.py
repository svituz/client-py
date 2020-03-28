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

class SurfaceCodes(object):
    """ This value set includes a smattering of FDI tooth surface codes.
    URL: http://terminology.hl7.org/CodeSystem/FDI-surface
    ValueSet: http://hl7.org/fhir/ValueSet/surface
    """
    # The surface of a tooth that is closest to the midline (middle) of the face.
    M = "M"
    # The chewing surface of posterior teeth.
    O = "O"
    # The biting edge of anterior teeth.
    I = "I"
    # The surface of a tooth that faces away from the midline of the face.
    D = "D"
    # The surface of a posterior tooth facing the cheeks.
    B = "B"
    # The surface of a tooth facing the lips.
    V = "V"
    # The surface of a tooth facing the tongue.
    L = "L"
    # The Mesioclusal surfaces of a tooth.
    MO = "MO"
    # The Distoclusal surfaces of a tooth.
    DO = "DO"
    # The Distoincisal surfaces of a tooth.
    DI = "DI"
    # The Mesioclusodistal surfaces of a tooth.
    MOD = "MOD"

    allowed_values = [M, O, I, D, B, V, L, MO, DO, DI, MOD]