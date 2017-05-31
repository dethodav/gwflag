# -*- coding: utf-8 -*-
# Copyright (C) Derek Davis (2017)
#
# This file is part of gwFlag.
#
# gwFlag is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gwFlag is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gwFlag.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
from gwdetchar import const

def add_threshold_arguments(parser, **kwargs):
    """Add `threshold` and `threshold-multiplier` arguments to the given parser
    """
    a = parser.add_argument('-t', '--threshold', nargs='+', default=100.,
                    help='threshold, or list of thresholds, to produce flags with, '
                         ' (unit depends on method and channel choice)')
    b = parser.add_argument('-e', '--threshold-multiplier', type=int, default=0,
                    help='power of 10 for threshold, '
                         'default: 0')
    return a, b


def add_padding_arguments(parser, **kwargs):
    """Add `segment-end-pad` and `segment-start-pad` arguments to the given parser
    """
    a = parser.add_argument('-sf', '--segment-end-pad', type=int, default=0,
                    help='amount of time to add to the end of each segment')
    b = parser.add_argument('-si', '--segment-start-pad', type=int, default=0,
                    help='amount of time to add to the start of each segment')    

    return a, b

def add_channel_option(parser, **kwargs):
    """Add a `-c/--main-channel` option to this given parser
    """
    kwargs.setdefault('help', 'name of main (h(t)) channel, default: %(default)s')
    return parser.add_argument('-c', '--main-channel',
                    default='%s:GDS-CALIB_STRAIN' % const.IFO, **kwargs)

def add_state_option(parser, **kwargs):
    """Add a `-a/--state-flag` option to this given parser
    """
    kwargs.setdefault('help', 'restrict search to times when FLAG was active')
    return parser.add_argument('-a', '--state-flag', metavar='FLAG',
                    default='%s:DMT-ANALYSIS_READY:1' % const.IFO, **kwargs)
