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

class EndpointConnectionType(object):
    """ This is an example value set defined by the FHIR project, that could be used to represent possible connection type
profile values.
    URL: http://terminology.hl7.org/CodeSystem/endpoint-connection-type
    ValueSet: http://hl7.org/fhir/ValueSet/endpoint-connection-type
    """
    # IHE Cross Community Patient Discovery Profile (XCPD) - http://wiki.ihe.net/index.php/Cross-
    # Community_Patient_Discovery
    IHEXCPD = "ihe-xcpd"
    # IHE Cross Community Access Profile (XCA) - http://wiki.ihe.net/index.php/Cross-Community_Access
    IHEXCA = "ihe-xca"
    # IHE Cross-Enterprise Document Reliable Exchange (XDR) - http://wiki.ihe.net/index.php/Cross-
    # enterprise_Document_Reliable_Interchange
    IHEXDR = "ihe-xdr"
    # IHE Cross-Enterprise Document Sharing (XDS) - http://wiki.ihe.net/index.php/Cross-Enterprise_Document_Sharing
    IHEXDS = "ihe-xds"
    # IHE Invoke Image Display (IID) - http://wiki.ihe.net/index.php/Invoke_Image_Display
    IHEIID = "ihe-iid"
    # DICOMweb RESTful Image Retrieve - http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_6.5.html
    DICOMWADORS = "dicom-wado-rs"
    # DICOMweb RESTful Image query - http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_6.7.html
    DICOMQIDORS = "dicom-qido-rs"
    # DICOMweb RESTful image sending and storage -
    # http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_6.6.html
    DICOMSTOWRS = "dicom-stow-rs"
    # DICOMweb Image Retrieve - http://dicom.nema.org/dicom/2013/output/chtml/part18/sect_6.3.html
    DICOMWADOURI = "dicom-wado-uri"
    # Interact with the server interface using FHIR's RESTful interface. For details on its version/capabilities you
    # should connect the value in Endpoint.address and retrieve the FHIR CapabilityStatement.
    HL7FHIRREST = "hl7-fhir-rest"
    # Use the servers FHIR Messaging interface. Details can be found on the messaging.html page in the FHIR
    # Specification. The FHIR server's base address is specified in the Endpoint.address property.
    HL7FHIRMSG = "hl7-fhir-msg"
    # HL7v2 messages over an LLP TCP connection
    HL7V2MLLP = "hl7v2-mllp"
    # Email delivery using a digital certificate to encrypt the content using the public key, receiver must have the
    # private key to decrypt the content
    SECUREEMAIL = "secure-email"
    # Direct Project information - http://wiki.directproject.org/
    DIRECTPROJECT = "direct-project"

    allowed_values = [IHEXCPD, IHEXCA, IHEXDR, IHEXDS, IHEIID, DICOMWADORS, DICOMQIDORS, DICOMSTOWRS, DICOMWADOURI, HL7FHIRREST, HL7FHIRMSG, HL7V2MLLP, SECUREEMAIL, DIRECTPROJECT]