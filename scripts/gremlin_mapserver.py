#!/usr/bin/env python

import rospy


class GremlinMapServer:
    def __init__(self):
        rospy.init_node('gremlin_mapserver')
        self.establish_database_connection()
        rospy.spin()

