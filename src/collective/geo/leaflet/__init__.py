# -*- coding: utf-8 -*-
"""Init and utils."""

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.geo.leaflet')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
