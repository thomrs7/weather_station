#!/usr/bin/env python

import sys
from splunklib.searchcommands import \
    dispatch, StreamingCommand, Configuration, Option, validators, Integer


@Configuration()
class CricketChirps(StreamingCommand):
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
        default='chirps')


    def stream(self, events):
        """

        :param events:
        :return:
        """

        for event in events:
            self.logger.debug("start")



            cc = float(event[self.Temp]) - 40
            event[self.field] = round(cc, 2)



            yield event


dispatch(CricketChirps, sys.argv, sys.stdin, sys.stdout, __name__)
