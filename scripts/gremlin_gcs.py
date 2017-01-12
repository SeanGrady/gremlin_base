#!/usr/bin/env python

from ros_node_base import RosNodeBase


class GremlinGCS(RosNodeBase):
    def __init__(self):
        #super(GremlinGCS, self).__init__('gremlin_gcs')
        super().__init__('gremlin_gcs')

    def subscriber_hook(self):
        print('GremlinGCS hook')


if __name__ == '__main__':
    gcs = GremlinGCS()
