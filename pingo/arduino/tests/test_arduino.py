import sys
import unittest
import platform
import pytest

import pingo
from pingo.test import level0
from pingo.test import level1
from pingo.test import not_has_module


@pytest.mark.skipif(not_has_module('pyfirmata'),
                    reason="pingo.arduino.Arduino requires pyfirmata installed")
class ArduinoFirmataTest(unittest.TestCase):

    def setUp(self):
        device = pingo.detect.detect._find_arduino_dev(platform.system())
        self.board = pingo.arduino.ArduinoFirmata(device)

        # Level0 Parameters
        self.vdd_pin_number = 0
        self.digital_output_pin_number = 13
        self.digital_input_pin_number = 12
        self.total_pins = 14

        # Level1 Parameters
        self.analog_input_pin_number = 'A4'
        self.expected_analog_input = 1004
        self.expected_analog_ratio = 0.98

    def tearDown(self):
        self.board.cleanup()


class ArduinoBasics(ArduinoFirmataTest, level0.BoardBasics):

    @unittest.skip('TODO: decide on the API to list all pins on an Arduino')
    def test_list_pins(self):
        pass

    @unittest.skip('This needs a jumper from Vdd to digital_input_pin_number')
    def test_jumpwire(self):
        pass


class ArduinoDigitalExceptions(ArduinoFirmataTest, level0.BoardExceptions):
    pass


class ArduinoAnalogRead(ArduinoFirmataTest, level1.AnalogReadBasics):
    pass


class ArduinoAnalogExceptions(ArduinoFirmataTest, level1.AnalogExceptions):
    pass


if __name__ == '__main__':
    unittest.main()
