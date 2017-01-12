#!/usr/bin/env python

import rospy
from database_functions import establish_database_connection


class GremlinMapServer:
    def __init__(self):
        rospy.init_node('gremlin_mapserver')
        engine, Session = establish_database_connection()
        self.engine = engine
        self.Session = Session
        rospy.spin()


if __name__ == '__main__':
    ms = GremlinMapServer()
