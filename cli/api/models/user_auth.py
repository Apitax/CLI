# coding: utf-8

"""
    Apitax

    The API for the frontend of Apitax  # noqa: E501

    OpenAPI spec version: 2
    Contact: shawn.clake@nopatience.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserAuth(object):
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
        'username': 'str',
        'password': 'str',
        'api_token': 'str',
        'extra': 'object'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'api_token': 'api_token',
        'extra': 'extra'
    }

    def __init__(self, username=None, password=None, api_token=None, extra=None):  # noqa: E501
        """UserAuth - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._password = None
        self._api_token = None
        self._extra = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if api_token is not None:
            self.api_token = api_token
        if extra is not None:
            self.extra = extra

    @property
    def username(self):
        """Gets the username of this UserAuth.  # noqa: E501


        :return: The username of this UserAuth.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserAuth.


        :param username: The username of this UserAuth.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this UserAuth.  # noqa: E501


        :return: The password of this UserAuth.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserAuth.


        :param password: The password of this UserAuth.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def api_token(self):
        """Gets the api_token of this UserAuth.  # noqa: E501


        :return: The api_token of this UserAuth.  # noqa: E501
        :rtype: str
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """Sets the api_token of this UserAuth.


        :param api_token: The api_token of this UserAuth.  # noqa: E501
        :type: str
        """

        self._api_token = api_token

    @property
    def extra(self):
        """Gets the extra of this UserAuth.  # noqa: E501


        :return: The extra of this UserAuth.  # noqa: E501
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this UserAuth.


        :param extra: The extra of this UserAuth.  # noqa: E501
        :type: object
        """

        self._extra = extra

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other