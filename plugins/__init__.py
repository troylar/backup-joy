from kitchen_sink_logger import KitchenSinkLoger

class BasePlugin(object):
    def __init__(self, **kwargs):
        self.logger = kwargs.get('Logger', KitchenSinkLogger())
        self.name = kwargs.get('Name')
        self.logger.with_item('name', self.name)
        pass

    def pre_backup(self, **kwargs):
        self.logger.debug('Running pre_backup')

    def run_backup(self, **kwargs):
        self.logger.debug('Running backup')

