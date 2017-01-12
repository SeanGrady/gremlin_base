#!/usr/bin/env python

import rospy


class GremlinMapServer:
    def __init__(self):
        rospy.init_node('gremlin_mapserver')
        establish_database_connection(self)
        rospy.spin()

