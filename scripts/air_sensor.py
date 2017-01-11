#!/usr/bin/env python

import rospy
import serial
from gremlin_base.srv import AirSensor


class AirSensor:
    def __init__(self, simulated):
        #TODO: init node should be anonymous or name should use vehicle name
        rospy.init_node("air_sensor")
        self._simulated = simulated
        self._serial_speed = 9600
        self._serial_speed = '/dev/ttyACM0'
        self._timeout = 1
        self._connection = None
        if not self._simulated:
            self.connect_to_sensor()
        self.setup_services()
        rospy.spin()

    def setup_services(self):
        """Setup ROS service for requesting air data"""
        data_service = rospy.Service(
            'air_sensor_data',
            AirSensor,
            self.air_data_service,
        )

    def air_data_service(self):
        """Read air data from sensor and return it."""
        data = self.read_air_data()
        return data

    def connect_to_sensor(self):
        """Connect to an air sensor and prepare it for reading data."""
        try:
            self._connection = serial.Serial(
                    self._serial_port,
                    self._serial_speed,
                    timeout= self._timeout
            )
            # Ask Michael about why this is necessary
            self._connection.write('{"msg":"cmd","usb":1}')
        except serial.serialutil.SerialException as e:
            rospy.logerr("Error opening serial port:\n %s", e.__repr__())

    def read_air_data(self):
        pass

if __name__ == '__main__':
    as = AirSensor()
