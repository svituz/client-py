import logging
import re

import isodate
import six
from isodate import ISO8601Error

logger = logging.getLogger(__name__)


class FHIRAbstractDatatype(object):
    def __init__(self, value):
        self.value = value
        self.validate_value()

    @classmethod
    def with_json(cls, jsonobj):
        if isinstance(jsonobj, six.string_types) or isinstance(jsonobj, (int, float, bool)):
            return cls(jsonobj)

        if isinstance(jsonobj, list):
            return [cls(jsonval) for jsonval in jsonobj]

        raise TypeError("`cls.with_json()` only takes string or list of strings, but you provided {}"
                        .format(type(jsonobj)))

    @classmethod
    def with_json_and_owner(cls, jsonobj, owner):
        return cls.with_json(jsonobj)

    def as_json(self):
        return self.value

    def validate_value(self):
        if hasattr(self, 'regex'):
            match = re.fullmatch(self.regex, self.value)
            if match is None:
                raise ValueError(f'Invalid value. Should match {self.regex}')


class FHIRString(FHIRAbstractDatatype):
    def __init__(self, value):
        self.regex = re.compile(r'[ \r\n\t\S]{1,1048576}')
        super(FHIRString, self).__init__(value)


class FHIRUri(FHIRAbstractDatatype):
    def __init__(self, value):
        self.regex = re.compile(r'\S*')
        super(FHIRUri, self).__init__(value)


class FHIRUrl(FHIRAbstractDatatype):
    def __init__(self, value):
        # taken from Django and changed the protocol part
        self.regex = re.compile(
            r'^(?:[a-z]+)s?://'  # set any possible protocol since FHIR spec says it can be lot of protocols  
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        super(FHIRUrl, self).__init__(value)


FHIRCanonical = FHIRUri


class FHIRBase64Binary(FHIRAbstractDatatype):
    def __init__(self, value):
        self.regex = re.compile(r'(\s*([0-9a-zA-Z\+\=]){4}\s*)+')
        super(FHIRBase64Binary, self).__init__(value)


class BaseFHIRTime(FHIRAbstractDatatype):
    def __init__(self, value):
        self.date = None
        self.origval = value
        super(BaseFHIRTime, self).__init__(value)
    
    def validate_value(self):
        # check the value is a string
        if self.value is not None:
            if not isinstance(self.value, six.string_types):
                raise TypeError('Expecting string when initializing {}, but got {}'
                                .format(type(self), type(self.value)))

        # check the value matches the regex
        try:
            super(BaseFHIRTime, self).validate_value()
        except ValueError:
            raise ValueError(self.error_message)

        try:
            # keeping self.date for backward compatibility
            self.value = self.date = self.parser(self.value)
        except ISO8601Error as e:
            logger.warning('Failed to initialize FHIRDate from \'{}\': {}'
                           .format(self.value, e))
            raise ValueError(self.error_message)

    @property
    def isostring(self):
        if self.value is None:
            return None
        return self.renderer(self.value)

    def as_json(self):
        if self.origval is not None:
            return self.origval
        return self.isostring

    def __setattr__(self, prop, value):
        if 'date' == prop:
            self.origval = None
        object.__setattr__(self, prop, value)


class FHIRInstant(BaseFHIRTime):
    def __init__(self, value):
        self.regex = r'([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]+)?(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))'
        self.parser = isodate.parse_datetime
        self.renderer = isodate.datetime_isoformat
        self.error_message = 'Invalid value. It must be an ISO8601 datetetime with  ' \
                             'at least precision to seconds and time zone'
        super(FHIRInstant, self).__init__(value)


class FHIRDate(BaseFHIRTime):
    def __init__(self, value):
        self.regex = r'([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1]))?)?'
        self.parser = isodate.parse_date
        self.renderer = isodate.date_isoformat
        self.error_message = 'Invalid value. It must be an ISO8601 date'
        super(FHIRDate, self).__init__(value)


class FHIRDateTime(BaseFHIRTime):
    def __init__(self, value):
        self.regex = r'([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]+)?(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?'
        self.parser = isodate.parse_datetime
        self.renderer = isodate.datetime_isoformat
        self.error_message = 'Invalid value. It must be an ISO8601 datetime with time zone'
        super(FHIRDateTime, self).__init__(value)


class FHIRTime(BaseFHIRTime):
    def __init__(self, value):
        self.regex = r'([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]+)?'
        self.parser = isodate.parse_time
        self.renderer = isodate.time_isoformat
        self.error_message = 'Invalid value. Should be an ISO8601 time with  ' \
                             'at least precision to seconds'
        super(FHIRTime, self).__init__(value)


class FHIRCode(FHIRAbstractDatatype):
    def __init__(self, value):
        # TODO: checf if it is possible to add the valueset
        self.regex = re.compile(r'[^\s]+(\s[^\s]+)*')
        super(FHIRCode, self).__init__(value)


class FHIROid(FHIRAbstractDatatype):
    def __init__(self, value):
        self.regex = r'urn:oid:[0-2](\.(0|[1-9][0-9]*))+'
        super(FHIROid, self).__init__(value)


class FHIRId(FHIRAbstractDatatype):
    def __init__(self, value):
        self.regex = re.compile(r'([A-Za-z0-9\-\.]{1,64})')
        super(FHIRId, self).__init__(value)


class FHIRMarkdown(FHIRAbstractDatatype):
    def __init__(self, value):
        self.regex = r'\s*(\S|\s)*'
        super(FHIRMarkdown, self).__init__(value)


FHIRUuid = FHIRUri


class FHIRUnsignedInt(FHIRAbstractDatatype):
    def __init__(self, value):
        super(FHIRUnsignedInt, self).__init__(value)

    def validate_value(self):
        if self.value < 0:
            raise ValueError('Invalid Value. It must be greater than 0')


class FHIRPositiveInt(FHIRAbstractDatatype):
    def __init__(self, value):
        super(FHIRPositiveInt, self).__init__(value)

    def validate_value(self):
        if self.value < 1:
            raise ValueError('Invalid Value. It must be greater than 1')
