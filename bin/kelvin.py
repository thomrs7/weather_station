#!/usr/bin/env python

import sys
from splunklib.searchcommands import \
    dispatch, StreamingCommand, Configuration, Option, validators, Integer


@Configuration()
class Kelvin(StreamingCommand):
    """ %(synopsis)

    ##Syntax

    %(syntax)

    ##Description

    %(description)

    """
    Temp = Option(
        doc=''' Temp Field ''', default='Temp')




    field = Option(
        doc=''' field to put value in ''',
        default='kelvin')


    def stream(self, events):
        """

        :param events:
        :return:
        """

        for event in events:
            self.logger.debug("start")
            try:
                temp = float(event[self.Temp])

                event[self.field] = round( (temp -32)/ 1.8 +  273.15 ,2)
            except:
                event[self.field] = "N/A"

            yield event


dispatch(Kelvin, sys.argv, sys.stdin, sys.stdout, __name__)
