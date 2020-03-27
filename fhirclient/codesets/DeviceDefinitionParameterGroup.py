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
    # Haemodynamic Parameter Group - MDC_PGRP_HEMO.
    haemodynamic = "haemodynamic"
    # ECG Parameter Group - MDC_PGRP_ECG.
    ecg = "ecg"
    # Respiratory Parameter Group - MDC_PGRP_RESP.
    respiratory = "respiratory"
    # Ventilation Parameter Group - MDC_PGRP_VENT.
    ventilation = "ventilation"
    # Neurological Parameter Group - MDC_PGRP_NEURO.
    neurological = "neurological"
    # Drug Delivery Parameter Group - MDC_PGRP_DRUG.
    drugDelivery = "drug-delivery"
    # Fluid Chemistry Parameter Group - MDC_PGRP_FLUID.
    fluidChemistry = "fluid-chemistry"
    # Blood Chemistry Parameter Group - MDC_PGRP_BLOOD_CHEM.
    bloodChemistry = "blood-chemistry"
    # Miscellaneous Parameter Group - MDC_PGRP_MISC.
    miscellaneous = "miscellaneous"