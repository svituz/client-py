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

class DeviceDefinitionParameterGroup(object):
    """ Codes identifying groupings of parameters; e.g. Cardiovascular.
    URL: http://terminology.hl7.org/CodeSystem/parameter-group
    ValueSet: http://hl7.org/fhir/ValueSet/parameter-group
    """
    """Haemodynamic Parameter Group - MDC_PGRP_HEMO."""
    HAEMODYNAMIC = "haemodynamic"
    """ECG Parameter Group - MDC_PGRP_ECG."""
    ECG = "ecg"
    """Respiratory Parameter Group - MDC_PGRP_RESP."""
    RESPIRATORY = "respiratory"
    """Ventilation Parameter Group - MDC_PGRP_VENT."""
    VENTILATION = "ventilation"
    """Neurological Parameter Group - MDC_PGRP_NEURO."""
    NEUROLOGICAL = "neurological"
    """Drug Delivery Parameter Group - MDC_PGRP_DRUG."""
    DRUGDELIVERY = "drug-delivery"
    """Fluid Chemistry Parameter Group - MDC_PGRP_FLUID."""
    FLUIDCHEMISTRY = "fluid-chemistry"
    """Blood Chemistry Parameter Group - MDC_PGRP_BLOOD_CHEM."""
    BLOODCHEMISTRY = "blood-chemistry"
    """Miscellaneous Parameter Group - MDC_PGRP_MISC."""
    MISCELLANEOUS = "miscellaneous"
    allowed_values = ['HAEMODYNAMIC', 'ECG', 'RESPIRATORY', 'VENTILATION', 'NEUROLOGICAL', 'DRUGDELIVERY', 'FLUIDCHEMISTRY', 'BLOODCHEMISTRY', 'MISCELLANEOUS']