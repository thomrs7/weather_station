#!/usr/bin/env python

import sys
from splunklib.searchcommands import \
    dispatch, StreamingCommand, Configuration, Option, validators, Integer


@Configuration()
class Reaumur(StreamingCommand):
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
        default='reaumur')


    def stream(self, events):
        """

        :param events:
        :return:
        """

        for event in events:
            self.logger.debug("start")
            try:
                temp = float(event[self.Temp])

                event[self.field] = round(( temp - 32) / 2.25 ,2)
            except:
                event[self.field] = "N/A"

            yield event


dispatch(Reaumur, sys.argv, sys.stdin, sys.stdout, __name__)
