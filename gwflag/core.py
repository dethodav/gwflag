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

import os.path
import re
import warnings
from StringIO import StringIO

from gwdetchar import (cli, const, scattering, __version__)

import matplotlib
matplotlib.use('Agg')
from glue import segments
from gwpy.timeseries import TimeSeriesDict
from gwpy.segments import (DataQualityFlag, DataQualityDict,
                            Segment, SegmentList)
from gwpy.utils import gprint
import numpy


def ImportSegments(args):
    span = Segment(args.gpsstart, args.gpsend)
    if args.state_flag:
        state = DataQualityFlag.query(args.state_flag, int(args.gpsstart),
                                      int(args.gpsend), url=const.O1_SEGMENT_SERVER)
        for i, seg in enumerate(state.active):
            state.active[i] = type(seg)(seg[0], seg[1])
        state.coalesce()
        statea = state.active
        livetime = float(abs(statea))
        if args.verbose:
            gprint("Downloaded %d segments for %s [%.2fs livetime]"
                   % (len(statea), args.state_flag, livetime))
    else:
        statea = SegmentList([span])
    return statea

def FlagWrite(args,time,threshold,flag_segments):
  step = 1
  segs = segments.segmentlist()
  segs.extend([segments.segment(int(t), int(t)+step) for t in time])
  segs = segs.coalesce()

  start_time = []
  start_time.extend([t[0]-(args.segment_start_pad) for t in segs])
  end_time = []
  end_time.extend([t[1]+(args.segment_end_pad) for t in segs])

  threshstr = str(threshold).replace('.', '_')
  flag_name = '%s:DCH-%s_%s:1' % (args.ifo,args.main_channel, threshstr)

  flag = DataQualityFlag(flag_name, active=zip(start_time,end_time), known=[[args.gpsstart,args.gpsend]])
  flag_segments[threshold] = flag


