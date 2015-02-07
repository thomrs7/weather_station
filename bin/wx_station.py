import json
import sys
import re
import urllib2

from splunklib.modularinput import *
import time

import urllib
import urllib2


class NoRedirection(urllib2.HTTPErrorProcessor):
    def http_response(self, request, response):
        return response

    https_response = http_response


class MyScript(Script):
    def get_scheme(self):
        scheme = Scheme("Weather Station")

        scheme.description = "Weather Station"

        scheme.use_external_validation = True
        scheme.use_single_instance = True

        station_argument = Argument("zip")
        station_argument.data_type = Argument.data_type_number
        station_argument.description = "Zip Code"
        station_argument.required_on_create = True
        # If you are not using external validation, add something like:
        #
        # setValidation("min > 0")
        scheme.add_argument(station_argument)

        return scheme

    def validate_input(self, validation_definition):
        zip = validation_definition.parameters["zip"]

        if zip == '':
            raise ValueError("Can not be blank")

    def stream_events(self, inputs, ew):

        polling_interval = 60 * 30


        # Go through each input for this modular input
        while True:
            for input_name, input_item in inputs.inputs.iteritems():

                ew.log("info", input_name)

                zip = input_item["zip"]

                values = {'inputstring': zip}
                data = urllib.urlencode(values)

                ew.log("info", data)

                event = Event()
                event.stanza = input_name

                try:
                    opener = urllib2.build_opener(NoRedirection,
                                                  urllib2.HTTPCookieProcessor())
                    response = opener.open(
                        "http://forecast.weather.gov/zipcity.php", data)
                    url = response.headers['Location'] + '&FcstType=json'

                    ew.log("info", url)

                    res = opener.open(url, data).read()

                    res = res.replace('\n', ' ').replace('\r', '')
                    res = re.sub('\s+', ' ', res).strip()

                    #ew.log('INFO', res)

                    event.sourceType = "json_no_timestamp"
                    event.index  ="wx"
                    event.data = res
                    ew.write_event(event)

                    # get Zone
                    # http://alerts.weather.gov/cap/wwaatmget.php?x=FLZ050&y=1
                    # alert  = Event()


                except Exception as e:
                    ew.log('ERROR', "ERROR ERROR ERROR")
                    ew.log('ERROR', e)

                # url = "http://w1.weather.gov/xml/current_obs/%s.xml" % \
                # zip
                # try:
                # req = urllib2.Request(url, headers=h)
                #     req.add_unredirected_header('User-Agent',
                #                                 'Custom User-Agent')
                #     connection = urllib2.urlopen(req)
                #     res = connection.read()
                #
                #     res = res.replace('\n', ' ').replace('\r', '')
                #     res = re.sub('\s+', ' ', res).strip()
                #     event.data = res
                #     ew.write_event(event)
                #     #ew.log('INFO', res)
                #
                # except Exception as e:
                #     ew.log('ERROR', e)


                time.sleep(1)
                ew.log('INFO', 'pause')

            time.sleep(polling_interval)


if __name__ == "__main__":
    sys.exit(MyScript().run(sys.argv))
