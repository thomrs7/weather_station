#!/usr/bin/env python

import sys
from splunklib.searchcommands import \
    dispatch, StreamingCommand, Configuration, Option, validators, Integer


@Configuration()
class Wfps(StreamingCommand):
    """ %(synopsis)

    ##Syntax

    %(syntax)

    ##Description

    %(description)

    """
    Winds = Option(
        doc=''' Temp Field ''', default='Winds')




    field = Option(
        doc=''' field to put value in ''',
        default='windfps')


    def stream(self, events):
        """

        :param events:
        :return:
        """

        for event in events:
            self.logger.debug("start")
            try:
                w = float(event[self.Winds])

                event[self.field] = round(  1.46667 * w ,2)
            except:
                event[self.field] = "N/A"

            yield event


dispatch(Wfps, sys.argv, sys.stdin, sys.stdout, __name__)
