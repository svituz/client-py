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

class DataType(object):
    """ A version specific list of the data types defined by the FHIR specification for use as an element  type (any of the FHIR
defined data types).
    URL: http://hl7.org/fhir/data-types
    """
    # An address expressed using postal conventions (as opposed to GPS or other location definition formats).  This
    # data type may be used to convey addresses for use in delivering mail as well as for visiting locations which
    # might not be valid for mail delivery.  There are a variety of postal address formats defined around the world.
    ADDRESS = "Address"
    # A duration of time during which an organism (or a process) has existed.
    AGE = "Age"
    # A  text note which also  contains information about who made the statement and when.
    ANNOTATION = "Annotation"
    # For referring to data content defined in other formats.
    ATTACHMENT = "Attachment"
    # Base definition for all elements that are defined inside a resource - but not those in a data type.
    BACKBONEELEMENT = "BackboneElement"
    # A concept that may be defined by a formal reference to a terminology or ontology or may be provided by text.
    CODEABLECONCEPT = "CodeableConcept"
    # A reference to a code defined by a terminology system.
    CODING = "Coding"
    # Specifies contact information for a person or organization.
    CONTACTDETAIL = "ContactDetail"
    # Details for all kinds of technology mediated contact points for a person or organization, including telephone,
    # email, etc.
    CONTACTPOINT = "ContactPoint"
    # A contributor to the content of a knowledge asset, including authors, editors, reviewers, and endorsers.
    CONTRIBUTOR = "Contributor"
    # A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts
    # that are not precisely quantified, including amounts involving arbitrary units and floating currencies.
    COUNT = "Count"
    # Describes a required data item for evaluation in terms of the type of data, and optional code or date-based
    # filters of the data.
    DATAREQUIREMENT = "DataRequirement"
    # A length - a value with a unit that is a physical distance.
    DISTANCE = "Distance"
    # Indicates how the medication is/was taken or should be taken by the patient.
    DOSAGE = "Dosage"
    # A length of time.
    DURATION = "Duration"
    # Base definition for all elements in a resource.
    ELEMENT = "Element"
    # Captures constraints on each element within the resource, profile, or extension.
    ELEMENTDEFINITION = "ElementDefinition"
    # A expression that is evaluated in a specified context and returns a value. The context of use of the expression
    # must specify the context in which the expression is evaluated, and how the result of the expression is used.
    EXPRESSION = "Expression"
    # Optional Extension Element - found in all resources.
    EXTENSION = "Extension"
    # A human's name with the ability to identify parts and usage.
    HUMANNAME = "HumanName"
    # An identifier - identifies some entity uniquely and unambiguously. Typically this is used for business
    # identifiers.
    IDENTIFIER = "Identifier"
    # The marketing status describes the date when a medicinal product is actually put on the market or the date as of
    # which it is no longer available.
    MARKETINGSTATUS = "MarketingStatus"
    # The metadata about a resource. This is content in the resource that is maintained by the infrastructure. Changes
    # to the content might not always be associated with version changes to the resource.
    META = "Meta"
    # An amount of economic utility in some recognized currency.
    MONEY = "Money"
    # moneyQuantity
    MONEYQUANTITY = "MoneyQuantity"
    # A human-readable summary of the resource conveying the essential clinical and business information for the
    # resource.
    NARRATIVE = "Narrative"
    # The parameters to the module. This collection specifies both the input and output parameters. Input parameters
    # are provided by the caller as part of the $evaluate operation. Output parameters are included in the
    # GuidanceResponse.
    PARAMETERDEFINITION = "ParameterDefinition"
    # A time period defined by a start and end date and optionally time.
    PERIOD = "Period"
    # A populatioof people with some set of grouping criteria.
    POPULATION = "Population"
    # The marketing status describes the date when a medicinal product is actually put on the market or the date as of
    # which it is no longer available.
    PRODCHARACTERISTIC = "ProdCharacteristic"
    # The shelf-life and storage information for a medicinal product item or container can be described using this
    # class.
    PRODUCTSHELFLIFE = "ProductShelfLife"
    # A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts
    # that are not precisely quantified, including amounts involving arbitrary units and floating currencies.
    QUANTITY = "Quantity"
    # A set of ordered Quantities defined by a low and high limit.
    RANGE = "Range"
    # A relationship of two Quantity values - expressed as a numerator and a denominator.
    RATIO = "Ratio"
    # A reference from one resource to another.
    REFERENCE = "Reference"
    # Related artifacts such as additional documentation, justification, or bibliographic references.
    RELATEDARTIFACT = "RelatedArtifact"
    # A series of measurements taken by a device, with upper and lower limits. There may be more than one dimension in
    # the data.
    SAMPLEDDATA = "SampledData"
    # A signature along with supporting context. The signature may be a digital signature that is cryptographic in
    # nature, or some other signature acceptable to the domain. This other signature may be as simple as a graphical
    # image representing a hand-written signature, or a signature ceremony Different signature approaches have
    # different utilities.
    SIGNATURE = "Signature"
    # simpleQuantity
    SIMPLEQUANTITY = "SimpleQuantity"
    # Chemical substances are a single substance type whose primary defining element is the molecular structure.
    # Chemical substances shall be defined on the basis of their complete covalent molecular structure; the presence
    # of a salt (counter-ion) and/or solvates (water, alcohols) is also captured. Purity, grade, physical form or
    # particle size are not taken into account in the definition of a chemical substance or in the assignment of a
    # Substance ID.
    SUBSTANCEAMOUNT = "SubstanceAmount"
    # Specifies an event that may occur multiple times. Timing schedules are used to record when things are planned,
    # expected or requested to occur. The most common usage is in dosage instructions for medications. They are also
    # used when planning care of various kinds, and may be used for reporting the schedule to which past regular
    # activities were carried out.
    TIMING = "Timing"
    # A description of a triggering event. Triggering events can be named events, data events, or periodic, as
    # determined by the type element.
    TRIGGERDEFINITION = "TriggerDefinition"
    # Specifies clinical/business/etc. metadata that can be used to retrieve, index and/or categorize an artifact.
    # This metadata can either be specific to the applicable population (e.g., age category, DRG) or the specific
    # context of care (e.g., venue, care setting, provider of care).
    USAGECONTEXT = "UsageContext"
    # A stream of bytes
    BASE64BINARY = "base64Binary"
    # Value of "true" or "false"
    BOOLEAN = "boolean"
    # A URI that is a reference to a canonical URL on a FHIR resource
    CANONICAL = "canonical"
    # A string which has at least one character and no leading or trailing whitespace and where there is no whitespace
    # other than single spaces in the contents
    CODE = "code"
    # A date or partial date (e.g. just year or year + month). There is no time zone. The format is a union of the
    # schema types gYear, gYearMonth and date.  Dates SHALL be valid dates.
    DATE = "date"
    # A date, date-time or partial date (e.g. just year or year + month).  If hours and minutes are specified, a time
    # zone SHALL be populated. The format is a union of the schema types gYear, gYearMonth, date and dateTime. Seconds
    # must be provided due to schema type constraints but may be zero-filled and may be ignored.                 Dates
    # SHALL be valid dates.
    DATETIME = "dateTime"
    # A rational number with implicit precision
    DECIMAL = "decimal"
    # Any combination of letters, numerals, "-" and ".", with a length limit of 64 characters.  (This might be an
    # integer, an unprefixed OID, UUID or any other identifier pattern that meets these constraints.)  Ids are case-
    # insensitive.
    ID = "id"
    # An instant in time - known at least to the second
    INSTANT = "instant"
    # A whole number
    INTEGER = "integer"
    # A string that may contain Github Flavored Markdown syntax for optional processing by a mark down presentation
    # engine
    MARKDOWN = "markdown"
    # An OID represented as a URI
    OID = "oid"
    # An integer with a value that is positive (e.g. >0)
    POSITIVEINT = "positiveInt"
    # A sequence of Unicode characters
    STRING = "string"
    # A time during the day, with no date specified
    TIME = "time"
    # An integer with a value that is not negative (e.g. >= 0)
    UNSIGNEDINT = "unsignedInt"
    # String of characters used to identify a name or a resource
    URI = "uri"
    # A URI that is a literal reference
    URL = "url"
    # A UUID, represented as a URI
    UUID = "uuid"
    # XHTML format, as defined by W3C, but restricted usage (mainly, no active content)
    XHTML = "xhtml"

    allowed_values = [ADDRESS, AGE, ANNOTATION, ATTACHMENT, BACKBONEELEMENT, CODEABLECONCEPT, CODING, CONTACTDETAIL, CONTACTPOINT, CONTRIBUTOR, COUNT, DATAREQUIREMENT, DISTANCE, DOSAGE, DURATION, ELEMENT, ELEMENTDEFINITION, EXPRESSION, EXTENSION, HUMANNAME, IDENTIFIER, MARKETINGSTATUS, META, MONEY, MONEYQUANTITY, NARRATIVE, PARAMETERDEFINITION, PERIOD, POPULATION, PRODCHARACTERISTIC, PRODUCTSHELFLIFE, QUANTITY, RANGE, RATIO, REFERENCE, RELATEDARTIFACT, SAMPLEDDATA, SIGNATURE, SIMPLEQUANTITY, SUBSTANCEAMOUNT, TIMING, TRIGGERDEFINITION, USAGECONTEXT, BASE64BINARY, BOOLEAN, CANONICAL, CODE, DATE, DATETIME, DECIMAL, ID, INSTANT, INTEGER, MARKDOWN, OID, POSITIVEINT, STRING, TIME, UNSIGNEDINT, URI, URL, UUID, XHTML]