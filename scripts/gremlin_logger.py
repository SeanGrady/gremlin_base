#!/usr/bin/env python

import rospy


class GremlinLogger:
    def __init__(self):
        rospy.init_node('gremlin_logger')
        self.setup_subscribers()
        establish_database_connection(self)
        rospy.spin()

    def setup_subscribers(self):
        rospy.Subscribe('logging/sensor_data')

    def setup_publishers(self):
        pass


if __name__ == '__main__':
    gl = GremlinLogger()
