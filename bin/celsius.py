#!/usr/bin/env python

import sys
from splunklib.searchcommands import \
    dispatch, StreamingCommand, Configuration, Option, validators, Integer


@Configuration()
class Celsius(StreamingCommand):
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
        default='celsius')


    def stream(self, events):
        """

        :param events:
        :return:
        """

        for event in events:
            self.logger.debug("start")
            try:
                temp = float(event[self.Temp])

                event[self.field] = round( temp - 32 /  1.8000)
            except:
                event[self.field] = "N/A"

            yield event


dispatch(Celsius, sys.argv, sys.stdin, sys.stdout, __name__)
