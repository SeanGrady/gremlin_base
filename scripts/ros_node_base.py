class RosNodeBase:
    def __init__(self, name):
        self.hooks = ['subscriber_hook']
        print('init {}'.format(name))
        for hook in self.hooks:
            getattr(self, hook, lambda: None)()
        print('spin')


if __name__ == '__main__':
    rnb = RosNodeBase('base')
