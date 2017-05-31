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

import ConfigParser
import sys
import os



def configinit(thresholds,ifo,channel,segxml,snr=['8','20','100']):
  metrics = """ 'Deadtime',
           'Efficiency',
           'Efficiency/Deadtime,
           """
  for i in snr:
      line = """'Efficiency | SNR>=%s',
             'Efficiency/Deadtime | SNR>=%s',
             """ % (i,i)
      metrics += line      
  metrics += """'Use percentage',
            'Loudest event by SNR'
            """

  defaults = {'type':'veto-flag',
              'event-channel':'%(ifo)s:GDS-CALIB_STRAIN',
              'event-generator':'Omicron',
              'metrics':metrics}

  parser = ConfigParser.SafeConfigParser(defaults)
              
  parser.add_section('plugins')
  parser.set('plugins','gwvet.tabs','')

  parser.add_section('states')
  parser.set('states','science','%(ifo)s:DMT-ANALYSIS_READY:1')

  parser.add_section('segment-database')
  parser.set('segment-database','url','https://segments.ligo.org')

  parser.add_section('omicron')
  parser.set('omicron','columns','time,snr,peak_frequency')
  parser.set('omicron','ligolw_columns','peak_time,peak_time_ns,snr,peak_frequency')

  for i in thresholds:
      tab = 'tab-' + str(i)
      name = str(channel)+str(i)
      shortname = str(i)
      flag = str(ifo)+":DCH-"+str(channel)+"_"+str(i)+":1"
      xml = str(segxml)

      parser.add_section(tab)
      parser.set(tab,'name',name)
      parser.set(tab,'shortname',shortname)
      parser.set(tab,'flags',flag)
      parser.set(tab,'states','science')
      parser.set(tab,'segmentfile',xml)

  return parser


