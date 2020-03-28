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

class FeedingDeviceCodes(object):
    """ Materials used or needed to feed the patient.
    URL: http://hl7.org/fhir/feeding-device
    """
    # Standard nipple definition:
    STANDARDNIPPLE = "standard-nipple"
    # Preemie nipple definition:
    PREEMIENIPPLE = "preemie-nipple"
    # Orthodontic nipple definition:
    ORTHONIPPLE = "ortho-nipple"
    # Slow flow nipple definition:
    SLOFLONIPPLE = "sloflo-nipple"
    # Middle flow nipple definition:
    MIDFLONIPPLE = "midflo-nipple"
    # Enlarged, cross-cut nipple definition:
    BIGCUTNIPPLE = "bigcut-nipple"
    # Haberman bottle definition:
    HABERMANBOTTLE = "haberman-bottle"
    # Sippy cup with valve definition:
    SIPPYVALVE = "sippy-valve"
    # Sippy cup without valve definition:
    SIPPYNOVALVE = "sippy-no-valve"
    # Provale Cup definition:
    PROVALECUP = "provale-cup"
    # Glass with lid/sippy cup definition:
    GLASSLID = "glass-lid"
    # Double handhold on glass/cup definition:
    HANDHOLDCUP = "handhold-cup"
    # Rubber matting under tray definition:
    RUBBERMAT = "rubber-mat"
    # Straw definition:
    STRAW = "straw"
    # Nose cup definition:
    NOSECUP = "nose-cup"
    # Scoop plate definition:
    SCOOPPLATE = "scoop-plate"
    # Hand wrap utensil holder definition:
    UTENSILHOLDER = "utensil-holder"
    # Foam handle utensils definition:
    FOAMHANDLE = "foam-handle"
    # Angled utensils definition:
    ANGLEDUTENSIL = "angled-utensil"
    # Spout cup definition:
    SPOUTCUP = "spout-cup"
    # Automated feeding devices definition:
    AUTOFEEDINGDEVICE = "autofeeding-device"
    # Rocker knife definition:
    ROCKERKNIFE = "rocker-knife"

    allowed_values = [STANDARDNIPPLE, PREEMIENIPPLE, ORTHONIPPLE, SLOFLONIPPLE, MIDFLONIPPLE, BIGCUTNIPPLE, HABERMANBOTTLE, SIPPYVALVE, SIPPYNOVALVE, PROVALECUP, GLASSLID, HANDHOLDCUP, RUBBERMAT, STRAW, NOSECUP, SCOOPPLATE, UTENSILHOLDER, FOAMHANDLE, ANGLEDUTENSIL, SPOUTCUP, AUTOFEEDINGDEVICE, ROCKERKNIFE]