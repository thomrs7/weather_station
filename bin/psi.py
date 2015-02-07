#!/usr/bin/env python

import sys
from splunklib.searchcommands import \
    dispatch, StreamingCommand, Configuration, Option, validators, Integer


@Configuration()
class Psi(StreamingCommand):
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
        default='psi')


    def stream(self, events):
        """

        :param events:
        :return:
        """

        for event in events:
            self.logger.debug("start")
            try:
                p = float(event[self.SLP])

                event[self.field] = round(  0.491154  * p ,2)
            except:
                event[self.field] = "N/A"

            yield event


dispatch(Psi, sys.argv, sys.stdin, sys.stdout, __name__)
