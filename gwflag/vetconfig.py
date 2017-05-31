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


#parser = ConfigParser.SafeConfigParser()

def configinit(parser,snr=['8','20','100']):
  parser.add_section('plugins')
  parser.set('plugins','gwvet.tabs','')

  parser.add_section('states')
  parser.set('states','Science','%(ifo)s:DMT-ANALYSIS_READY:1')

  parser.add_section('segment-database')
  parser.set('segment-database','url','https://segments.ligo.org')

  parser.add_section('omicron')
  parser.set('omicron','columns','time,snr,peak_frequency')
  parser.set('omicron','ligolw_columns','peak_time,peak_time_ns,snr,peak_frequency')


  parser.add_section('DEFAULT')
  parser.set('DEFAULT','type','veto-flag')
  parser.set('DEFAULT','event-channel','%(ifo)s:GDS-CALIB_STRAIN')
  parser.set('DEFAULT','event-generator','Omicron')

  metrics = """ 'Deadtime',
           'Efficiency',
           'Efficiency/Deadtime,
           """
  for i in snr:
      line = """'Efficiency | SNR>=%s',
             'Efficiency/Deadtime | SNR>=%s',
             """ % (i,i)
      metrics += line      
  metric += """'Use percentage',
            'Loudest event by SNR'
            """

  parser.set('DEFAULT','metrics',metrics)



def configflagtab(parser,threshold,ifo,channel,xml):

  tab = 'tab ' + str(threshold)
  name = str(channel)+str(threshold)
  shortname = str(threshold)
  flag = str(ifo)+":DCH-"+str(channel)+"_"+str(threshold)+":1"
  xml = str(xml)

  parser.add_section(tab)
  parser.set(tab,'name',name)
  parser.set(tab,'shortname',shortname)
  parser.set(tab,'flags',)
  parser.set(tab,'states','')
  parser.set(tab,'segmentfile','')



