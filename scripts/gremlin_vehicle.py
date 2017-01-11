#!/usr/bin/env python

import rospy


class GremlinVehicle:
    def __init__(self, vehicle_name):
        self.name = vehicle_name
        rospy.init_node('gremlin_vehicle')
        self.setup_subscribers()
        self.setup_vehicle()
        rospy.spin()

    def setup_vehicle(self):
        pass

    def setup_subscribers(self):
        mission_topic = 'mission/'+self.name
        rospy.Subscribe(mission_topic)

    def setup_publishers(self):
        pass

    def read_gps_data(self):
        pass

    def read_air_data(self):
        pass

    def read_RF_data(self):
        pass


if __name__ == '__main__':
    gv = GremlinVehicle()
