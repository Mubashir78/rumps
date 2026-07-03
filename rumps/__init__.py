#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# rumps: Ridiculously Uncomplicated macOS Python Statusbar apps.
# Copyright: (c) 2020, Jared Suttles. All rights reserved.
# License: BSD, see LICENSE for details.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""
rumps
=====

Ridiculously Uncomplicated macOS Python Statusbar apps.

rumps exposes Objective-C classes as Python classes and functions which greatly simplifies the process of creating a
statusbar application.
"""

__title__ = 'rumps'
__version__ = '0.4.0'
__author__ = 'Jared Suttles'
__license__ = 'Modified BSD'
__copyright__ = 'Copyright 2020 Jared Suttles'

from . import notifications as _notifications
from .rumps import (separator as separator, debug_mode as debug_mode, alert as alert,
                    application_support as application_support, timers as timers,
                    quit_application as quit_application, timer as timer,
                    clicked as clicked, MenuItem as MenuItem, SliderMenuItem as SliderMenuItem,
                    TextFieldMenuItem as TextFieldMenuItem, Timer as Timer, Window as Window,
                    App as App, slider as slider, text_field as text_field)

notifications = _notifications.on_notification
notification = _notifications.notify
