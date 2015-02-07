#!/usr/bin/env python

import sys
from splunklib.searchcommands import \
    dispatch, StreamingCommand, Configuration, Option, validators, Integer


@Configuration()
class Knots(StreamingCommand):
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
        default='knots')


    def stream(self, events):
        """

        :param events:
        :return:
        """

        for event in events:
            self.logger.debug("start")
            try:
                w = float(event[self.Winds])

                event[self.field] = round(  0.8689762 * w ,2)
            except:
                event[self.field] = "N/A"

            yield event


dispatch(Knots, sys.argv, sys.stdin, sys.stdout, __name__)
