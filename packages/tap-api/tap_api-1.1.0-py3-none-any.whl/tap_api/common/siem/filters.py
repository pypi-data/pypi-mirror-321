"""
Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from enum import Enum


class ThreatType(Enum):
    URL = 'url'
    ATTACHMENT = 'attachment'
    MESSAGE_TEXT = 'messageText'


class ThreatStatus(Enum):
    ACTIVE = 'active'
    CLEARED = 'cleared'
    FALSE_POSITIVE = 'falsePositive'
