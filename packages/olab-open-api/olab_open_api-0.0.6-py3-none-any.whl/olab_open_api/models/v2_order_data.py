# coding: utf-8

"""
    PredictionMarket

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from olab_open_api.configuration import Configuration


class V2OrderData(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'currency_address': 'str',
        'expiration': 'int',
        'filled': 'str',
        'mutil_title': 'str',
        'mutil_topic_id': 'int',
        'order_id': 'int',
        'outcome': 'str',
        'outcome_side': 'int',
        'price': 'str',
        'profit': 'str',
        'side': 'int',
        'status': 'int',
        'topic_id': 'int',
        'topic_title': 'str',
        'total_price': 'str',
        'trading_method': 'int',
        'trans_no': 'str'
    }

    attribute_map = {
        'currency_address': 'currencyAddress',
        'expiration': 'expiration',
        'filled': 'filled',
        'mutil_title': 'mutilTitle',
        'mutil_topic_id': 'mutilTopicId',
        'order_id': 'orderId',
        'outcome': 'outcome',
        'outcome_side': 'outcomeSide',
        'price': 'price',
        'profit': 'profit',
        'side': 'side',
        'status': 'status',
        'topic_id': 'topicId',
        'topic_title': 'topicTitle',
        'total_price': 'totalPrice',
        'trading_method': 'tradingMethod',
        'trans_no': 'transNo'
    }

    def __init__(self, currency_address=None, expiration=None, filled=None, mutil_title=None, mutil_topic_id=None, order_id=None, outcome=None, outcome_side=None, price=None, profit=None, side=None, status=None, topic_id=None, topic_title=None, total_price=None, trading_method=None, trans_no=None, local_vars_configuration=None):  # noqa: E501
        """V2OrderData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency_address = None
        self._expiration = None
        self._filled = None
        self._mutil_title = None
        self._mutil_topic_id = None
        self._order_id = None
        self._outcome = None
        self._outcome_side = None
        self._price = None
        self._profit = None
        self._side = None
        self._status = None
        self._topic_id = None
        self._topic_title = None
        self._total_price = None
        self._trading_method = None
        self._trans_no = None
        self.discriminator = None

        if currency_address is not None:
            self.currency_address = currency_address
        if expiration is not None:
            self.expiration = expiration
        if filled is not None:
            self.filled = filled
        if mutil_title is not None:
            self.mutil_title = mutil_title
        if mutil_topic_id is not None:
            self.mutil_topic_id = mutil_topic_id
        if order_id is not None:
            self.order_id = order_id
        if outcome is not None:
            self.outcome = outcome
        if outcome_side is not None:
            self.outcome_side = outcome_side
        if price is not None:
            self.price = price
        if profit is not None:
            self.profit = profit
        if side is not None:
            self.side = side
        if status is not None:
            self.status = status
        if topic_id is not None:
            self.topic_id = topic_id
        if topic_title is not None:
            self.topic_title = topic_title
        if total_price is not None:
            self.total_price = total_price
        if trading_method is not None:
            self.trading_method = trading_method
        if trans_no is not None:
            self.trans_no = trans_no

    @property
    def currency_address(self):
        """Gets the currency_address of this V2OrderData.  # noqa: E501


        :return: The currency_address of this V2OrderData.  # noqa: E501
        :rtype: str
        """
        return self._currency_address

    @currency_address.setter
    def currency_address(self, currency_address):
        """Sets the currency_address of this V2OrderData.


        :param currency_address: The currency_address of this V2OrderData.  # noqa: E501
        :type: str
        """

        self._currency_address = currency_address

    @property
    def expiration(self):
        """Gets the expiration of this V2OrderData.  # noqa: E501


        :return: The expiration of this V2OrderData.  # noqa: E501
        :rtype: int
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this V2OrderData.


        :param expiration: The expiration of this V2OrderData.  # noqa: E501
        :type: int
        """

        self._expiration = expiration

    @property
    def filled(self):
        """Gets the filled of this V2OrderData.  # noqa: E501


        :return: The filled of this V2OrderData.  # noqa: E501
        :rtype: str
        """
        return self._filled

    @filled.setter
    def filled(self, filled):
        """Sets the filled of this V2OrderData.


        :param filled: The filled of this V2OrderData.  # noqa: E501
        :type: str
        """

        self._filled = filled

    @property
    def mutil_title(self):
        """Gets the mutil_title of this V2OrderData.  # noqa: E501


        :return: The mutil_title of this V2OrderData.  # noqa: E501
        :rtype: str
        """
        return self._mutil_title

    @mutil_title.setter
    def mutil_title(self, mutil_title):
        """Sets the mutil_title of this V2OrderData.


        :param mutil_title: The mutil_title of this V2OrderData.  # noqa: E501
        :type: str
        """

        self._mutil_title = mutil_title

    @property
    def mutil_topic_id(self):
        """Gets the mutil_topic_id of this V2OrderData.  # noqa: E501


        :return: The mutil_topic_id of this V2OrderData.  # noqa: E501
        :rtype: int
        """
        return self._mutil_topic_id

    @mutil_topic_id.setter
    def mutil_topic_id(self, mutil_topic_id):
        """Sets the mutil_topic_id of this V2OrderData.


        :param mutil_topic_id: The mutil_topic_id of this V2OrderData.  # noqa: E501
        :type: int
        """

        self._mutil_topic_id = mutil_topic_id

    @property
    def order_id(self):
        """Gets the order_id of this V2OrderData.  # noqa: E501


        :return: The order_id of this V2OrderData.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this V2OrderData.


        :param order_id: The order_id of this V2OrderData.  # noqa: E501
        :type: int
        """

        self._order_id = order_id

    @property
    def outcome(self):
        """Gets the outcome of this V2OrderData.  # noqa: E501


        :return: The outcome of this V2OrderData.  # noqa: E501
        :rtype: str
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """Sets the outcome of this V2OrderData.


        :param outcome: The outcome of this V2OrderData.  # noqa: E501
        :type: str
        """

        self._outcome = outcome

    @property
    def outcome_side(self):
        """Gets the outcome_side of this V2OrderData.  # noqa: E501

        1 - yes, 2 - no  # noqa: E501

        :return: The outcome_side of this V2OrderData.  # noqa: E501
        :rtype: int
        """
        return self._outcome_side

    @outcome_side.setter
    def outcome_side(self, outcome_side):
        """Sets the outcome_side of this V2OrderData.

        1 - yes, 2 - no  # noqa: E501

        :param outcome_side: The outcome_side of this V2OrderData.  # noqa: E501
        :type: int
        """

        self._outcome_side = outcome_side

    @property
    def price(self):
        """Gets the price of this V2OrderData.  # noqa: E501


        :return: The price of this V2OrderData.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this V2OrderData.


        :param price: The price of this V2OrderData.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def profit(self):
        """Gets the profit of this V2OrderData.  # noqa: E501


        :return: The profit of this V2OrderData.  # noqa: E501
        :rtype: str
        """
        return self._profit

    @profit.setter
    def profit(self, profit):
        """Sets the profit of this V2OrderData.


        :param profit: The profit of this V2OrderData.  # noqa: E501
        :type: str
        """

        self._profit = profit

    @property
    def side(self):
        """Gets the side of this V2OrderData.  # noqa: E501

        1-for buy, 2-for sell  # noqa: E501

        :return: The side of this V2OrderData.  # noqa: E501
        :rtype: int
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this V2OrderData.

        1-for buy, 2-for sell  # noqa: E501

        :param side: The side of this V2OrderData.  # noqa: E501
        :type: int
        """

        self._side = side

    @property
    def status(self):
        """Gets the status of this V2OrderData.  # noqa: E501

        1-pending, 2-finished, 3-canceled, 4-expired  # noqa: E501

        :return: The status of this V2OrderData.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V2OrderData.

        1-pending, 2-finished, 3-canceled, 4-expired  # noqa: E501

        :param status: The status of this V2OrderData.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def topic_id(self):
        """Gets the topic_id of this V2OrderData.  # noqa: E501


        :return: The topic_id of this V2OrderData.  # noqa: E501
        :rtype: int
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """Sets the topic_id of this V2OrderData.


        :param topic_id: The topic_id of this V2OrderData.  # noqa: E501
        :type: int
        """

        self._topic_id = topic_id

    @property
    def topic_title(self):
        """Gets the topic_title of this V2OrderData.  # noqa: E501


        :return: The topic_title of this V2OrderData.  # noqa: E501
        :rtype: str
        """
        return self._topic_title

    @topic_title.setter
    def topic_title(self, topic_title):
        """Sets the topic_title of this V2OrderData.


        :param topic_title: The topic_title of this V2OrderData.  # noqa: E501
        :type: str
        """

        self._topic_title = topic_title

    @property
    def total_price(self):
        """Gets the total_price of this V2OrderData.  # noqa: E501


        :return: The total_price of this V2OrderData.  # noqa: E501
        :rtype: str
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """Sets the total_price of this V2OrderData.


        :param total_price: The total_price of this V2OrderData.  # noqa: E501
        :type: str
        """

        self._total_price = total_price

    @property
    def trading_method(self):
        """Gets the trading_method of this V2OrderData.  # noqa: E501

        买卖方式:1-市价,2-现价  # noqa: E501

        :return: The trading_method of this V2OrderData.  # noqa: E501
        :rtype: int
        """
        return self._trading_method

    @trading_method.setter
    def trading_method(self, trading_method):
        """Sets the trading_method of this V2OrderData.

        买卖方式:1-市价,2-现价  # noqa: E501

        :param trading_method: The trading_method of this V2OrderData.  # noqa: E501
        :type: int
        """

        self._trading_method = trading_method

    @property
    def trans_no(self):
        """Gets the trans_no of this V2OrderData.  # noqa: E501


        :return: The trans_no of this V2OrderData.  # noqa: E501
        :rtype: str
        """
        return self._trans_no

    @trans_no.setter
    def trans_no(self, trans_no):
        """Sets the trans_no of this V2OrderData.


        :param trans_no: The trans_no of this V2OrderData.  # noqa: E501
        :type: str
        """

        self._trans_no = trans_no

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, V2OrderData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2OrderData):
            return True

        return self.to_dict() != other.to_dict()
