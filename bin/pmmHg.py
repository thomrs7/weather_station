#!/usr/bin/env python

import sys
from splunklib.searchcommands import \
    dispatch, StreamingCommand, Configuration, Option, validators, Integer


@Configuration()
class PmmHg(StreamingCommand):
    """ %(synopsis)

    ##Syntax

    %(syntax)

    ##Description

    %(description)

    """
    SLP = Option(
        doc=''' Temp Field ''', default='SLP')

    field = Option(
        doc=''' field to put value in ''',
        default='Pressure_mmHg')


    def stream(self, events):
        """

        :param events:
        :return:
        """

        for event in events:
            self.logger.debug("start")
            try:
                p = float(event[self.SLP])

                event[self.field] = round(25.4 * p, 2)
            except:
                event[self.field] = "N/A"

            yield event


dispatch(PmmHg, sys.argv, sys.stdin, sys.stdout, __name__)
