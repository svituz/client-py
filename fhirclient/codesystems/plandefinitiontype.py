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

class PlanDefinitionType(object):
    """ The type of PlanDefinition.
    URL: http://terminology.hl7.org/CodeSystem/plan-definition-type
    ValueSet: http://hl7.org/fhir/ValueSet/plan-definition-type
    """
    # A pre-defined and approved group of orders related to a particular clinical condition (e.g. hypertension
    # treatment and monitoring) or stage of care (e.g. hospital admission to Coronary Care Unit). An order set is used
    # as a checklist for the clinician when managing a patient with a specific condition. It is a structured
    # collection of orders relevant to that condition and presented to the clinician in a computerized provider order
    # entry (CPOE) system.
    ORDERSET = "order-set"
    # Defines a desired/typical sequence of clinical activities including preconditions, triggers and temporal
    # relationships.
    CLINICALPROTOCOL = "clinical-protocol"
    # A decision support rule of the form [on Event] if Condition then Action. It is intended to be a shareable,
    # computable definition of actions that should be taken whenever some condition is met in response to a particular
    # event or events.
    ECARULE = "eca-rule"
    # Defines the steps for a group of one or more systems in an event flow process along with the step constraints,
    # sequence, pre-conditions and decision points to complete a particular objective.
    WORKFLOWDEFINITION = "workflow-definition"

    allowed_values = [ORDERSET, CLINICALPROTOCOL, ECARULE, WORKFLOWDEFINITION]