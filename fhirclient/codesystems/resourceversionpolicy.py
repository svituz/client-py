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

class ResourceVersionPolicy(object):
    """ How the system supports versioning for a resource.
    URL: http://hl7.org/fhir/versioning-policy
    ValueSet: http://hl7.org/fhir/ValueSet/versioning-policy
    """
    # VersionId meta-property is not supported (server) or used (client).
    NOVERSION = "no-version"
    # VersionId meta-property is supported (server) or used (client).
    VERSIONED = "versioned"
    # VersionId must be correct for updates (server) or will be specified (If-match header) for updates (client).
    VERSIONEDUPDATE = "versioned-update"

    allowed_values = [NOVERSION, VERSIONED, VERSIONEDUPDATE]