#!/usr/bin/env python

import sys
from splunklib.searchcommands import \
    dispatch, StreamingCommand, Configuration, Option, validators, Integer


@Configuration()
class WindDir(StreamingCommand):
    """ %(synopsis)

    ##Syntax

    %(syntax)

    ##Description

    %(description)

    """

    Windd = Option(
        doc=''' Temp Field ''', default='Windd')

    field = Option(
        doc=''' field to put value in ''',
        default='Wind_dir')


    def stream(self, events):
        """

        :param events:
        :return:
        """
        dirs = ["", "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S",
                "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N"]
        for event in events:
            self.logger.debug("start")
            try:

                wd = float(event[self.Windd])

                event[self.field] = dirs[int(1 + abs(round(wd / 22.5, 0)))]
            except:
                event[self.field] = "N/A"

            yield event


dispatch(WindDir, sys.argv, sys.stdin, sys.stdout, __name__)
