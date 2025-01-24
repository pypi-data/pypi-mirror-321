import numpy as np
import os
from pymodaq.utils.daq_utils import ThreadCommand
from pymodaq.utils.data import DataFromPlugins, Axis, DataToExport
from pymodaq.control_modules.viewer_utility_classes import DAQ_Viewer_base, comon_parameters, main
from pymodaq.utils.parameter import Parameter

import pymodaq.utils.math_utils as mutils

from pymodaq_plugins_template.hardware.TANGO.tango_device import TangoDevice
from pymodaq_plugins_template.hardware.TANGO.tango_utils import TangoTomlConfig



# TODO:
# (1) change the name of the following class to DAQ_1DViewer_TheNameOfYourChoice
# (2) change the name of this file to daq_1Dviewer_TheNameOfYourChoice ("TheNameOfYourChoice" should be the SAME
#     for the class name and the file name.)
# (3) this file should then be put into the right folder, namely IN THE FOLDER OF THE PLUGIN YOU ARE DEVELOPING:
#     pymodaq_plugins_my_plugin/daq_viewer_plugins/plugins_1D
class DAQ_1DViewer_Spectrometer(DAQ_Viewer_base):
    """ Instrument plugin class for a 1D viewer.
    
    This object inherits all functionalities to communicate with PyMoDAQ’s DAQ_Viewer module through inheritance via
    DAQ_Viewer_base. It makes a bridge between the DAQ_Viewer module and the Python wrapper of a particular instrument.

    TODO Complete the docstring of your plugin with:
        * The set of instruments that should be compatible with this instrument plugin.
        * With which instrument it has actually been tested.
        * The version of PyMoDAQ during the test.
        * The version of the operating system.
        * Installation instructions: what manufacturer’s drivers should be installed to make it run?

    Attributes:
    -----------
    controller: object
        The particular object that allow the communication with the hardware, in general a python wrapper around the
         hardware library.
         
    # TODO add your particular attributes here if any
    """

    """Find right place for toml file"""
    print(os.getcwd())
    config = TangoTomlConfig('spectrometers', "hardware/TANGO/tango_devices.toml")
    print(config.addresses)
    params = comon_parameters + [{'title': 'Device address:', 'name': 'dev_address',
                                  'type': 'list','value':'SY-SPECTRO_1/Spectrometer/FE1',
                                  'limits': ['SY-SPECTRO_1/Spectrometer/FE1', 'SY-SPECTRO_1/Spectrometer/FE2', 'SY-SPECTRO_1/Spectrometer/FE3'],
                                  'readonly': False},]



    def ini_attributes(self):
        self.controller: TangoDevice = None
        self.device_proxy_success = False
        self._address = None

    def commit_settings(self, param: Parameter):
            pass

    def ini_detector(self, controller=None):

        self._address = self.settings.child('dev_address').value()
        print(self._address)
        self.ini_detector_init(controller, TangoDevice(address=self._address,
                           dimension= '1D',
                           attributes=["lambda", "intensity"]))

        initialized = self.controller.connected
        info = 'Controller ok'

        return info, initialized

    def close(self):
        pass

    def grab_data(self, Naverage=1, **kwargs):
        """Start a grab from the detector

        Parameters
        ----------
        Naverage: int
            Number of hardware averaging (if hardware averaging is possible, self.hardware_averaging should be set to
            True in class preamble and you should code this implementation)
        kwargs: dict
            others optionals arguments
        """

        xaxis, data = self.controller.value
        data = DataFromPlugins(name='Spectrum', data=[data],
                               axes=[Axis('Wavelength', data=xaxis)])

        self.dte_signal.emit(DataToExport('Spectrum', data=[data]))


    def stop(self):
        return ""


if __name__ == '__main__':
    main(__file__)
