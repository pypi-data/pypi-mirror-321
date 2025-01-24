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

class AlphaIdentitiesResponse(object):
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
        'unix_timestamp': 'int',
        'am_identity_name_list': 'list[str]'
    }

    attribute_map = {
        'unix_timestamp': 'unix_timestamp',
        'am_identity_name_list': 'am_identity_name_list'
    }

    def __init__(self, unix_timestamp=None, am_identity_name_list=None):  # noqa: E501
        """AlphaIdentitiesResponse - a model defined in Swagger"""  # noqa: E501
        self._unix_timestamp = None
        self._am_identity_name_list = None
        self.discriminator = None
        self.unix_timestamp = unix_timestamp
        self.am_identity_name_list = am_identity_name_list

    @property
    def unix_timestamp(self):
        """Gets the unix_timestamp of this AlphaIdentitiesResponse.  # noqa: E501


        :return: The unix_timestamp of this AlphaIdentitiesResponse.  # noqa: E501
        :rtype: int
        """
        return self._unix_timestamp

    @unix_timestamp.setter
    def unix_timestamp(self, unix_timestamp):
        """Sets the unix_timestamp of this AlphaIdentitiesResponse.


        :param unix_timestamp: The unix_timestamp of this AlphaIdentitiesResponse.  # noqa: E501
        :type: int
        """
        if unix_timestamp is None:
            raise ValueError("Invalid value for `unix_timestamp`, must not be `None`")  # noqa: E501

        self._unix_timestamp = unix_timestamp

    @property
    def am_identity_name_list(self):
        """Gets the am_identity_name_list of this AlphaIdentitiesResponse.  # noqa: E501


        :return: The am_identity_name_list of this AlphaIdentitiesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._am_identity_name_list

    @am_identity_name_list.setter
    def am_identity_name_list(self, am_identity_name_list):
        """Sets the am_identity_name_list of this AlphaIdentitiesResponse.


        :param am_identity_name_list: The am_identity_name_list of this AlphaIdentitiesResponse.  # noqa: E501
        :type: list[str]
        """
        if am_identity_name_list is None:
            raise ValueError("Invalid value for `am_identity_name_list`, must not be `None`")  # noqa: E501

        self._am_identity_name_list = am_identity_name_list

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
        if issubclass(AlphaIdentitiesResponse, dict):
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
        if not isinstance(other, AlphaIdentitiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
