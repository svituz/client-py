#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-28.
#  2020, SMART Health IT.


class FHIRElementFactory(object):
    """ Factory class to instantiate resources by resource name.
    """
    
    @classmethod
    def instantiate(cls, resource_type, jsondict):
        """ Instantiate a resource of the type correlating to "resource_type".
        
        :param str resource_type: The name/type of the resource to instantiate
        :param dict jsondict: The JSON dictionary to use for data
        :returns: A resource of the respective type or `Element`
        """
        if "Account" == resource_type:
            from fhirclient.models import account
            return account.Account(jsondict)
        if "ActivityDefinition" == resource_type:
            from fhirclient.models import activitydefinition
            return activitydefinition.ActivityDefinition(jsondict)
        if "AdverseEvent" == resource_type:
            from fhirclient.models import adverseevent
            return adverseevent.AdverseEvent(jsondict)
        if "AllergyIntolerance" == resource_type:
            from fhirclient.models import allergyintolerance
            return allergyintolerance.AllergyIntolerance(jsondict)
        if "Appointment" == resource_type:
            from fhirclient.models import appointment
            return appointment.Appointment(jsondict)
        if "AppointmentResponse" == resource_type:
            from fhirclient.models import appointmentresponse
            return appointmentresponse.AppointmentResponse(jsondict)
        if "AuditEvent" == resource_type:
            from fhirclient.models import auditevent
            return auditevent.AuditEvent(jsondict)
        if "Basic" == resource_type:
            from fhirclient.models import basic
            return basic.Basic(jsondict)
        if "Binary" == resource_type:
            from fhirclient.models import binary
            return binary.Binary(jsondict)
        if "BiologicallyDerivedProduct" == resource_type:
            from fhirclient.models import biologicallyderivedproduct
            return biologicallyderivedproduct.BiologicallyDerivedProduct(jsondict)
        if "BodyStructure" == resource_type:
            from fhirclient.models import bodystructure
            return bodystructure.BodyStructure(jsondict)
        if "Bundle" == resource_type:
            from fhirclient.models import bundle
            return bundle.Bundle(jsondict)
        if "CapabilityStatement" == resource_type:
            from fhirclient.models import capabilitystatement
            return capabilitystatement.CapabilityStatement(jsondict)
        if "CarePlan" == resource_type:
            from fhirclient.models import careplan
            return careplan.CarePlan(jsondict)
        if "CareTeam" == resource_type:
            from fhirclient.models import careteam
            return careteam.CareTeam(jsondict)
        if "CatalogEntry" == resource_type:
            from fhirclient.models import catalogentry
            return catalogentry.CatalogEntry(jsondict)
        if "ChargeItem" == resource_type:
            from fhirclient.models import chargeitem
            return chargeitem.ChargeItem(jsondict)
        if "ChargeItemDefinition" == resource_type:
            from fhirclient.models import chargeitemdefinition
            return chargeitemdefinition.ChargeItemDefinition(jsondict)
        if "Claim" == resource_type:
            from fhirclient.models import claim
            return claim.Claim(jsondict)
        if "ClaimResponse" == resource_type:
            from fhirclient.models import claimresponse
            return claimresponse.ClaimResponse(jsondict)
        if "ClinicalImpression" == resource_type:
            from fhirclient.models import clinicalimpression
            return clinicalimpression.ClinicalImpression(jsondict)
        if "CodeSystem" == resource_type:
            from fhirclient.models import codesystem
            return codesystem.CodeSystem(jsondict)
        if "Communication" == resource_type:
            from fhirclient.models import communication
            return communication.Communication(jsondict)
        if "CommunicationRequest" == resource_type:
            from fhirclient.models import communicationrequest
            return communicationrequest.CommunicationRequest(jsondict)
        if "CompartmentDefinition" == resource_type:
            from fhirclient.models import compartmentdefinition
            return compartmentdefinition.CompartmentDefinition(jsondict)
        if "Composition" == resource_type:
            from fhirclient.models import composition
            return composition.Composition(jsondict)
        if "ConceptMap" == resource_type:
            from fhirclient.models import conceptmap
            return conceptmap.ConceptMap(jsondict)
        if "Condition" == resource_type:
            from fhirclient.models import condition
            return condition.Condition(jsondict)
        if "Consent" == resource_type:
            from fhirclient.models import consent
            return consent.Consent(jsondict)
        if "Contract" == resource_type:
            from fhirclient.models import contract
            return contract.Contract(jsondict)
        if "Coverage" == resource_type:
            from fhirclient.models import coverage
            return coverage.Coverage(jsondict)
        if "CoverageEligibilityRequest" == resource_type:
            from fhirclient.models import coverageeligibilityrequest
            return coverageeligibilityrequest.CoverageEligibilityRequest(jsondict)
        if "CoverageEligibilityResponse" == resource_type:
            from fhirclient.models import coverageeligibilityresponse
            return coverageeligibilityresponse.CoverageEligibilityResponse(jsondict)
        if "DetectedIssue" == resource_type:
            from fhirclient.models import detectedissue
            return detectedissue.DetectedIssue(jsondict)
        if "Device" == resource_type:
            from fhirclient.models import device
            return device.Device(jsondict)
        if "DeviceDefinition" == resource_type:
            from fhirclient.models import devicedefinition
            return devicedefinition.DeviceDefinition(jsondict)
        if "DeviceMetric" == resource_type:
            from fhirclient.models import devicemetric
            return devicemetric.DeviceMetric(jsondict)
        if "DeviceRequest" == resource_type:
            from fhirclient.models import devicerequest
            return devicerequest.DeviceRequest(jsondict)
        if "DeviceUseStatement" == resource_type:
            from fhirclient.models import deviceusestatement
            return deviceusestatement.DeviceUseStatement(jsondict)
        if "DiagnosticReport" == resource_type:
            from fhirclient.models import diagnosticreport
            return diagnosticreport.DiagnosticReport(jsondict)
        if "DocumentManifest" == resource_type:
            from fhirclient.models import documentmanifest
            return documentmanifest.DocumentManifest(jsondict)
        if "DocumentReference" == resource_type:
            from fhirclient.models import documentreference
            return documentreference.DocumentReference(jsondict)
        if "DomainResource" == resource_type:
            from fhirclient.models import domainresource
            return domainresource.DomainResource(jsondict)
        if "EffectEvidenceSynthesis" == resource_type:
            from fhirclient.models import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesis(jsondict)
        if "Encounter" == resource_type:
            from fhirclient.models import encounter
            return encounter.Encounter(jsondict)
        if "Endpoint" == resource_type:
            from fhirclient.models import endpoint
            return endpoint.Endpoint(jsondict)
        if "EnrollmentRequest" == resource_type:
            from fhirclient.models import enrollmentrequest
            return enrollmentrequest.EnrollmentRequest(jsondict)
        if "EnrollmentResponse" == resource_type:
            from fhirclient.models import enrollmentresponse
            return enrollmentresponse.EnrollmentResponse(jsondict)
        if "EpisodeOfCare" == resource_type:
            from fhirclient.models import episodeofcare
            return episodeofcare.EpisodeOfCare(jsondict)
        if "EventDefinition" == resource_type:
            from fhirclient.models import eventdefinition
            return eventdefinition.EventDefinition(jsondict)
        if "Evidence" == resource_type:
            from fhirclient.models import evidence
            return evidence.Evidence(jsondict)
        if "EvidenceVariable" == resource_type:
            from fhirclient.models import evidencevariable
            return evidencevariable.EvidenceVariable(jsondict)
        if "ExampleScenario" == resource_type:
            from fhirclient.models import examplescenario
            return examplescenario.ExampleScenario(jsondict)
        if "ExplanationOfBenefit" == resource_type:
            from fhirclient.models import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefit(jsondict)
        if "FamilyMemberHistory" == resource_type:
            from fhirclient.models import familymemberhistory
            return familymemberhistory.FamilyMemberHistory(jsondict)
        if "Flag" == resource_type:
            from fhirclient.models import flag
            return flag.Flag(jsondict)
        if "Goal" == resource_type:
            from fhirclient.models import goal
            return goal.Goal(jsondict)
        if "GraphDefinition" == resource_type:
            from fhirclient.models import graphdefinition
            return graphdefinition.GraphDefinition(jsondict)
        if "Group" == resource_type:
            from fhirclient.models import group
            return group.Group(jsondict)
        if "GuidanceResponse" == resource_type:
            from fhirclient.models import guidanceresponse
            return guidanceresponse.GuidanceResponse(jsondict)
        if "HealthcareService" == resource_type:
            from fhirclient.models import healthcareservice
            return healthcareservice.HealthcareService(jsondict)
        if "ImagingStudy" == resource_type:
            from fhirclient.models import imagingstudy
            return imagingstudy.ImagingStudy(jsondict)
        if "Immunization" == resource_type:
            from fhirclient.models import immunization
            return immunization.Immunization(jsondict)
        if "ImmunizationEvaluation" == resource_type:
            from fhirclient.models import immunizationevaluation
            return immunizationevaluation.ImmunizationEvaluation(jsondict)
        if "ImmunizationRecommendation" == resource_type:
            from fhirclient.models import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendation(jsondict)
        if "ImplementationGuide" == resource_type:
            from fhirclient.models import implementationguide
            return implementationguide.ImplementationGuide(jsondict)
        if "InsurancePlan" == resource_type:
            from fhirclient.models import insuranceplan
            return insuranceplan.InsurancePlan(jsondict)
        if "Invoice" == resource_type:
            from fhirclient.models import invoice
            return invoice.Invoice(jsondict)
        if "Library" == resource_type:
            from fhirclient.models import library
            return library.Library(jsondict)
        if "Linkage" == resource_type:
            from fhirclient.models import linkage
            return linkage.Linkage(jsondict)
        if "List" == resource_type:
            from fhirclient.models import list
            return list.List(jsondict)
        if "Location" == resource_type:
            from fhirclient.models import location
            return location.Location(jsondict)
        if "Measure" == resource_type:
            from fhirclient.models import measure
            return measure.Measure(jsondict)
        if "MeasureReport" == resource_type:
            from fhirclient.models import measurereport
            return measurereport.MeasureReport(jsondict)
        if "Media" == resource_type:
            from fhirclient.models import media
            return media.Media(jsondict)
        if "Medication" == resource_type:
            from fhirclient.models import medication
            return medication.Medication(jsondict)
        if "MedicationAdministration" == resource_type:
            from fhirclient.models import medicationadministration
            return medicationadministration.MedicationAdministration(jsondict)
        if "MedicationDispense" == resource_type:
            from fhirclient.models import medicationdispense
            return medicationdispense.MedicationDispense(jsondict)
        if "MedicationKnowledge" == resource_type:
            from fhirclient.models import medicationknowledge
            return medicationknowledge.MedicationKnowledge(jsondict)
        if "MedicationRequest" == resource_type:
            from fhirclient.models import medicationrequest
            return medicationrequest.MedicationRequest(jsondict)
        if "MedicationStatement" == resource_type:
            from fhirclient.models import medicationstatement
            return medicationstatement.MedicationStatement(jsondict)
        if "MedicinalProduct" == resource_type:
            from fhirclient.models import medicinalproduct
            return medicinalproduct.MedicinalProduct(jsondict)
        if "MedicinalProductAuthorization" == resource_type:
            from fhirclient.models import medicinalproductauthorization
            return medicinalproductauthorization.MedicinalProductAuthorization(jsondict)
        if "MedicinalProductContraindication" == resource_type:
            from fhirclient.models import medicinalproductcontraindication
            return medicinalproductcontraindication.MedicinalProductContraindication(jsondict)
        if "MedicinalProductIndication" == resource_type:
            from fhirclient.models import medicinalproductindication
            return medicinalproductindication.MedicinalProductIndication(jsondict)
        if "MedicinalProductIngredient" == resource_type:
            from fhirclient.models import medicinalproductingredient
            return medicinalproductingredient.MedicinalProductIngredient(jsondict)
        if "MedicinalProductInteraction" == resource_type:
            from fhirclient.models import medicinalproductinteraction
            return medicinalproductinteraction.MedicinalProductInteraction(jsondict)
        if "MedicinalProductManufactured" == resource_type:
            from fhirclient.models import medicinalproductmanufactured
            return medicinalproductmanufactured.MedicinalProductManufactured(jsondict)
        if "MedicinalProductPackaged" == resource_type:
            from fhirclient.models import medicinalproductpackaged
            return medicinalproductpackaged.MedicinalProductPackaged(jsondict)
        if "MedicinalProductPharmaceutical" == resource_type:
            from fhirclient.models import medicinalproductpharmaceutical
            return medicinalproductpharmaceutical.MedicinalProductPharmaceutical(jsondict)
        if "MedicinalProductUndesirableEffect" == resource_type:
            from fhirclient.models import medicinalproductundesirableeffect
            return medicinalproductundesirableeffect.MedicinalProductUndesirableEffect(jsondict)
        if "MessageDefinition" == resource_type:
            from fhirclient.models import messagedefinition
            return messagedefinition.MessageDefinition(jsondict)
        if "MessageHeader" == resource_type:
            from fhirclient.models import messageheader
            return messageheader.MessageHeader(jsondict)
        if "MolecularSequence" == resource_type:
            from fhirclient.models import molecularsequence
            return molecularsequence.MolecularSequence(jsondict)
        if "NamingSystem" == resource_type:
            from fhirclient.models import namingsystem
            return namingsystem.NamingSystem(jsondict)
        if "NutritionOrder" == resource_type:
            from fhirclient.models import nutritionorder
            return nutritionorder.NutritionOrder(jsondict)
        if "Observation" == resource_type:
            from fhirclient.models import observation
            return observation.Observation(jsondict)
        if "ObservationDefinition" == resource_type:
            from fhirclient.models import observationdefinition
            return observationdefinition.ObservationDefinition(jsondict)
        if "OperationDefinition" == resource_type:
            from fhirclient.models import operationdefinition
            return operationdefinition.OperationDefinition(jsondict)
        if "OperationOutcome" == resource_type:
            from fhirclient.models import operationoutcome
            return operationoutcome.OperationOutcome(jsondict)
        if "Organization" == resource_type:
            from fhirclient.models import organization
            return organization.Organization(jsondict)
        if "OrganizationAffiliation" == resource_type:
            from fhirclient.models import organizationaffiliation
            return organizationaffiliation.OrganizationAffiliation(jsondict)
        if "Parameters" == resource_type:
            from fhirclient.models import parameters
            return parameters.Parameters(jsondict)
        if "Patient" == resource_type:
            from fhirclient.models import patient
            return patient.Patient(jsondict)
        if "PaymentNotice" == resource_type:
            from fhirclient.models import paymentnotice
            return paymentnotice.PaymentNotice(jsondict)
        if "PaymentReconciliation" == resource_type:
            from fhirclient.models import paymentreconciliation
            return paymentreconciliation.PaymentReconciliation(jsondict)
        if "Person" == resource_type:
            from fhirclient.models import person
            return person.Person(jsondict)
        if "PlanDefinition" == resource_type:
            from fhirclient.models import plandefinition
            return plandefinition.PlanDefinition(jsondict)
        if "Practitioner" == resource_type:
            from fhirclient.models import practitioner
            return practitioner.Practitioner(jsondict)
        if "PractitionerRole" == resource_type:
            from fhirclient.models import practitionerrole
            return practitionerrole.PractitionerRole(jsondict)
        if "Procedure" == resource_type:
            from fhirclient.models import procedure
            return procedure.Procedure(jsondict)
        if "Provenance" == resource_type:
            from fhirclient.models import provenance
            return provenance.Provenance(jsondict)
        if "Questionnaire" == resource_type:
            from fhirclient.models import questionnaire
            return questionnaire.Questionnaire(jsondict)
        if "QuestionnaireResponse" == resource_type:
            from fhirclient.models import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponse(jsondict)
        if "RelatedPerson" == resource_type:
            from fhirclient.models import relatedperson
            return relatedperson.RelatedPerson(jsondict)
        if "RequestGroup" == resource_type:
            from fhirclient.models import requestgroup
            return requestgroup.RequestGroup(jsondict)
        if "ResearchDefinition" == resource_type:
            from fhirclient.models import researchdefinition
            return researchdefinition.ResearchDefinition(jsondict)
        if "ResearchElementDefinition" == resource_type:
            from fhirclient.models import researchelementdefinition
            return researchelementdefinition.ResearchElementDefinition(jsondict)
        if "ResearchStudy" == resource_type:
            from fhirclient.models import researchstudy
            return researchstudy.ResearchStudy(jsondict)
        if "ResearchSubject" == resource_type:
            from fhirclient.models import researchsubject
            return researchsubject.ResearchSubject(jsondict)
        if "Resource" == resource_type:
            from fhirclient.models import resource
            return resource.Resource(jsondict)
        if "RiskAssessment" == resource_type:
            from fhirclient.models import riskassessment
            return riskassessment.RiskAssessment(jsondict)
        if "RiskEvidenceSynthesis" == resource_type:
            from fhirclient.models import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesis(jsondict)
        if "Schedule" == resource_type:
            from fhirclient.models import schedule
            return schedule.Schedule(jsondict)
        if "SearchParameter" == resource_type:
            from fhirclient.models import searchparameter
            return searchparameter.SearchParameter(jsondict)
        if "ServiceRequest" == resource_type:
            from fhirclient.models import servicerequest
            return servicerequest.ServiceRequest(jsondict)
        if "Slot" == resource_type:
            from fhirclient.models import slot
            return slot.Slot(jsondict)
        if "Specimen" == resource_type:
            from fhirclient.models import specimen
            return specimen.Specimen(jsondict)
        if "SpecimenDefinition" == resource_type:
            from fhirclient.models import specimendefinition
            return specimendefinition.SpecimenDefinition(jsondict)
        if "StructureDefinition" == resource_type:
            from fhirclient.models import structuredefinition
            return structuredefinition.StructureDefinition(jsondict)
        if "StructureMap" == resource_type:
            from fhirclient.models import structuremap
            return structuremap.StructureMap(jsondict)
        if "Subscription" == resource_type:
            from fhirclient.models import subscription
            return subscription.Subscription(jsondict)
        if "Substance" == resource_type:
            from fhirclient.models import substance
            return substance.Substance(jsondict)
        if "SubstanceNucleicAcid" == resource_type:
            from fhirclient.models import substancenucleicacid
            return substancenucleicacid.SubstanceNucleicAcid(jsondict)
        if "SubstancePolymer" == resource_type:
            from fhirclient.models import substancepolymer
            return substancepolymer.SubstancePolymer(jsondict)
        if "SubstanceProtein" == resource_type:
            from fhirclient.models import substanceprotein
            return substanceprotein.SubstanceProtein(jsondict)
        if "SubstanceReferenceInformation" == resource_type:
            from fhirclient.models import substancereferenceinformation
            return substancereferenceinformation.SubstanceReferenceInformation(jsondict)
        if "SubstanceSourceMaterial" == resource_type:
            from fhirclient.models import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterial(jsondict)
        if "SubstanceSpecification" == resource_type:
            from fhirclient.models import substancespecification
            return substancespecification.SubstanceSpecification(jsondict)
        if "SupplyDelivery" == resource_type:
            from fhirclient.models import supplydelivery
            return supplydelivery.SupplyDelivery(jsondict)
        if "SupplyRequest" == resource_type:
            from fhirclient.models import supplyrequest
            return supplyrequest.SupplyRequest(jsondict)
        if "Task" == resource_type:
            from fhirclient.models import task
            return task.Task(jsondict)
        if "TerminologyCapabilities" == resource_type:
            from fhirclient.models import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilities(jsondict)
        if "TestReport" == resource_type:
            from fhirclient.models import testreport
            return testreport.TestReport(jsondict)
        if "TestScript" == resource_type:
            from fhirclient.models import testscript
            return testscript.TestScript(jsondict)
        if "ValueSet" == resource_type:
            from fhirclient.models import valueset
            return valueset.ValueSet(jsondict)
        if "VerificationResult" == resource_type:
            from fhirclient.models import verificationresult
            return verificationresult.VerificationResult(jsondict)
        if "VisionPrescription" == resource_type:
            from fhirclient.models import visionprescription
            return visionprescription.VisionPrescription(jsondict)
        from . import element
        return element.Element(jsondict)
