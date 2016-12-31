#!/usr/bin/env python

import rospy


class GremlinGCS:
    def __init__(self):
        rospy.init_node('gremlin_gcs')
        self.setup_subs()

    def setup_subs(self):
        pass


if __name__ == '__main__':
    gcs = GremlinGCS()
