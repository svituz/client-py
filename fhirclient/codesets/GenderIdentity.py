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

class GenderIdentity(object):
    """ This example value set defines a set of codes that can be used to indicate a patient's gender identity.
    URL: http://hl7.org/fhir/gender-identity
    """
    # the patient identifies as transgender male-to-female
    transgenderFemale = "transgender-female"
    # the patient identifies as transgender female-to-male
    transgenderMale = "transgender-male"
    # the patient identifies with neither/both female and male
    nonBinary = "non-binary"
    # the patient identifies as male
    male = "male"
    # the patient identifies as female
    female = "female"
    # other gender identity
    other = "other"
    # the patient does not wish to disclose his gender identity
    nonDisclose = "non-disclose"