# coding: utf-8

"""
    FINTER API

    ## Finter API Document 1. Domain   - production      - https://api.finter.quantit.io/   - staging      - https://staging.api.finter.quantit.io/  2. Authorization <br><br/>(1) 토큰 발급<br/>curl -X POST https://api.finter.quantit.io/login -d {'username': '{finter_user_id}', 'password': '{finter_user_password}'<br> (2) username, password 로그인 (swagger ui 이용 시)<br/>  # noqa: E501

    OpenAPI spec version: 0.298
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BaseFlexibleFundGetPortfolio(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'start': 'str',
        'end': 'str',
        'exchange': 'str',
        'universe': 'str',
        'instrument_type': 'str',
        'freq': 'str',
        'position_type': 'str',
        'portfolio_set': 'list[str]',
        'identity_name': 'str'
    }

    attribute_map = {
        'start': 'start',
        'end': 'end',
        'exchange': 'exchange',
        'universe': 'universe',
        'instrument_type': 'instrument_type',
        'freq': 'freq',
        'position_type': 'position_type',
        'portfolio_set': 'portfolio_set',
        'identity_name': 'identity_name'
    }

    def __init__(self, start=None, end=None, exchange=None, universe=None, instrument_type=None, freq=None, position_type=None, portfolio_set=None, identity_name=None):  # noqa: E501
        """BaseFlexibleFundGetPortfolio - a model defined in Swagger"""  # noqa: E501
        self._start = None
        self._end = None
        self._exchange = None
        self._universe = None
        self._instrument_type = None
        self._freq = None
        self._position_type = None
        self._portfolio_set = None
        self._identity_name = None
        self.discriminator = None
        self.start = start
        self.end = end
        self.exchange = exchange
        self.universe = universe
        self.instrument_type = instrument_type
        self.freq = freq
        self.position_type = position_type
        self.portfolio_set = portfolio_set
        self.identity_name = identity_name

    @property
    def start(self):
        """Gets the start of this BaseFlexibleFundGetPortfolio.  # noqa: E501


        :return: The start of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this BaseFlexibleFundGetPortfolio.


        :param start: The start of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :type: str
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def end(self):
        """Gets the end of this BaseFlexibleFundGetPortfolio.  # noqa: E501


        :return: The end of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this BaseFlexibleFundGetPortfolio.


        :param end: The end of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :type: str
        """
        if end is None:
            raise ValueError("Invalid value for `end`, must not be `None`")  # noqa: E501

        self._end = end

    @property
    def exchange(self):
        """Gets the exchange of this BaseFlexibleFundGetPortfolio.  # noqa: E501


        :return: The exchange of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this BaseFlexibleFundGetPortfolio.


        :param exchange: The exchange of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :type: str
        """
        if exchange is None:
            raise ValueError("Invalid value for `exchange`, must not be `None`")  # noqa: E501

        self._exchange = exchange

    @property
    def universe(self):
        """Gets the universe of this BaseFlexibleFundGetPortfolio.  # noqa: E501


        :return: The universe of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._universe

    @universe.setter
    def universe(self, universe):
        """Sets the universe of this BaseFlexibleFundGetPortfolio.


        :param universe: The universe of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :type: str
        """
        if universe is None:
            raise ValueError("Invalid value for `universe`, must not be `None`")  # noqa: E501

        self._universe = universe

    @property
    def instrument_type(self):
        """Gets the instrument_type of this BaseFlexibleFundGetPortfolio.  # noqa: E501


        :return: The instrument_type of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this BaseFlexibleFundGetPortfolio.


        :param instrument_type: The instrument_type of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :type: str
        """
        if instrument_type is None:
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501

        self._instrument_type = instrument_type

    @property
    def freq(self):
        """Gets the freq of this BaseFlexibleFundGetPortfolio.  # noqa: E501


        :return: The freq of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._freq

    @freq.setter
    def freq(self, freq):
        """Sets the freq of this BaseFlexibleFundGetPortfolio.


        :param freq: The freq of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :type: str
        """
        if freq is None:
            raise ValueError("Invalid value for `freq`, must not be `None`")  # noqa: E501

        self._freq = freq

    @property
    def position_type(self):
        """Gets the position_type of this BaseFlexibleFundGetPortfolio.  # noqa: E501


        :return: The position_type of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._position_type

    @position_type.setter
    def position_type(self, position_type):
        """Sets the position_type of this BaseFlexibleFundGetPortfolio.


        :param position_type: The position_type of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :type: str
        """
        if position_type is None:
            raise ValueError("Invalid value for `position_type`, must not be `None`")  # noqa: E501

        self._position_type = position_type

    @property
    def portfolio_set(self):
        """Gets the portfolio_set of this BaseFlexibleFundGetPortfolio.  # noqa: E501


        :return: The portfolio_set of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :rtype: list[str]
        """
        return self._portfolio_set

    @portfolio_set.setter
    def portfolio_set(self, portfolio_set):
        """Sets the portfolio_set of this BaseFlexibleFundGetPortfolio.


        :param portfolio_set: The portfolio_set of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :type: list[str]
        """
        if portfolio_set is None:
            raise ValueError("Invalid value for `portfolio_set`, must not be `None`")  # noqa: E501

        self._portfolio_set = portfolio_set

    @property
    def identity_name(self):
        """Gets the identity_name of this BaseFlexibleFundGetPortfolio.  # noqa: E501


        :return: The identity_name of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._identity_name

    @identity_name.setter
    def identity_name(self, identity_name):
        """Sets the identity_name of this BaseFlexibleFundGetPortfolio.


        :param identity_name: The identity_name of this BaseFlexibleFundGetPortfolio.  # noqa: E501
        :type: str
        """
        if identity_name is None:
            raise ValueError("Invalid value for `identity_name`, must not be `None`")  # noqa: E501

        self._identity_name = identity_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BaseFlexibleFundGetPortfolio, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BaseFlexibleFundGetPortfolio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
