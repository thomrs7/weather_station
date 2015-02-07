#!/usr/bin/env python

import sys
from splunklib.searchcommands import \
    dispatch, StreamingCommand, Configuration, Option, validators, Integer


@Configuration()
class WindChill(StreamingCommand):
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

    Winds = Option(
        doc=''' Temp Field ''', default='Winds')


    field = Option(
        doc=''' field to put value in ''',
        default='old_wind_chill')

    field2 = Option(
        doc=''' field to put value in ''',
        default='new_wind_chill')

    def stream(self, events):
        """

        :param events:
        :return:
        """

        for event in events:
            self.logger.debug("start")
            try:
                temp = float(event[self.Temp])
                RH = float(event[self.Relh])
                wind = float(event[self.Winds])


                old_chil = round((0.0817*(3.71*(pow(wind, 0.5)) + 5.81-0.25*wind)*(temp-91.4)+91.4),2)
                new_chil = round(((35.74+0.6215*temp-35.75*pow(wind,0.16)+0.4275*temp*pow(wind,0.16))),2)


                event[self.field] = round(old_chil,2)
                event[self.field2] = round(new_chil,2)
            except:
                event[self.field] =  "N/A"
                event[self.field2] = "N/A"
            yield event


dispatch(WindChill, sys.argv, sys.stdin, sys.stdout, __name__)
