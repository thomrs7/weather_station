#!/usr/bin/env python

import sys
from splunklib.searchcommands import \
    dispatch, StreamingCommand, Configuration, Option, validators, Integer


@Configuration()
class Kilopascals(StreamingCommand):
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
        default='kilopascals')


    def stream(self, events):
        """

        :param events:
        :return:
        """

        for event in events:
            self.logger.debug("start")
            try:
                p = float(event[self.SLP])

                event[self.field] = round(  33.8639 * (  p /10) ,2)
            except:
                event[self.field] = "N/A"

            yield event


dispatch(Kilopascals, sys.argv, sys.stdin, sys.stdout, __name__)
