#!/usr/bin/env python

import sys
from splunklib.searchcommands import \
    dispatch, StreamingCommand, Configuration, Option, validators, Integer


@Configuration()
class HeatIndex(StreamingCommand):
    """ %(synopsis)

    ##Syntax

    %(syntax)

    ##Description

    %(description)

    """
    Temp = Option(
        doc=''' Temp Field ''', default='Temp')

    Relh = Option(
        doc=''' Temp Field ''', default='Relh')


    field = Option(
        doc=''' field to put value in ''',
        default='heatIndex')


    def stream(self, events):
        """

        :param events:
        :return:
        """

        for event in events:

            self.logger.debug("start")
            try:
                T = float(event[self.Temp])
                RH = float(event[self.Relh])


                HI =(0.5 * (T + 61.0 + (T-68.0)*1.2 + (RH*0.094)))


                event[self.field] = round(HI,2)
            except:
                event[self.field] =  "N/A"

            yield event


dispatch(HeatIndex, sys.argv, sys.stdin, sys.stdout, __name__)
